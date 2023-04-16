#import necessary external modules
import numpy as np
import pandas as pd
import math
import matplotlib.pyplot as plt
import numpy as np
#import modules from visualiser and modeller
from modeller import pre_collision, post_collision_electron, post_collision_photon
from visualiser import Animator

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

def main():
    #startx = 200 #coordinates photon passes through
    #starty = 203 #coordinates photon passes through
    #startz = 69 #coordinates photon passes through
    #photon_pre_energy = 0.8 #measured in MeV
    #photon_post_energy = 0.75 #measured in MeV

    tf = int(input('How long should the simulation run for (in seconds)? '))
    startx = int(input('Enter an x coordinate in the path of the incoming  photon: '))
    starty = int(input('Enter a y coordinate in the path of the incoming  photon: '))
    startz = int(input('Enter a z coordinate in the path of the incoming  photon: '))
    photon_pre_energy = float(input('Enter the initial energy of the photon in MeV: ' ))
    photon_post_energy = float(input('Enter the energy of the photon after the collision in MeV: '))

    tf = 300
    pvelocity = 3 #photon velocity (measured in 10^8m/s)
    rest_energy_e = 0.512 #measured in MeV
    t0 = 0 # initial time
    #tf = 300 # end time
    dt = 1 # time step
    time = np.arange(t0, tf, dt, dtype='float') # time array

    p1, timepre = pre_collision(time, pvelocity, startx, starty, startz) #create database to model incoming photon
    p1 = p1.reindex(index=p1.index[::-1]) #reverse photon database so photon approaches origin instead
    p1["t"] = p1["t"].values[::-1] #but dont reverse time column

    #create databases to model photon and electron post collision
    pcomps = [p1.loc[0].at["vx"], p1.loc[0].at["vy"], p1.loc[0].at["vz"]] #vector components of photon velocity
    p2, ptime2, p2comps, photon_angle = post_collision_photon(time, pvelocity, photon_pre_energy, photon_post_energy, pcomps, rest_energy_e)
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
    plt.show()

main()