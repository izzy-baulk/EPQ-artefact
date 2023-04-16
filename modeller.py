import numpy as np
import sympy as sp
import pandas as pd
import numpy as np
import math
from scipy import constants
from extramodules import vector_derivative, evaluate_vector

def calcmag(expected, comp1, comp2, comp3, name):
    actual = math.sqrt(comp1**2 + comp2**2 + comp3**2)
    print('expected magnitude of {} is {}'.format(name, round(expected, 3)))
    print('actual magnitude of {} is {}\n'.format(name, round(actual, 3)))

def vector_magnitude(comps):
    comp1 = comps[0]
    comp2 = comps[1]
    comp3 = comps[2]
    mag = math.sqrt(comp1**2 + comp2**2 + comp3**2)
    return(mag)

def get_components_pre(vmag, x, y, z):
    #find components of vector from its magnitude
    displacement_vector = [x, y, z]
    displacement_mag = vector_magnitude(displacement_vector)
    vcomponents = []
    for component in displacement_vector:
        unitv_component = component / displacement_mag #get unit vector of displacement vector
        vector_component = unitv_component * vmag #get velocity component from unit vector
        vcomponents.append(vector_component)
    return vcomponents

def propagate(time, v0x, v0y, v0z):
    t = sp.symbols('t') # t is symbolic variable to represent time here, allows algebra to be used 
    R = [(0 + v0x*t), (0 + v0y*t), (0 + v0z*t)] #equation for position
    V = vector_derivative(R, t) # velocity = derivitive of position  
    propagation = []
    for second in time: #so each second
        r, r_mag = evaluate_vector(R, second, t) #subs in timestep to functions of xyz in R to get position
        v, v_mag = evaluate_vector(V, second, t) #subs in timstep to velocityy functions from R to evaluate velocity

        iteration_results = {'t': second, 'rx': r[0], 'ry': r[1], 'rz': r[2], 'r_mag': r_mag,
                            'vx': v[0], 'vy': v[1], 'vz': v[2], 'v_mag': v_mag}

        propagation.append(iteration_results)
    df = pd.DataFrame(propagation)
    #cut down dataframe to size of axes
    df.drop(df[df['rx'] > 500].index, inplace = True)
    df.drop(df[df['rx'] < -500].index, inplace = True)
    df.drop(df[df['ry'] > 500].index, inplace = True)
    df.drop(df[df['ry'] < -500].index, inplace = True)
    df.drop(df[df['rz'] > 500].index, inplace = True)
    df.drop(df[df['rz'] < -500].index, inplace = True)
    #cut down database to size of time array
    timeEnd = (df['t'].iloc[-1]) 
    time = np.delete(time, np.where
    (time >= timeEnd), axis=0)
    return(df, time)

def electron_velocity(energy):
    #calculate velocity of electron using relativistic formula
    mass = 9.1*(10**-31)
    energy = energy * 1.60218e-13 #convert MeV to J
    c = constants.c
    denom = (energy/(mass*(c**2))) + 1
    root = 1 - (1/denom)**2
    velocity = c * root
    velocity = velocity / (10**8)
    return velocity

def electron_recoil_angle(energy_photon_pre, energy_photon_post, rest_energy_e):
    #equation for electron recoil angle, split into steps to make computation easier
    changein = energy_photon_pre - energy_photon_post 
    tanthetaelectron = (rest_energy_e / (energy_photon_pre + rest_energy_e)) * math.sqrt(((2*energy_photon_pre*energy_photon_post)-(rest_energy_e*changein))/(rest_energy_e*changein))
    thetaelectron = math.degrees(math.atan(tanthetaelectron)) #so this is electron recoil angle
    return(180 - thetaelectron) #we want angle between incoming photon and electron, so the obtuse one

def photon_recoil_angle(energy_photon_pre, energy_photon_post, rest_energy_e):
    #equation for photon recoil angle, split into steps to make computation easier
    changein = energy_photon_pre - energy_photon_post 
    costheta = 1 - ((rest_energy_e*changein)/(energy_photon_pre*energy_photon_post))
    thetaphoton = math.degrees(math.acos(costheta))
    return(180 - thetaphoton) #we want angle between incoming photon and outgoing photon, so the obtuse one

def threedcomponents(amag, acomps, theta, bmag, type):
    theta = math.radians(theta)
    ax = acomps[0]
    ay = acomps[1]
    az = acomps[2]
    xangle = math.asin(az / amag) #angle between xy plane and magnitude
    ifirst = amag * math.cos(xangle) #adjacent component of first vector triangle
    if type == 'e':
        theta = theta - xangle
    else:
        theta = theta + xangle
    isecond = bmag * math.cos(theta) #adjacent component of second vector triangle
    sf = ifirst / isecond #shcale factor from adjacent components of each vector
    bz = bmag * math.sin(theta)
    if type == 'e':
        bz *= -1
    bx = ax / sf #scale down component by sf
    by = ay / sf #scale down component by sf
    return bx, by, bz  

def twodcomponents(amag, acomps, theta, bmag, type):
    theta = math.radians((theta))
    ax = acomps[0]
    ay = acomps[1]
    az = acomps[2]
    i = bmag * math.cos(theta) #adjacent component of vector triangle
    sf = amag / i #scale factor from ratio of magnitude of a to adjacent component
    if acomps[2] == 0:
        bz = bmag * math.sin(theta) #opposite component of vector triangle
        bx = ax / sf #other components calculated from scale factors
        by = ay / sf
        if type == 'e':
            bz *= -1
    elif acomps[1] == 0:
        by = bmag * math.sin(theta) #opposite component of vector triangle
        bz = az /sf #other components calculated from scale factors
        bx = ax /sf
        if type == 'e':
            by *= -1
    else:
        bx = bmag * math.sin(theta) #opposite component of vector triangle
        by = ay / sf #other components calculated from scale factors
        bz = az / sf
        if type == 'e':
            bx *= -1
    return bx, by, bz 

def onedcomponents(acomps, theta, bmag, type):
    theta = math.radians(theta)
    if (acomps[1] == 0 and acomps[2] == 0):
        Bx = bmag * math.cos(theta) #adjacent component of vector
        By = acomps[1] #zero component
        Bz = bmag * math.sin(theta) #opposite component of vector
        if type == 'e': #appropriate reflection in axis
            Bz *= -1
    elif (acomps[0] == 0 and acomps[1] == 0):
        Bx = acomps[0] #zero component
        Bz = bmag * math.cos(theta) #adjacent component of vector
        By = bmag * math.sin(theta) #opposite component of vector
        if type == 'p': #appropriate reflection in axis
            By *= -1
    else:
        By = bmag * math.cos(theta) #adjacent component of vector
        Bz = bmag * math.sin(theta) #opposite component of vector
        Bx = acomps[2]  #zero component
        if type == 'e': #appropriate reflection in axis
            Bz *= -1
            Bx *= -1
    return Bx, By, Bz   
    
def pre_collision(time, mag, x, y, z):
    t = sp.symbols('t') # symbolic variable for time
    #define xyz positions as functions of time
    displacement_vector = get_components_pre(mag, x, y, z)
    r0x = displacement_vector[0]
    r0y = displacement_vector[1]
    r0z = displacement_vector[2]
    df, time = propagate(time, r0x, r0y, r0z)
    return(df, time)

def post_collision_electron(time, pvelocity, energy_photon_pre, energy_photon_post, pcomps, rest_energy_e):
    energy_electron_post = (energy_photon_pre - energy_photon_post) + rest_energy_e
    evelocity = electron_velocity(energy_electron_post)
    electron_angle = electron_recoil_angle(energy_photon_pre, energy_photon_post, rest_energy_e)
    if (pcomps[0] == 0 and pcomps[1] == 0) or (pcomps[1] == 0 and pcomps[2] == 0) or (pcomps[0] == 0 and pcomps[2] == 0):
        bx, by, bz = onedcomponents(pcomps, electron_angle, evelocity, 'e')
    elif (pcomps[0] == 0) or (pcomps[1] == 0) or (pcomps[2] == 0):
        bx, by, bz = twodcomponents(pvelocity, pcomps, electron_angle, evelocity, 'e')
    else:
        bx, by, bz = threedcomponents(pvelocity, pcomps, electron_angle, evelocity, 'e')
    bcomps = [bx, by, bz]
    calcmag(evelocity, bx, by, bz, 'electron velocity')
    df, time = propagate(time, bx, by, bz)
    return(df, time, bcomps, electron_angle)

def post_collision_photon(time, pvelocity, energy_photon_pre, energy_photon_post, pcomps, rest_energy_e):
    pmag = pvelocity 
    photon_angle = photon_recoil_angle(energy_photon_pre, energy_photon_post, rest_energy_e)
    if (pcomps[0] == 0 and pcomps[1] == 0) or (pcomps[1] == 0 and pcomps[2] == 0) or (pcomps[0] == 0 and pcomps[2] == 0):
        bx, by, bz = onedcomponents(pcomps, photon_angle, pmag, 'p')
    elif (pcomps[0] == 0) or (pcomps[1] == 0) or (pcomps[2] == 0):
        bx, by, bz = twodcomponents(pmag, pcomps, photon_angle, pmag, 'p')
    else:
        bx, by, bz = threedcomponents(pvelocity, pcomps, photon_angle, pmag, 'p')        
    bcomps = [bx, by, bz]
    calcmag(pmag, bx, by, bz, 'photon velocity')
    df, time = propagate(time, bx, by, bz)
    return(df, time, bcomps, photon_angle)