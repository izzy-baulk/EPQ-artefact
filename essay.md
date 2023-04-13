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

The Compton scattering effect describes the interaction that takes place between a photon of energy between 30keV-30MeV, and a free, stationary electron, where eV is energy measured in electronvolts. One electron volt is the energy gained by an electron when accelerated through a potential difference of 1 volt. When these particles collide, the photon imparts some momentum to the electron, causing a change in direction and wavelength of the photon, and a change in the velocity of the electron. The illustration below shows this process, with *λ* representing the incoming photon, *λ’* representing the photon after the collision, *θ* representing photon scattering angle, *Φ* representing electron scattering angle, and *e-* representing the scattered electron[^1]

<img width="278" alt="image" src="https://user-images.githubusercontent.com/79797035/230788567-631402ac-8141-4fac-afb9-6591555b3d1c.png"></img>
###### Fig 1 - illustration of a collision involving compton scattering [^1]

The standard equation for Compton scattering, relating photon wavelength pre and post collision, electron rest energy, and photon scattering angle, was established by Arthur Compton and won him the Nobel Prize in 1927, and is shown below: 

<img width="278" alt="image" src="https://user-images.githubusercontent.com/79797035/230788650-39f581dd-9a25-4b5d-a908-34eaa4a7b1bc.png"></img>
###### Eqn 1 - equation for compton effect using photon energies[^2]

Using E<sub>o</sub> = m<sub>e</sub>c<sup>2</sup>, where E<sub>o</sub> represents the rest energy of an electron, this equation can be rearranged to give:

<img width="278" alt="image" src="https://user-images.githubusercontent.com/79797035/230788799-60cd5759-049a-4616-96c5-0ce35c455c70.png"></img>
###### Eqn 2 -  equation for compton effect using electron rest energy[^2]

### Python and Additional Libraries

Python is a high-level, general purpose programming language with support for countless graphical, scientific, and mathematical additional libraries, making it the ideal language for this simulation. A library is a collection of reusable chunks of code written to carry out a specific set of tasks, and distributed freely online. For example, graphics libraries contain code that can create 2D and 3D plots of data, and database libraries contain code that can create more complex and powerful databases than the Python programming language alone. I chose matplotlib to be my graphics library, and numpy and pandas to handle database creation and manipulation, as these are libraries built with the intention to be used in conjunction with one another, and libraries that I had previously used in other projects. Python has support for object-orientated programming (OOP), which is a type of programming based on the concept of ‘objects’, or standalone chunks of information used to describe specific items and events. Python also has support for procedural programming (PP), where instructions are created and executed in a specific order to carry out a series of operations on these objects. Both types of programming had to be utilised in my project, with OOP being vital to creating the animation behind the visualisation part of the program, and PP forming the basis of the modelling side of the code.

### Relativity and Scale

If using the standard equatiion for velocity from kinetic energy, 

<img width="143" alt="Screenshot 2023-04-12 at 11 17 29" src="https://user-images.githubusercontent.com/79797035/231428681-1e629c7d-e989-4fc9-8b1a-d38866267347.png">

a problem arises when calculating electron velocities at high energy levels. Because the mass of an electron is so small, 9.1x10<sup>-31</sup>kg, using this formula can lead to velocities above the speed of light being calculated, which must be disregarded as no object with mass can travel faster than the speed of light. This error arises because this formula applies to Newtonian physics, where it is assumed that absolute time and space exist outside of any observer, and so the speed of light can vary from one reference frame to another. Relativistic physics instead states that the speed of light is constant in all reference frames. This becomes significant as the speed of an object passes over half the speed of light, as special relativity states that an object's relativistic kinetic energy will increase to infinity, even as its Newtonian kinetic energy continues to increase at a steady rate.

<img width="488" alt="Screenshot 2023-04-12 at 15 24 49" src="https://user-images.githubusercontent.com/79797035/231488369-423e50dc-360c-4e82-a2af-9d9a91516f57.png"></img>
###### Fig 2 - graph showing how kinetic energy changes with speed[^3]

Therefore, the relativistic equation for velocity must be used, which can be found from rearranging the relativistic equation for kinetic energy.

<img width="189" alt="Screenshot 2023-04-12 at 15 27 48" src="https://user-images.githubusercontent.com/79797035/231489343-d9157da8-030d-4b28-8d6c-6defe5f78042.png"></img>

###### Eqn 3 - relativistic equation for kinetic energy[^3]

While using this equation ensures the correct electron velocity can be calculated, when working with energies in the range of MeV, the velocities calculated will still be a large fraction of the speed of light. As computers obviously cannot run simulations at a frame rate anywhere nearing the speed of light, I chose to instead create my plots with a scale of 1 unit = 10<sup>8</sup>m. The velocities of the particles could therefore be scaled down, allowing their relative magnitudes to remain accurate, but allowing the animation to run at a reasonable frame rate. 

## IV. Methodology

### Abstraction and Decomposition

After finishing my research into Compton scattering, and confirming this phenomenon could be suitably visualised on a 3D plot, I used the processes of abstraction and decomposition to plan my program before beginning work on the code. Abstraction in programming refers to the separation of unnecessary details from the information and tasks required to solve a problem, while decomposition is the process of breaking down a problem into smaller, more simple tasks, for each an individual coded solution can be found. Abstraction first led me to decide on the following input variables, output variables, intermediate variables, and constants for my code, with variables being values used to store information under specific monikers, through which they can be defined, accessed and updated.

**INPUTS** - photon energy pre-collision (*E<sub>i</sub>*), photon energy post-collision (*E<sub>r</sub>*)

**INTERMEDIATES** - electron energy post collision (*E<sub>k</sub>*)

**OUTPUTS**- electron recoil angle (*Φ*), photon recoil angle (*θ*), electron velocity post-collision (*V*)

**CONSTANTS** - velocity of photon (*c*), electron rest energy (*E<sub>0</sub>*), electron mass (*m*)

I decided to use these specific variables as they allowed me to use equations within my code that had already been proved and verified by other physicists, reducing chances of error in my program as I did not need to do any complex algebraic manipulation. However, to make sure I understood where these equations were coming from, I wrote my own proofs separately and checked these against the known ones. I was also able to better test my code, as I could find examples of calculations using these equations, the outputs of which I could check against the outputs of the calculations carried out within my program. The equations I ended up using were as follows:

<img width="278" alt="image" src="https://user-images.githubusercontent.com/79797035/230789096-d4bf6c2e-861d-46e5-b7db-c5dbaab77439.png"></img>
###### Eqn 4 - equation for electron recoil angle[^2]

<img width="127" alt="Screenshot 2023-04-10 at 15 18 22" src="https://user-images.githubusercontent.com/79797035/230919467-3e48056b-7941-4157-85dd-55ed9369bf3a.png"></img>
###### Eqn 5 - equation for photon recoil angle[^2]

<img width="232" alt="Screenshot 2023-04-12 at 11 07 18" src="https://user-images.githubusercontent.com/79797035/231426341-831696bf-4e6d-4220-af0f-9fc6d0f564a0.png">

###### Eqn 6 - equation for electron velocity (rearrangement of Eqn 3)

During decomposition, after analysing another piece of code used to create 3D animations using matplotlib, I decided to use a similar structure to my program, creating a class to contain my animation and plotting objects, and data frames to store data generated by my model. I also made the choice to use some utility functions used in vector calculations and manipulation defined within this program within my own code, and copied these into a separate file from which they could be called as necessary. Doing this allowed me to save time during the early stages of the programming process, and keep track of which functions were my own work, and which had been written by others. These functions were the following[^4]

```python
def vector_derivative(vector, wrt):
    return [component.diff(wrt) for component in vector] #wrt is symbolic variable from t, returns x y z components

def evaluate_vector(vector, time_step, t):
    numerical_vector = [float(component.subs(t, time_step).evalf()) for component in vector]
    magnitude = vector_magnitude(numerical_vector)
    return numerical_vector, magnitude
  
def get_limits1(self, params, axis):
    lower_lim, upper_lim = 0, 0
    for p in params:
        m = max(self.simulation_results1['%s%s' % (p, axis)])
        if m > upper_lim:
            upper_lim = m
        m = min(self.simulation_results1['%s%s' % (p, axis)])
        if m < lower_lim:
            lower_lim = m
    return lower_lim - 0.05, upper_lim + 0.05
```    
Classes in Python are complex data structures used to create instances of objects, and perform operations on these objects. However instead of using one file to hold my entire project, I chose to split my project into three separate Python files, one to contain the visualisation code, one to contain the modelling code, and one to act a control program to run the two and pass information between them. This led me to the creation of the following flowchart to plan my project:

![image](https://user-images.githubusercontent.com/79797035/230920731-48912f20-61ed-485c-b46d-25d0ec687bba.png)


### Initialisation

The first step I took was to create the plots in which the data generated by my model would be outputted. I decided to work with a three-dimensional plot to make my model different to others that I researched before beginning this project, which work in two dimensions. Working in the ‘lab frame’, where the electron with which the photon collides is centred in the plot in which the animation is created, I defined an ```Animator``` class and wrote functions in ```visualiser.py``` to create the animation plot. ```GridSpec``` is a method used to create a layout to which subplots can be added, here as I knew I would have three subplots alongside the main figure, I created a 3x3 grid.[^5]

```python
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

```

Next, I added the three subplots which would each track the positon and velocity of each particle during the simulation. I used the ```twinx()``` method to make sure each plot displayed both variables.

```python
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

This code also creates an empty object to store the the trajectory of each particle. Writing this code under the ‘init’ function allows this block of code to run automatically as soon as the ```Animator``` class is called by the control file, without the function having to be called by name. The ```set_axes_limits()``` method calls a number of other functions which are run during this automatic initialisation process, which create labels, titles, scales and limits for each axis for each plot, as well as initialing the origin of the graph in the centre of the plot. 

```python
    def set_axes_limits(self):
        #set limits of main plot to (500,500,500) and draw axes accordingly
        x_lims = [-500, 500]
        y_lims = [-500, 500]
        z_lims = [-500, 500]

        self.ax1.set_xlim3d(x_lims[0], x_lims[1])
        self.ax1.set_ylim3d(y_lims[0], y_lims[1])
        self.ax1.set_zlim3d(z_lims[0], z_lims[1])
        self.draw_xyz_axis(x_lims, y_lims, z_lims)
        
        #get limits for subplots from time period of simulation data
        t_lims1 = self.get_limits1(['t'], '')
        t_lims2 = self.get_limits2(['t'], '')
        if t_lims1 > t_lims2:
            t_lims = t_lims1
        else:
            t_lims = t_lims2       

        #do same with r and v to find axis limits
        self.axElectronA.set_xlim(t_lims)
        self.axElectronA.set_ylim(self.get_limits1(['r_mag'], ''))
        self.axElectronA.set_xlabel('t (s)')
        self.axElectronA.set_ylabel('position from origin (10^8m)', color='g')
        self.axElectronB.set_ylim(self.get_limits1(['v_mag'], ''))
        self.axElectronB.set_ylabel('velocity (10^8m/s)', color='r')

        self.axPhoton1A.set_xlim(t_lims)
        self.axPhoton1A.set_ylim(self.get_limits2(['r_mag'], ''))
        self.axPhoton1A.set_xlabel('t (s)')
        self.axPhoton1A.set_ylabel('position from origin (10^8m)', color='g')
        self.axPhoton1B.set_ylim(self.get_limits2(['v_mag'], ''))
        self.axPhoton1B.set_ylabel('velocity (10^8m/s)', color='r')

        self.axPhoton2A.set_xlim(t_lims)
        self.axPhoton2A.set_ylim(self.get_limits2(['r_mag'], ''))
        self.axPhoton2A.set_xlabel('t (s)')
        self.axPhoton2A.set_ylabel('position from origin (10^8m)', color='g')
        self.axPhoton2B.set_ylim(self.get_limits2(['v_mag'], ''))
        self.axPhoton2B.set_ylabel('velocity (10^8m/s)', color='r')
```

```get_limits1()``` and ```get_limits2()``` are functions used to find the maximum and minimum for each column in each dataframe. ```get_limits2()``` can be used for both the dataset following the incoming and outgoing photon, as the minimums and maximums for each column in the two dataframes will be very similiar if not the same.

### Modelling

Now I had my plots initialised, I turned my attention to the ```main.py``` file. Within the ```main()``` function, I first defined my constants, and then created input prompts for the other variables. I also defined an array to represent time, and while creating a whole separate data structure to represent time seemed at this stage unnecessary, the animation method I was using required a database of this sort to set the number of frames for the animation. 

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

Over in ```modeller.py```, I first began writing a single function to entirely produce the database used to model the photon pre collision. However, I later realised that part of this function could be reused during the second stage of modelling, where the electron and photon post collision are modelled. I therefore chose to split this first function into a propagation function and a sort of control function in order to make my code more efficient and eliminate duplicate code. The propagation function takes a length of time and the xyz velocity components of a particle as inputs, and creates an equation representing the change in position of the particle from these values, which is then differentiated to create an equation describing particle velocity. Then, for each second, the current time period is substituted into these equations to find the position and velocity of the particle at that given second in each direction in relation to the origin. 

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

The data frame produced is then cut down to ensure no position values are beyond the limits of the axes, and the database representing the number of seconds the program runs for is similarly cut to ensure it is the same length as the database modelling the particle.

```python
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

For modelling the particles post-collision, I wrote separate functions for the photon and electron. I first had to write functions which would calculate electron and photon recoil angles, as well as electron velocity from the inputted energies using the equations mentioned earlier, and then pass these values into additional functions that would calculate the components of velocity for each particle. I realised I would have to write separate functions for however many components of photon velocity were non zero. The calculated components could in turn be passed to the ```propagate()``` function. 

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
running two animations wasnt possible


Next, I realised that I needed to create 'filler' databases which could be concatenated with the databases containing position data


### Testing

## V. Skill Development

### Theoretical and Scientific

The theoretical side of my artefact proved the most challenging to understand, as it forced me to learn physics ideas and equations that ordinarily wouldn’t be encountered until undergraduate study.  Furthermore, with the programming element of my project, it was necessary to not only be familiar with these difficult concepts, but understand them to a level high enough to recreate them within the constraints of a programming language.


### Mathematical

However, it was the mathematical element of the project which created the most setbacks, as I would be forced to wait to meet a further mechanics teacher to go through the required calculations if I was faced with a problem, and simply would not be able to progress with a feature of my simulation until I learned the necessary maths behind it. 

### Computational

I generally found the programming side of the project to be the easiest and most rewarding. As working in any programming language encourages creativity and original thinking when devising solutions to problems, I found it enjoyable to work through any challenges I faced, and never encountered any significant setbacks as the modular nature of my program allowed me to simply switch to working on a different part of my code while I tried to resolve a problem created by another.

By far, the most challenging part of the programming element of the project was understanding and implementing object orientated programming techniques. I had limited experience with using classes, and had never used an ‘__init__’ function or the ‘self’  parameter prior to beginning this project. In fact, initially I tried to use an approach that would allow me to write the visualisation code without using a class, but found that this would not allow me to add the complexity to the associated data structures that I needed. Learning how to use  ‘__init__’ did not prove too challenging, and I found that reading the related Python documentation was sufficient for understanding its place in my code. However, it took me longer to understand the purpose of ‘self’, setting me back as I had to spend more time researching the technique in order to gain a deep enough understanding of it for use in my program. 

Another completely new skill I had to learn was the use of the sympy library, which is used to create variables that can be used in algebraic functions. I first read the accompanying article to the code I analysed at the beginning of my project to understand its use, and then began drafting a solution for this part of the program without using this library. However, I then realised I would not be able to derive an equation for velocity from the equation for position any where near as efficiently as with the use of this library, so decided to use sympy after all. 

[^1]: D’Alessandris, P. (2017). 4.2: Compton Scattering. [online] Physics LibreTexts. Available at: https://phys.libretexts.org/Bookshelves/Modern_Physics/Book%3A_Spiral_Modern_Physics_(D%27Alessandris)/4%3A_The_Photon/4.2%3A_Compton_Scattering [Accessed 26 Mar. 2023].

[^2]: Parker, N. (2020). Massive Meets Massless: Compton Scattering Revisited | Physics Forums. [online] Physics Forums Insights. Available at: https://www.physicsforums.com/insights/massive-meets-massless-compton-scattering-revisited/ [Accessed 26 Mar. 2023].

[^3]: Physics LibreTexts. (2020). 27.3: Relativistic Quantities. [online] Available at: https://phys.libretexts.org/Bookshelves/University_Physics/Book%3A_Physics_(Boundless)/27%3A__Special_Relativity/27.3%3A_Relativistic_Quantities [Accessed 12 Apr. 2023].

[^4]: Davies, A. (2022). kinematics_visualisaion.py (Commit 18da47a)[Source code]. Available at: https://github.com/ad-1/3DKinematicsVisualisation/blob/master/kinematics_visualisaion.py

[^5]: matplotlib.org. (n.d.). matplotlib.gridspec.GridSpec — Matplotlib 3.7.1 documentation. [online] Available at: https://matplotlib.org/stable/api/_as_gen/matplotlib.gridspec.GridSpec.html [Accessed 13 Apr. 2023].

‌

‌
‌
