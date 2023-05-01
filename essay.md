# A Python program to simulate and visualise the Compton scattering effect

### I. Abstract
### II. Introduction
### III. Background
### IV. Methodology
### V. Skill Development



## I. Abstract

## II. Introduction

I chose to write a Python program to give me an opportunity to develop my skills in object-orientated program, alongside showcasing my existing procedural programming abilities. As I hope to study physics or engineering at university, I decided that modelling a particle physics phenomenon would deepen my knowledge in this field, and provide an opportunity for me to draw links between studies in this area to future studies in science and technology. I made the choice to visualise this model in a 3D plot to further my understanding of the importance of graphical interfaces in research presentation. 

## III. Background

### Compton Scattering

The Compton scattering effect describes the interaction that takes place between a photon of energy between 30keV-30MeV, and a free, stationary electron, where eV is energy measured in electronvolts. One electron volt is the energy gained by an electron when accelerated through a potential difference of 1 volt[^1]. When these particles collide, the photon imparts some momentum to the electron, causing a change in direction and wavelength of the photon, and a change in the velocity of the electron. The illustration below shows this process, with *λ* representing the incoming photon, *λ’* representing the photon after the collision, *θ* representing photon scattering angle, *Φ* representing electron scattering angle, and *e-* representing the scattered electron[^2]

<img width="278" alt="image" src="https://user-images.githubusercontent.com/79797035/230788567-631402ac-8141-4fac-afb9-6591555b3d1c.png"></img>
###### Fig 1 - illustration of a collision involving compton scattering [^2]

The standard equation for Compton scattering, relating photon wavelength pre and post collision, electron rest energy, and photon scattering angle, was established by Arthur Compton and won him the Nobel Prize in 1927, and is shown below. *h* is the Planck constant, *c* is the speed of light, *m* is electron mass: 

<img width="211" alt="Screenshot 2023-04-20 at 09 38 51" src="https://user-images.githubusercontent.com/79797035/233309865-8a2b25cd-1e07-4d70-9d08-bf58d6ccff7f.png"></img>
###### Eqn 1 - equation for compton effect using photon wavelengths[^2]

Using the relationship *λ = hc/E*, this equation can be rearranged to give:

<img width="278" alt="image" src="https://user-images.githubusercontent.com/79797035/230788650-39f581dd-9a25-4b5d-a908-34eaa4a7b1bc.png"></img>
###### Eqn 2 - equation for compton effect using photon energies[^3]

Using E<sub>o</sub> = m<sub>e</sub>c<sup>2</sup>, where E<sub>o</sub> represents the rest energy of an electron, this equation can be rearranged to give:

<img width="278" alt="image" src="https://user-images.githubusercontent.com/79797035/230788799-60cd5759-049a-4616-96c5-0ce35c455c70.png"></img>
###### Eqn 3 -  equation for compton effect using electron rest energy[^3]

### Python and Additional Libraries

Python is a high-level, general purpose programming language with support for countless graphical, scientific, and mathematical additional libraries, making it the ideal language for this simulation. A library is a collection of reusable chunks of code written to carry out a specific set of tasks, and distributed freely online. For example, graphics libraries contain code that can create 2D and 3D plots of data, and database libraries contain code that can create more complex and powerful databases than the Python programming language alone. I chose matplotlib to be my graphics library, and numpy and pandas to handle database creation and manipulation, as these are libraries built with the intention to be used in conjunction with one another, and libraries that I had previously used in other projects. Python has support for object-orientated programming (OOP), which is a type of programming based on the concept of ‘objects’, or standalone chunks of information used to describe specific items and events. Python also has support for procedural programming (PP), where instructions are created and executed in a specific order to carry out a series of operations on these objects. Both types of programming had to be utilised in my project, with OOP being vital to creating the animation behind the visualisation part of the program, and PP forming the basis of the modelling side of the code.

### Relativity and Scale

If using the standard equatiion for velocity from kinetic energy, 

<img width="143" alt="Screenshot 2023-04-12 at 11 17 29" src="https://user-images.githubusercontent.com/79797035/231428681-1e629c7d-e989-4fc9-8b1a-d38866267347.png">

a problem arises when calculating electron velocities at high energy levels. Because the mass of an electron is so small, 9.1x10<sup>-31</sup>kg, using this formula can lead to velocities above the speed of light being calculated, which must be disregarded as no object with mass can travel faster than the speed of light. This error arises because this formula applies to classical mechanics, where it is assumed that absolute time and space exist outside of any observer, and so the speed of light can vary from one reference frame to another. Relativistic mechanics instead states that the speed of light is constant in all reference frames. This becomes significant as the speed of an object passes over half the speed of light, as special relativity states that an object's relativistic kinetic energy will increase to infinity, even as its Newtonian kinetic energy continues to increase at a steady rate.

<img width="488" alt="Screenshot 2023-04-12 at 15 24 49" src="https://user-images.githubusercontent.com/79797035/231488369-423e50dc-360c-4e82-a2af-9d9a91516f57.png"></img>
###### Fig 2 - graph showing how kinetic energy changes with speed[^4]

Therefore, the relativistic equation for velocity must be used, which can be found from rearranging the relativistic equation for kinetic energy.

<img width="189" alt="Screenshot 2023-04-12 at 15 27 48" src="https://user-images.githubusercontent.com/79797035/231489343-d9157da8-030d-4b28-8d6c-6defe5f78042.png"></img>

<img width="232" alt="Screenshot 2023-04-12 at 11 07 18" src="https://user-images.githubusercontent.com/79797035/231426341-831696bf-4e6d-4220-af0f-9fc6d0f564a0.png"></img>

###### Eqn 4 - relativistic equation for velocity [^4]

While using this equation ensures the correct electron velocity can be calculated, when working with energies in the range of MeV, the velocities calculated will still be a large fraction of the speed of light. As computers cannot run simulations at a frame rate anywhere nearing the speed of light, I chose to instead create my plots with a scale of 1 unit = 10<sup>8</sup>m. The velocities of the particles could therefore be scaled down, allowing their relative magnitudes to remain accurate, but allowing the animation to run at a reasonable frame rate. 

## IV. Methodology

### Abstraction and Decomposition

After finishing my research into Compton scattering, and confirming this phenomenon could be suitably visualised on a 3D plot, I used the processes of abstraction and decomposition to plan my program before beginning work on the code. Abstraction in programming refers to the separation of unnecessary details from the information and tasks required to solve a problem, while decomposition is the process of breaking down a problem into smaller, more simple tasks, for each an individual coded solution can be found. Abstraction first led me to decide on the following input variables, output variables, intermediate variables, and constants for my code, with variables being values used to store information under specific monikers, through which they can be defined, accessed and updated.

**INPUTS** - photon energy pre-collision (*E<sub>i</sub>*), photon energy post-collision (*E<sub>r</sub>*)

**INTERMEDIATES** - electron energy post collision (*E<sub>k</sub>*)

**OUTPUTS**- electron recoil angle (*Φ*), photon recoil angle (*θ*), electron velocity post-collision (*V*)

**CONSTANTS** - velocity of photon (*c*), electron rest energy (*E<sub>0</sub>*), electron mass (*m*)

I decided to use these specific variables as they allowed me to use equations within my code that had already been proved and verified by other physicists, reducing chances of error in my program as I did not need to do any complex algebraic manipulation. However, to make sure I understood where these equations were coming from, I wrote my own proofs separately and checked these against the known ones. I was also able to better test my code, as I could find examples of calculations using these equations, the outputs of which I could check against the outputs of the calculations carried out within my program. The equations I ended up using were as follows:

<img width="278" alt="image" src="https://user-images.githubusercontent.com/79797035/230789096-d4bf6c2e-861d-46e5-b7db-c5dbaab77439.png"></img>
###### Eqn 5 - equation for electron recoil angle[^3]

<img width="127" alt="Screenshot 2023-04-10 at 15 18 22" src="https://user-images.githubusercontent.com/79797035/230919467-3e48056b-7941-4157-85dd-55ed9369bf3a.png"></img>
###### Eqn 6 - equation for photon recoil angle[^3]

During decomposition, after analysing another piece of code used to create 3D animations using matplotlib, I decided to base the part of my program that would deal with visualisation off of this code, creating a class to contain my animation and plotting objects, and data frames to store data generated by my model[^5]. Classes in Python are complex data structures used to create instances of objects, and perform operations on these objects. This allowed me to avoid unnecessarily writing new code to carry out the same tasks, and let me spend more time on writing the rest of the program, which had to be written from scratch. I also made the choice to use some utility functions used in vector calculations and manipulation defined within this program within my own code, and copied these into a separate file from which they could be called as necessary. Doing this allowed me to save time during the early stages of the programming process, and keep track of which functions were my own work, and which had been written by others.

Instead of using one file to hold my entire project, I chose to split my project into three separate Python files, one to contain the visualisation code, one to contain the modelling code, and one to act a control program to run the two and pass information between them. This led me to the creation of the following flowchart to plan my project:

![image](https://user-images.githubusercontent.com/79797035/230920731-48912f20-61ed-485c-b46d-25d0ec687bba.png)


### Initialisation

The first step I took was to create the plots in which the data generated by my model would be outputted. I decided to work with a three-dimensional plot to make my model different to others that I researched before beginning this project, which work in two dimensions. I also here made the decision to use the ```FuncAnimation``` subclass of matplotlib to create the actual animation. This function creates an animation by creating outputted data for the first frame, and modifying this subsequently using a function that is called every frame, making it the most straightforward animation function to use. Its alternative, ```ArtistAnimation```, is used when data is stored on different Artists[^6], with Artists being objects that can use renderers to directly draw onto a figure[^7]. In hindsight, if I had the time, I would have created a version of my visualiser function using ```ArtistAnimation``` as well, and compared the two on memory efficiency, time efficiency, and suitability. 

Working in the ‘lab frame’, where the electron with which the photon collides is centred in the plot in which the animation is created REFERENCE, IN ```visualiser.py```, I defined  an ```Animator``` class and created the main figure and subplots. Here, I initilialised three trajectory objects, with a corresponding subplot each, with one instance representing the photon pre collision, one representing the photon post, and one representing the elcctron. I decided that the only variables I needed to track on each subplot were position and velocity, as acceleration would be constant throughout. I wrote this code under the ‘init’ function so that it would run automatically as soon as the ```Animator``` class is called by the control file, without the function having to be called by name. 

``` python
class Animator:
    def __init__(self, simulation_results1, simulation_results2, simulation_results3):
        # load in dataframes from modelling stage 
        self.simulation_results1 = simulation_results1
        self.simulation_results2 = simulation_results2
        self.simulation_results3 = simulation_results3
        #  configure plots and data structures
        self.fig = plt.figure(figsize=(15, 8))
        self.fig.subplots_adjust(left=0.05,
                                 bottom=None,
                                 right=0.95,
                                 top=None,
                                 wspace=None,
                                 hspace=0.28)
        gs = gridspec.GridSpec(3, 3)
        #create main animation plot
        self.ax1 = self.fig.add_subplot(gs[:, 0], projection='3d')

        #velocity and magnitude subplots for electron
        self.axElectronA = self.fig.add_subplot(gs[2, 2])
        self.axElectronB = self.axElectronA.twinx()
        self.rvte, = self.axElectronA.plot([], [], 'g-')
        self.vvte, = self.axElectronB.plot([], [], 'r-')
        self.rmag_texte = self.axElectronB.text(0, 0, '', size=12, color='b')

        #velocity and magnitude subplots incoming photon
        self.axPhoton1A = self.fig.add_subplot(gs[0, 2])
        self.axPhoton1B = self.axPhoton1A.twinx()
        self.rvtp1, = self.axPhoton1A.plot([], [], 'g-')
        self.vvtp1, = self.axPhoton1B.plot([], [], 'r-')
        self.rmag_textp1 = self.axPhoton1B.text(0, 0, '', size=12, color='b')        

        #outgoing photon
        self.axPhoton2A = self.fig.add_subplot(gs[1, 2])
        self.axPhoton2B = self.axPhoton2A.twinx()
        self.rvtp2, = self.axPhoton2A.plot([], [], 'g-')
        self.vvtp2, = self.axPhoton2B.plot([], [], 'r-')
        self.rmag_textp2 = self.axPhoton2B.text(0, 0, '', size=12, color='b')

        self.set_axes_limits()
        self.fig.tight_layout() #set appropriate spacing between plots

        #create a trajectory object for each particle
        self.trajectory1, = self.ax1.plot([], [], [], color='magenta', markersize=1)
        self.trajectory2, = self.ax1.plot([], [], [], color='purple', markersize=1)
        self.trajectory3, = self.ax1.plot([], [], [], color='blue', markersize=1)
```

### Modelling

Now I had my plots initialised, I turned my attention to the ```main.py``` file. Within the ```main()``` function, I first defined my constants, and then created input prompts for the other variables. At this point I chose to define a separate array to represent time beacause the animation method I was using required a database of this sort to set the number of frames for the animation. 

```python
def main():
    tf = int(input('How long should the simulation run for (in seconds)? '))
    startx = int(input('Enter an x coordinate in the path of the incoming  photon: '))
    starty = int(input('Enter a y coordinate in the path of the incoming  photon: '))
    startz = int(input('Enter a z coordinate in the path of the incoming  photon: '))
    photon_pre_energy = float(input('Enter the initial energy of the photon in MeV: ' ))
    photon_post_energy = float(input('Enter the energy of the photon after the collision in MeV: '))

    pvelocity = 3 #photon velocity (measured in 10^8m/s)
    rest_energy_e = 0.512 #measured in MeV
    t0 = 0 # initial time
    dt = 1 # time step
    time = np.arange(t0, tf, dt, dtype='float') # time array
```

Over in ```modeller.py```, I first began writing a single function to entirely produce the database used to model the photon pre collision. However, I later realised that part of this function could be reused during the second stage of modelling, where the electron and photon post collision are modelled. I therefore chose to split this first function into a propagation function and a sort of control function in order to make my code more efficient and eliminate duplicate code.

```python
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
```

For modelling pre collision, I wrote the following function to take a set of coordinates found at a point along the path of the incoming photon, create a vector representing its displacement, and pass this to the propagation function. The dataframe created and shortened time array are then returned to the ```main()``` function:

```python
def pre_collision(time, mag, x, y, z):
    t = sp.symbols('t') # symbolic variable for time
    #define xyz positions as functions of time
    displacement_vector = get_components_pre(mag, x, y, z)
    r0x = displacement_vector[0]
    r0y = displacement_vector[1]
    r0z = displacement_vector[2]
    df, time = propagate(time, r0x, r0y, r0z)
    return(df, time)
```
Back in ```main.py```, as the dataframe produced by ```pre_collision()``` starts with position coordinates running from the origin, I needed to reverse this dataframe so when animated, the particle would appear to move towards the origin rather than away, making sure to keep the order of the column representing time intact. The example dataframes below show this change, note the very letfmost column is the index column:

<img width="569" alt="Screenshot 2023-04-11 at 22 47 14" src="https://user-images.githubusercontent.com/79797035/231295335-67b27171-f84b-4333-9cba-01defd8f634e.png">

<img width="631" alt="Screenshot 2023-04-11 at 22 48 18" src="https://user-images.githubusercontent.com/79797035/231295506-ee92b11e-c880-4bdb-a3ba-a90f72ac2abd.png">

For modelling the particles post-collision, I wrote separate functions for the photon and electron. I first had to write functions which would calculate electron and photon recoil angles, as well as electron velocity from the inputted energies using the equations mentioned earlier, and then pass these values into additional functions that would calculate the components of velocity for each particle.

```python
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
```

I realised I would have to write separate functions for however many components of photon velocity were non zero. The calculated components could in turn be passed to the ```propagate()``` function. 

```python
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
```

I first began trying to write a function that would calculate these components with all the incoming components of photon velocity being non-zero, however soon realised it would be far easier and more logical to start with a function that required only one component to be non-zero (ie, photon only moving in one direction). This proved the easiest component function to write, as it employed only basic trigonemtry for mathematical calculations. The below function was initially split into two, one for the elctron, and one for the photon, but once these two were finished I realised I could prevent duplicate code and improve efficiency by merging the two.

```python
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
```
The greatest challenge I faced was writing the next two functions where more than one component of photon velocity was non-zero, and in fact I wrote 9 different versions before I found a mathematical solution that would produce accurate outputs consistently. Most of my efforts went into finding a method using vector projections to calculate the components of the second velocity vector from the first. However, as I had limited understanding of these vector properties, I struggled to make progress. Below is one of these attempted functions:

```python
def velocity_components(acomps, amag, theta, bmag):
    theta = math.radians(theta)
    cosine = math.cos(theta)
    bcomps = [bmag, 0, 0]
    #dotprod = sum([acomps[i]*bcomps[i] for i in range(3)])
    dotprod = amag * bmag * cosine
    projAontoB = [dotprod/bmag**2 * bcomps[i] for i in range(3)]
    bperp = [bcomps[i] - projAontoB[i] for i in range(3)]
    bx, by, bz = bperp
    print(bperp)
    return bx, by, bz
```

I then realised that resolving the incoming velocity vector into a component parallel to an axis would help avoid use of complex vector methods. To do this, I calculated the angle between the incoming vector and x axis, and used this in conjunction with the angle between the incoming and outgoing vectors to find the angle between the outgoing vector and x axis.

```python
def velocitycomponents(acomps, theta, bmag): #worked but not with z
    theta = math.radians((theta))
    ax = acomps[0]
    ay = acomps[1]
    angle_ax = math.atan2(ay, ax)
    angle_bx = angle_ax + theta
    b_x = bmag * math.cos(angle_bx)
    b_y = bmag * math.sin(angle_bx)
    b_z = 0
    return b_x, b_y, b_z
```

However, this function did not always produce a vector with the correct orientation on the plot. Finally, I realised that as the incoming and outgoing vectors would always be in one identical plane, the components of the vectors in this identical plane must be in the same ratio as the magnitudes of the vectors. As I could calculate this ratio of magnitudes, knowing the scalar velocities of the incoming and outgoing particles, I could therefore apply the same scale factor to the components of that plane, as the adjacent component and magnitude of each vector would form two similar triangles. The other component could always be calculated using basic trigonometry.

``` python
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
```
The only major difference between this function and the one calculating vector components where all incoming velocity components were non-zero was that the adjacent component had to be calculated for both vectors before the scale factor, and I therefore had to use the angle between the chosen axis and outgoing vector.

```python
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
    sf = ifirst / isecond #scale factor from adjacent components of each vector
    bz = bmag * math.sin(theta)
    if type == 'e':
        bz *= -1
    bx = ax / sf #scale down component by sf
    by = ay / sf #scale down component by sf
    return bx, by, bz
```

This concluded my work in ```modeller.py```.

### Visualisation

Before creating the animation, I needed to write code to format my databases as required before passing them to the simulation. First, I wrote a function that would ensure the databases modelling the electron's movement post collision and photon's movement post collision were the same length by comparing the length of the two time arrays.

```python
def time_chop(df1, df2, df1t, df2t):
    if len(df1t) > len(df2t):
        time = df2t
        df1.drop(df1[df1['t'] >= df2t[-1]].index, inplace = True)
    else:
        time = df1t
        df2.drop(df2[df2['t'] >= df1t[-1]].index, inplace = True)
    return df1, df2, time
```

Next, I realised that I needed to create 'filler' databases which could be concatenated with the databases containing position data. Concatenation refers to the process of joining two objects end to end. This would lead to passing three databases to my ```Animator``` class, so providing data for three trajectories and three subplots. I wrote the following function to create a 'filler' database for electron movement pre collision, incoming photon movement post collision, and outgoing photon movement pre collision.

```python
def filler_databases(time):
    feature_list = ['t', 'rx', 'ry', 'rz', 'r_mag', 'vx', 'vy', 'vz', 'v_mag']
    df = pd.DataFrame(0, index=np.arange(len(time)), columns=feature_list) #create empty database as long as specified time period
    df['t'] = df.index
    return df
```

To ensure the transition between databases would be seamless once concatenated, which was important for the ```t``` column as this would be the only variable in the filler database that changed, I defined this function to increase the time values of the second database by the last value of the first.

```python
def format_databases(df, dftimefrom):
    df['t'] = df['t'].apply(lambda x: x + dftimefrom.iloc[-1].at['t']) #add the last time value from the previous database to enure no jumps in 't' column
    return df
```

These lines of code in ```main()``` create the required 'filler' databases, format them, and concatenate them with their counterpart databases:

```python
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
```
Finally, an instance of the ```Animator``` class could be created, and the three databases could be passed to it. Over in ```visualiser.py```, the last function to be written was the ```visualise()``` function, which would plot the information about each particle at each second on the graphs, and serve as the ```func``` parameter for ```FuncAnimation``` as mentioned earlier. The following function updates the trajectory and subplots for each particle at each second by accessing the corresponding elements from the databases created by the modeller.

```python
    def visualize(self, i):
        # update trajectory of each particle for current time step
        self.trajectory1.set_data(self.simulation_results1['rx'][:i], self.simulation_results1['ry'][:i])
        self.trajectory1.set_3d_properties(self.simulation_results1['rz'][:i])

        self.trajectory2.set_data(self.simulation_results2['rx'][:i], self.simulation_results2['ry'][:i])
        self.trajectory2.set_3d_properties(self.simulation_results2['rz'][:i])

        self.trajectory3.set_data(self.simulation_results3['rx'][:i], self.simulation_results3['ry'][:i])
        self.trajectory3.set_3d_properties(self.simulation_results3['rz'][:i])

        time_stepe = self.simulation_results1['t'][:i]
        time_stepp = self.simulation_results2['t'][:i]

        #ELECTRON
        self.rvte.set_data(time_stepe, self.simulation_results1['r_mag'][:i]) #position vs time
        self.vvte.set_data(time_stepe, self.simulation_results1['v_mag'][:i]) # magnitude of velocity vs time

        #PHOTON 1
        self.rvtp1.set_data(time_stepp, self.simulation_results2['r_mag'][:i]) #position vs time
        self.vvtp1.set_data(time_stepp, self.simulation_results2['v_mag'][:i]) #position vs time

        #PHOTON 2
        self.rvtp2.set_data(time_stepp, self.simulation_results3['r_mag'][:i]) # magnitude of velocity vs time
        self.vvtp2.set_data(time_stepp, self.simulation_results3['v_mag'][:i]) # magnitude of velocity vs time
```

Back in ```main.py```, I called the ```.animate()``` method and outputted the plots. 

```python
    #create and run animation, show plots
    animator = Animator(simulation_results1=electron, simulation_results2=incomingphoton, simulation_results3=outgoingphoton)
    anim = animator.animate(timearray, electron_angle, photon_angle)
    plt.show()
```

The flowchart below shows the entire program flow of the project:

<img width="1097" alt="Screenshot 2023-04-14 at 15 05 14" src="https://user-images.githubusercontent.com/79797035/232069943-556100f6-b308-4a20-86eb-b03738228736.png">
<img width="785" alt="Screenshot 2023-04-14 at 15 05 35" src="https://user-images.githubusercontent.com/79797035/232069960-b6f83e2a-3a60-4735-bb2f-2f4aefb41222.png">

### Testing and Feedback
#### Accuracy
At this point my code was fully functional, but I needed a way to check the accuracy of both my modelling and visualisation functions. In ```modeller.py```, I wrote the following function to compare the values of particle velocity computed using **Eqn 4** with the magnitude of the vectors outputted on the graph.

```python
def calcmag(expected, comp1, comp2, comp3, name):
    actual = math.sqrt(comp1**2 + comp2**2 + comp3**2)
    print('expected magnitude of {} is {}'.format(name, round(expected, 3)))
    print('actual magnitude of {} is {}\n'.format(name, round(actual, 3)))
```

In ```main.py```, I wrote a function using vector doct product to calculate the actual angle between the incoming photon and each outgoing particle, and then compare these angles to those calculated in ```electron_recoil_angle()``` and ```photon_recoil_angle()```.

```python
def angle_checker(postcomps, precomps, expected, name):
    dot_prod = postcomps[0]*precomps[0] + postcomps[1]*precomps[1] + postcomps[2]*precomps[2]
    magpre = vector_magnitude(precomps)
    magpost = vector_magnitude(postcomps)
    cosine = dot_prod / (magpre * magpost) 
    theta = math.acos(cosine)
    theta = math.degrees(theta)
    print('expected angle between {} and incoming photon is {} degrees'.format(name, round(expected, 3)))
    print('actual angle between {} and incoming photon is {} degrees\n'.format(name, round(theta, 3)))  
```

#### Usefulness

To test the extent to which my program aided in a teaching scenario, I arranged to lead a physics enrichment session at school where I taught Year 12 students about the Compton scattering effect using my program. I then got feedback using a survey I distributed at the end of the session, the results of which were the following:

put in implemented feedback within code

## V. Skill Development

### Theoretical and Scientific

The theoretical side of my artefact proved the most challenging to understand, as it forced me to learn physics ideas and equations that ordinarily wouldn’t be encountered until undergraduate study.  Furthermore, with the programming element of my project, it was necessary to not only be familiar with these difficult concepts, but understand them to a level high enough to recreate them within the constraints of a programming language.


### Mathematical

However, it was the mathematical element of the project which created the most setbacks, as I would be forced to wait to meet a further mechanics teacher to go through the required calculations if I was faced with a problem, and simply would not be able to progress with a feature of my simulation until I learned the necessary maths behind it. 

### Computational

I generally found the programming side of the project to be the easiest and most rewarding. As working in any programming language encourages creativity and original thinking when devising solutions to problems, I found it enjoyable to work through any challenges I faced, and never encountered any significant setbacks as the modular nature of my program allowed me to simply switch to working on a different part of my code while I tried to resolve a problem created by another.

By far, the most challenging part of the programming element of the project was understanding and implementing object orientated programming techniques. I had limited experience with using classes, and had never used an ‘__init__’ function or the ‘self’  parameter prior to beginning this project. In fact, initially I tried to use an approach that would allow me to write the visualisation code without using a class, but found that this would not allow me to add the complexity to the associated data structures that I needed. Learning how to use  ‘__init__’ did not prove too challenging, and I found that reading the related Python documentation was sufficient for understanding its place in my code. However, it took me longer to understand the purpose of ‘self’, setting me back as I had to spend more time researching the technique in order to gain a deep enough understanding of it for use in my program. 

Another completely new skill I had to learn was the use of the sympy library, which is used to create variables that can be used in algebraic functions. I first read the accompanying article to the code I analysed at the beginning of my project to understand its use, and then began drafting a solution for this part of the program without using this library. However, I then realised I would not be able to derive an equation for velocity from the equation for position any where near as efficiently as with the use of this library, so decided to use sympy after all. 

[^1]: Brittanica, The Editors of Encyclopaedia (2022). Electron volt | unit of measurement. [online] Encyclopedia Britannica. Available at: https://www.britannica.com/science/electron-volt [Accessed 14 Apr. 2023].
‌
[^2]: D’Alessandris, P. (2017). 4.2: Compton Scattering. [online] Physics LibreTexts. Available at: https://phys.libretexts.org/Bookshelves/Modern_Physics/Book%3A_Spiral_Modern_Physics_(D%27Alessandris)/4%3A_The_Photon/4.2%3A_Compton_Scattering [Accessed 26 Mar. 2023].

[^3]: Parker, N. (2020). Massive Meets Massless: Compton Scattering Revisited | Physics Forums. [online] Physics Forums Insights. Available at: https://www.physicsforums.com/insights/massive-meets-massless-compton-scattering-revisited/ [Accessed 26 Mar. 2023].

[^4]: Physics LibreTexts. (2020). 27.3: Relativistic Quantities. [online] Available at: https://phys.libretexts.org/Bookshelves/University_Physics/Book%3A_Physics_(Boundless)/27%3A__Special_Relativity/27.3%3A_Relativistic_Quantities [Accessed 12 Apr. 2023].

[^5]: Davies, A. (2022). kinematics_visualisaion.py (Commit 18da47a)[Source code]. Available at: https://github.com/ad-1/3DKinematicsVisualisation/blob/master/kinematics_visualisaion.py

[^6]: The Matplotlib development team (n.d.). Animations using Matplotlib — Matplotlib 3.7.1 documentation. [online] matplotlib.org. Available at: https://matplotlib.org/stable/tutorials/introductory/animation_tutorial.html [Accessed 25 Apr. 2023].

[^7]: The Matplotlib development team (n.d.). Artist tutorial — Matplotlib 3.7.1 documentation. [online] matplotlib.org. Available at: https://matplotlib.org/stable/tutorials/intermediate/artists.html [Accessed 25 Apr. 2023].


‌

‌
‌
