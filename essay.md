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

a problem arises when calculating electron velocities at high energy levels. Because the mass of an electron is so small, 9.1x10<sup>-31</sup>kg, using this formula can lead to velocities above the speed of light being calculated, which must be disregarded as no object with mass can travel faster than the speed of light. This error arises because this formula applies to Newtonian physics, where it is assumed that absolute time and space exist outside of any observer, and so the speed of light can vary from one reference frame to another. Relativistic physics instead states that the speed of light is constant in all reference frames. As the speed of an object passes over half the speed of light, special relativity states that an object's relativistic kinetic energy will increase to infinity, even as its Newtonian kinetic energy continues to increase at a steady rate.

## IV. Methodology

### Abstraction and Decomposition

After finishing my research into Compton scattering, and confirming this phenomenon could be suitably visualised on a 3D plot, I used the processes of abstraction and decomposition to plan my program before beginning work on the code. Abstraction in programming refers to the separation of unnecessary details from the information and tasks required to solve a problem, while decomposition is the process of breaking down a problem into smaller, more simple tasks, for each an individual coded solution can be found. Abstraction first led me to decide on the following input variables, output variables, intermediate variables, and constants for my code, with variables being values used to store information under specific monikers, through which they can be defined, accessed and updated.

**INPUTS** - photon energy pre-collision (*E<sub>i</sub>*), photon energy post-collision (*E<sub>r</sub>*)

**INTERMEDIATES** - electron energy post collision (*E<sub>k</sub>*)

**OUTPUTS**- electron recoil angle (*Φ*), photon recoil angle (*θ*), electron velocity post-collision (*V*)

**CONSTANTS** - velocity of photon (*c*), electron rest energy (*E<sub>0</sub>*), electron mass (*m*)

I decided to use these specific variables as they allowed me to use equations within my code that had already been proved and verified by other physicists, reducing chances of error in my program as I did not need to do any complex algebraic manipulation. However, to make sure I understood where these equations were coming from, I wrote my own proofs separately and checked these against the known ones. I was also able to better test my code, as I could find examples of calculations using these equations, the outputs of which I could check against the outputs of the calculations carried out within my program. The equations I ended up using were as follows:

<img width="278" alt="image" src="https://user-images.githubusercontent.com/79797035/230789096-d4bf6c2e-861d-46e5-b7db-c5dbaab77439.png"></img>
###### Eqn 3 - equation for electron recoil angle[^2]

<img width="127" alt="Screenshot 2023-04-10 at 15 18 22" src="https://user-images.githubusercontent.com/79797035/230919467-3e48056b-7941-4157-85dd-55ed9369bf3a.png"></img>
###### Eqn 4 - equation for photon recoil angle[^2]

<img width="232" alt="Screenshot 2023-04-12 at 11 07 18" src="https://user-images.githubusercontent.com/79797035/231426341-831696bf-4e6d-4220-af0f-9fc6d0f564a0.png">

###### Eqn 5 - equation for electron velocity (rearrangement of relativistic expression for KE [^4] )

During decomposition, after analysing another piece of code used to create 3D animations using matplotlib, I decided to use a similar structure to my program, creating a class to contain my animation and plotting objects, and data frames to store data generated by my model. I also made the choice to use some utility functions used in vector calculations and manipulation defined within this program within my own code, and copied these into a separate file from which they could be called as necessary. Doing this allowed me to save time during the early stages of the programming process, and keep track of which functions were my own work, and which had been written by others. These functions were the following[^3]

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

The first step I took was to create the plots in which the data generated by my model would be outputted. I decided to work with a three-dimensional plot to make my model different to others that I researched before beginning this project, which work in two dimensions. Working in the ‘lab frame’, where the electron with which the photon collides is centred in the plot in which the animation is created, I defined an 'Animator' class and wrote functions in 'visualiser.py' to create the animation plot, as well as the subplots where the position and velocity of each particle could be followed throughout the simulation. 

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

This code also creates an empty object to store the the trajectory of each particle. Writing this code under the ‘init’ function allows this block of code to run automatically as soon as the ‘Animator’ class is called by the control file, without the function having to be called by name. The ‘set_axes_limits()’ method calls a number of other functions which are run during this automatic initialisation process, which create labels, titles, scales and limits for each axis for each plot, as well as initialing the origin of the graph in the centre of the plot. 

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

'get_limits1' and 'get_limits2' are functions used to find the maximum and minimum for each column in each dataframe. 'get_limits2' can be used for both the dataset following the incoming and outgoing photon, as the minimums and maximums for each column in the two dataframes will be very similiar if not the same.

### Modelling

Now I had my plots initialised, I turned my attention to the 'main.py' file. Within the 'main()' function, I first defined my constants, and then created input prompts for the other variables. I also defined an array to represent time, and while creating a whole separate data structure to represent time seemed at this stage unnecessary, the animation method I was using required a database of this sort to set the number of frames for the animation. 

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

Over in 'modeller.py', I first began writing a single function to entirely produce the database used to model the photon pre collision. However, I later realised that part of this function could be reused during the second stage of modelling, where the electron and photon post collision are modelled. I therefore chose to split this first function into a propagation function and a sort of control function in order to make my code more efficient and eliminate duplicate code. The propagation function takes a length of time and the xyz velocity components of a particle as inputs, and creates an equation representing the change in position of the particle from these values, which is then differentiated to create an equation describing particle velocity. Then, for each second, the current time period is substituted into these equations to find the position and velocity of the particle at that given second in each direction in relation to the origin. 

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

For modelling pre collision, I wrote the following function to take a set of coordinates found at a point along the path of the incoming photon, create a vector representing its displacement, and pass this to the propagation function. The dataframe created and shortened time array are then returned to the 'main()' function:

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
Back in 'main.py', as the dataframe produced by 'pre_collision()' starts with position coordinates running from the origin, I needed to reverse this dataframe so when animated, the particle would appear to move towards the origin rather than away, making sure to keep the order of the column representing time intact. The example dataframes below show this change, note the very letfmost column is the index column:

<img width="569" alt="Screenshot 2023-04-11 at 22 47 14" src="https://user-images.githubusercontent.com/79797035/231295335-67b27171-f84b-4333-9cba-01defd8f634e.png">

<img width="631" alt="Screenshot 2023-04-11 at 22 48 18" src="https://user-images.githubusercontent.com/79797035/231295506-ee92b11e-c880-4bdb-a3ba-a90f72ac2abd.png">

For the functions handelling modelling post collision, I first had to write functions calculating electron and photon recoil angles, as well as electron velocity from the inputted energies using the equations mentioned earlier.

### Visualisation

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

‌[^3]: Davies, A. (2022). kinematics_visualisaion.py (Commit 18da47a)[Source code]. Available at: https://github.com/ad-1/3DKinematicsVisualisation/blob/master/kinematics_visualisaion.py

[^4]: Physics LibreTexts. (2020). 27.3: Relativistic Quantities. [online] Available at: https://phys.libretexts.org/Bookshelves/University_Physics/Book%3A_Physics_(Boundless)/27%3A__Special_Relativity/27.3%3A_Relativistic_Quantities [Accessed 12 Apr. 2023].

‌
‌
