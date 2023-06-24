#import necessary external modules
import numpy as np
import pandas as pd
import math
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import os
from tkinter import *
from tkinter import ttk
#import modules from visualiser and modeller
from modeller import pre_collision, post_collision_electron, post_collision_photon
from visualiser import Animator
from matplotlib import animation

#initialisation GUI
matplotlib.use('TkAgg')

#calculate vector magnitude from components
def vector_magnitude(comps):
    comp1 = comps[0]
    comp2 = comps[1]
    comp3 = comps[2]
    mag = math.sqrt(comp1**2 + comp2**2 + comp3**2)
    return(mag)

#function to find length of time animation should run for post-collision
def time_chop(df1, df2, df1t, df2t):
    if len(df1t) > len(df2t):
        time = df2t
        df1.drop(df1[df1['t'] >= df2t[-1]].index, inplace = True)
    else:
        time = df1t
        df2.drop(df2[df2['t'] >= df1t[-1]].index, inplace = True)
    return df1, df2, time

#calculates angle between vectors to check if its the expected angle
def angle_checker(postcomps, precomps, expected, name):
    dot_prod = postcomps[0]*precomps[0] + postcomps[1]*precomps[1] + postcomps[2]*precomps[2]
    magpre = vector_magnitude(precomps)
    magpost = vector_magnitude(postcomps)
    cosine = dot_prod / (magpre * magpost) 
    theta = math.acos(cosine)
    theta = math.degrees(theta)
    print('expected angle between {} and incoming photon is {} degrees'.format(name, round(expected, 3)))
    print('actual angle between {} and incoming photon is {} degrees\n'.format(name, round(theta, 3)))  

def filler_databases(time):
    feature_list = ['t', 'rx', 'ry', 'rz', 'r_mag', 'vx', 'vy', 'vz', 'v_mag']
    df = pd.DataFrame(0, index=np.arange(len(time)), columns=feature_list) #create empty database as long as specified time period
    df['t'] = df.index
    return df

def format_databases(df, dftimefrom):
    df['t'] = df['t'].apply(lambda x: x + dftimefrom.iloc[-1].at['t']) #add the last time value from the previous database to enure no jumps in 't' column
    return df

def main(startx, starty, startz, photon_pre_energy, photon_post_energy, save, f):
    tf = 200
    pvelocity = 3 #photon velocity (measured in 10^8m/s)
    rest_energy_e = 0.512 #measured in MeV
    t0 = 0 # initial time
    dt = 1 # time step
    time = np.arange(t0, tf, dt, dtype='float') # time array

    p1, timepre = pre_collision(time, pvelocity, startx, starty, startz) #create database to model incoming photon
    p1 = p1.reindex(index=p1.index[::-1]) #reverse photon database so photon approaches origin instead
    p1["t"] = p1["t"].values[::-1] #but dont reverse time column

    #create databases to model photon and electron post collision
    pcomps = [p1.loc[0].at["vx"], p1.loc[0].at["vy"], p1.loc[0].at["vz"]] #vector components of photon velocity
    p2, ptime2, p2comps, photon_angle = post_collision_photon(time, pvelocity, photon_pre_energy, photon_post_energy, pcomps, rest_energy_e)
    print(p2)
    e2, etime2, e2comps, electron_angle = post_collision_electron(time, pvelocity, photon_pre_energy, photon_post_energy, pcomps, rest_energy_e)

    #find database with shorter runtime and cut other one to same size
    p2, e2, timepost = time_chop(p2, e2, ptime2, etime2)

    #create filler databases for the electron before the collision, and outgoing photon before the collision
    #this allows subplots for each to be created, as well as different colours to be used
    e1 = filler_databases(timepre)
    emptyp1 = filler_databases(timepre)
    emptyp2 = filler_databases(timepost)

    #make sure time columns for each database follow on from one another before concatenation
    p2 = format_databases(p2, emptyp1)
    e2 = format_databases(e2, e1)
    emptyp2 = format_databases(emptyp2, p1)
    incomingphoton = pd.concat([p1, emptyp2]) #dataframe to model whole process of incoming photon
    outgoingphoton = pd.concat([emptyp1, p2]) #dataframe to model whole process of photon post collision
    electron = pd.concat([e1, e2]) #dataframe to model whole process of electron (pre and post collision)
    timearray = np.concatenate([timepre, timepost]) #array to represent time for whole animation to take place over

    #check angles between vectors are as expected
    angle_checker(p2comps, pcomps, photon_angle, 'outgoing photon')
    angle_checker(e2comps, pcomps, electron_angle, 'electron')
    electron_angle = int(180 - electron_angle)
    photon_angle = int(180 - photon_angle)

    #create and run animation, show plots
    animator = Animator(simulation_results1=electron, simulation_results2=incomingphoton, simulation_results3=outgoingphoton)
    anim = animator.animate(timearray, electron_angle, photon_angle)
    if save == 'Y':
        writervideo = animation.FFMpegWriter(fps=60) 
        anim.save(f, writer=writervideo)
    else:
        plt.show()


def makeform(root, fields):
    entries = {}
    error = Label(root, text="", fg='red', font=('Helvetica 13'))
    error.pack()
    for field in fields:
        row = Frame(root)
        if field == 'x coordinate' or field == 'y coordinate' or field == 'z coordinate':
            validation = ' (integer between -500 and 500)'
        elif field == 'initial energy of photon':
            validation = ' (between 0-30 MeV)'
        elif field ==  'final energy of photon':
            validation = ' (must be smaller than initial energy, but above 0)'
        elif field == 'save file? ':
            validation = ' (Y/N)'
        elif field == 'filepath':
            validation = ' (enter valid path to folder, or enter "D" to use default path "./")'
        else:
            validation = ''    
        lab = Label(row, text=field+ validation + ": ", anchor='w')
        ent = Entry(row)
        row.pack(side = TOP, fill = X, padx = 5 , pady = 5)
        lab.pack(side = LEFT)
        ent.pack(side = RIGHT, expand = YES, fill = X)
        entries[field] = ent
    return entries, error


def validate(entries, root, error):
    startx = int(entries['x coordinate'].get())
    starty = int(entries['y coordinate'].get())
    startz = int(entries['z coordinate'].get())
    photon_pre_energy = float(entries['initial energy of photon'].get())
    photon_post_energy= float(entries['final energy of photon'].get())
    save = entries['save file? '].get()
    filepath =  entries['filepath'].get()
    filename = entries['filename'].get()
    path = ''
    if save == 'Y':
            if filepath == 'D':
                path = './' + filename + '.mp4'
            else:
                path = filepath + '/' + filename + '.mp4'
    if startx < -500 or startx > 500 or starty < -500 or starty > 500 or startz < -500 or startz > 500 or photon_pre_energy < 0 or photon_pre_energy > 30 or photon_post_energy < 0 or photon_post_energy > photon_pre_energy:
        error['text'] = 'Please enter valid data'
    else:      
        if (os.path.exists(filepath) == False) and (filepath != 'D') and (save != 'N'):
            error['text'] = 'Please enter valid data/file path'  
        else:
            root.quit()
            main(startx, starty, startz, photon_pre_energy, photon_post_energy, save, path)   

def run():
    fields = ('x coordinate', 'y coordinate', 'z coordinate', 'initial energy of photon', 'final energy of photon', 'save file? ', 'filepath', 'filename')
    root = Tk()
    root.geometry('1000x600')
    root.title('Simulation Setup')
    ents, error = makeform(root, fields)
    b1 = Button(root, text = 'submit',
        command=(lambda e = ents: validate(e, root, error)))
    b1.pack(side = LEFT, padx = 5, pady = 5)
    b3 = Button(root, text = 'Quit', command = root.quit)
    b3.pack(side = LEFT, padx = 5, pady = 5)
    root.mainloop() 

if __name__ == '__main__':
    run()
