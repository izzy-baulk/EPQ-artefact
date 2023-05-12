# A Python program to simulate and visualise the Compton scattering effect

## Table of Contents
### I. Overview
### II. Background
### III. Methodology
### IV. Skill Development
### V. Glossary

## I. Overview

I chose to write a Python program to give me an opportunity to develop my skills in object-orientated program, alongside showcasing my existing procedural programming abilities. As I hope to study physics or engineering at university, I decided that modelling a particle physics phenomenon would deepen my knowledge in this field, and provide an opportunity for me to draw links between studies in this area to future studies in science and technology. I made the choice to visualise this model in a 3D plot to further my understanding of the importance of graphical interfaces in research presentation. 

## II. Background

### Compton Scattering

The Compton scattering effect describes the interaction that takes place between a photon of energy between 30keV-30MeV, and a free, stationary electron, where eV is energy measured in [electronvolts](#electronvolt).When these particles collide, the photon imparts some momentum to the electron, causing a change in direction and wavelength of the photon, and a change in the velocity of the electron. The illustration below shows this process, with *λ* representing the incoming photon, *λ’* representing the photon after the collision, *θ* representing photon scattering angle, *Φ* representing electron scattering angle, and *e-* representing the scattered electron[^1]

<img width="278" alt="image" src="https://user-images.githubusercontent.com/79797035/230788567-631402ac-8141-4fac-afb9-6591555b3d1c.png"></img>
###### Fig 1 - illustration of a collision involving compton scattering [^1]

The standard equation for Compton scattering, relating photon wavelength pre and post collision, electron rest energy, and photon scattering angle, was established by Arthur Compton and won him the Nobel Prize in 1927, and is shown below. *h* is the Planck constant, *c* is the speed of light, *m* is electron mass: 

<img width="211" alt="Screenshot 2023-04-20 at 09 38 51" src="https://user-images.githubusercontent.com/79797035/233309865-8a2b25cd-1e07-4d70-9d08-bf58d6ccff7f.png"></img>
###### Eqn 1 - equation for compton effect using photon wavelengths[^1]

Using the relationship *λ = hc/E*, this equation can be rearranged to give:

<img width="278" alt="image" src="https://user-images.githubusercontent.com/79797035/230788650-39f581dd-9a25-4b5d-a908-34eaa4a7b1bc.png"></img>
###### Eqn 2 - equation for compton effect using photon energies[^2]

Using E<sub>o</sub> = m<sub>e</sub>c<sup>2</sup>, where E<sub>o</sub> represents the rest energy of an electron, this equation can be rearranged to give:

<img width="278" alt="image" src="https://user-images.githubusercontent.com/79797035/230788799-60cd5759-049a-4616-96c5-0ce35c455c70.png"></img>
###### Eqn 3 -  equation for compton effect using electron rest energy[^2]

### Python and Additional Libraries

Python is a high-level, general purpose programming language with support for countless graphical, scientific, and mathematical additional [libraries](#library), making it the ideal language for this simulation. I chose matplotlib to be my graphics library, and numpy and pandas to handle database creation and manipulation, as these are libraries built with the intention to be used in conjunction with one another, and libraries that I had previously used in other projects. Python has support for both [object-orientated programming (OOP)](#oop) and [procedural programming (PP)](#pp), which was important as both types of programming had to be utilised in my project, with OOP being vital to creating the animation behind the visualisation part of the program, and PP forming the basis of the modelling side of the code.

### Relativity and Scale

If using the standard equatiion for velocity from kinetic energy, 

<img width="143" alt="Screenshot 2023-04-12 at 11 17 29" src="https://user-images.githubusercontent.com/79797035/231428681-1e629c7d-e989-4fc9-8b1a-d38866267347.png">

a problem arises when calculating electron velocities at high energy levels. Because the mass of an electron is so small, 9.1x10<sup>-31</sup>kg, using this formula can lead to velocities above the speed of light being calculated, which must be disregarded as no object with mass can travel faster than the speed of light[^3]. This error arises because this formula applies to classical mechanics, where it is assumed that absolute time and space exist outside of any observer, and so the speed of light can vary from one reference frame to another. Relativistic mechanics instead states that the speed of light is constant in all reference frames. This becomes significant as the speed of an object passes over half the speed of light, as special relativity states that an object's relativistic kinetic energy will increase to infinity, even as its Newtonian kinetic energy continues to increase at a steady rate.

<img width="488" alt="Screenshot 2023-04-12 at 15 24 49" src="https://user-images.githubusercontent.com/79797035/231488369-423e50dc-360c-4e82-a2af-9d9a91516f57.png"></img>
###### Fig 2 - graph showing how kinetic energy changes with speed[^3]

Therefore, the relativistic equation for velocity must be used, which can be found from rearranging the relativistic equation for kinetic energy.

<img width="189" alt="Screenshot 2023-04-12 at 15 27 48" src="https://user-images.githubusercontent.com/79797035/231489343-d9157da8-030d-4b28-8d6c-6defe5f78042.png"></img>

<img width="232" alt="Screenshot 2023-04-12 at 11 07 18" src="https://user-images.githubusercontent.com/79797035/231426341-831696bf-4e6d-4220-af0f-9fc6d0f564a0.png"></img>

###### Eqn 4 - relativistic equation for velocity [^3]

While using this equation ensures the correct electron velocity can be calculated, when working with energies in the range of MeV, the velocities calculated will still be a large fraction of the speed of light. As computers cannot run simulations at a frame rate anywhere nearing the speed of light, I chose to instead create my plots with a scale of 1 unit = 10<sup>8</sup>m. The velocities of the particles could therefore be scaled down, allowing their relative magnitudes to remain accurate, but allowing the animation to run at a reasonable frame rate. 

## III. Methodology

### Abstraction and Decomposition

After finishing my research into Compton scattering, and confirming this phenomenon could be suitably visualised on a 3D plot, I used the processes of [abstraction](#abstraction) and [decomposition](#decomposition) to plan my program before beginning work on the code. Abstraction first led me to decide on the following input [variables](#variable), output variables, intermediate variables, and [constants](#constant) for my code.

**INPUTS** - photon energy pre-collision (*E<sub>i</sub>*), photon energy post-collision (*E<sub>r</sub>*)

**INTERMEDIATES** - electron energy post collision (*E<sub>k</sub>*)

**OUTPUTS**- electron recoil angle (*Φ*), photon recoil angle (*θ*), electron velocity post-collision (*V*)

**CONSTANTS** - velocity of photon (*c*), electron rest energy (*E<sub>0</sub>*), electron mass (*m*)

I decided to use these specific variables as they allowed me to use equations within my code that had already been proved and verified by other physicists, reducing chances of error in my program as I did not need to do any complex algebraic manipulation. However, to make sure I understood where these equations were coming from, I wrote my own proofs separately and checked these against the known ones. I was also able to better test my code, as I could find examples of calculations using these equations, the outputs of which I could check against the outputs of the calculations carried out within my program. The equations I ended up using were as follows:

<img width="278" alt="image" src="https://user-images.githubusercontent.com/79797035/230789096-d4bf6c2e-861d-46e5-b7db-c5dbaab77439.png"></img>
###### Eqn 5 - equation for electron recoil angle[^2]

<img width="127" alt="Screenshot 2023-04-10 at 15 18 22" src="https://user-images.githubusercontent.com/79797035/230919467-3e48056b-7941-4157-85dd-55ed9369bf3a.png"></img>
###### Eqn 6 - equation for photon recoil angle[^2]

During decomposition, after analysing another piece of code used to create 3D animations using matplotlib, I decided to base the part of my program that would deal with visualisation off of this code, creating a [class](#class) to contain my animation and plotting objects, and data frames to store data generated by my model[^5]. This allowed me to avoid unnecessarily writing new code to carry out the same tasks, and let me spend more time on writing the rest of the program, which had to be written from scratch. I also made the choice to use some utility functions used in vector calculations and manipulation defined within this program within my own code, and copied these into a separate file from which they could be called as necessary. Doing this allowed me to save time during the early stages of the programming process, and keep track of which functions were my own work, and which had been written by others.

Instead of using one file to hold my entire project, I chose to split my project into three separate Python files, one to contain the visualisation code, one to contain the modelling code, and one to act a control program to run the two and pass information between them. This led me to the creation of the following flowchart to plan my project:

![image](https://user-images.githubusercontent.com/79797035/230920731-48912f20-61ed-485c-b46d-25d0ec687bba.png)


### Initialisation

The first step I took was to create the plots in which the data generated by my model would be outputted. I decided to work with a three-dimensional plot to make my model different to others that I researched before beginning this project, which work in two dimensions. I also here made the decision to use the ```FuncAnimation``` subclass of matplotlib to create the actual animation. This function creates an animation by creating outputted data for the first frame, and modifying this subsequently using a [function](#function) that is called every frame, making it the most straightforward animation function to use. Its alternative, ```ArtistAnimation```, is used when data is stored on different Artists[^5], with Artists being objects that can use renderers to directly draw onto a figure[^6]. In hindsight, if I had the time, I would have created a version of my visualiser function using ```ArtistAnimation``` as well, and compared the two on memory efficiency, time efficiency, and suitability. 

Working in the [lab frame](#lab-frame)[^7], in ```visualiser.py```, I defined  an ```Animator``` class and created the main figure and subplots. Here, I initilialised three trajectory objects, with a corresponding subplot each, with one instance representing the photon pre collision, one representing the photon post, and one representing the elcctron. I decided that the only variables I needed to track on each subplot were position and velocity, as acceleration would be constant throughout. I wrote this code under the ‘init’ function so that it would run automatically as soon as the ```Animator``` class is called by the control file, without the function having to be called by name. *(see visualiser.py lines 5-130)*


### Modelling

Now I had my plots initialised, I turned my attention to the ```main.py``` file. Within the ```main()``` function, I first defined my constants, and then created input prompts for the other variables *(see main.py lines 50-73)*. At this point I chose to define a separate array to represent time beacause the animation method I was using required a database of this sort to set the number of frames for the animation.

Over in ```modeller.py```, I first began writing a single function to entirely produce the database used to model the photon pre collision. However, I later realised that part of this function could be reused during the second stage of modelling, where the electron and photon post collision are modelled. I therefore chose to split this first function into a propagation function (```propagate()```), and 'control' functions (```pre_collision()```, ```post_collision_photon```, and ```post_collision_electron``` in order to make my code more efficient and eliminate duplicate code. *(see modeller.py lines 32-57, 154-191)*

When it came to modelling photon motion up to the point of collision, my first approach was to use algebra to solve vector equations to find the end position of the displacement vector given its components of velocity in each dimension. However, this proved mathematically challenging and impractical, as it seemed more logical to ask a user to input a point in the photon's path than its velocity components. So, I instead decided to write data showing the photon moving away from the origin towards a specified point as time progressed, and then in ```main.py```, reverse this dataframe so when animated, the particle would appear to move towards the origin rather than away, making sure to keep the order of the column representing time intact.

```python
    p1, timepre = pre_collision(time, pvelocity, startx, starty, startz) #create database to model incoming photon
    p1 = p1.reindex(index=p1.index[::-1]) #reverse photon database so photon approaches origin instead
    p1["t"] = p1["t"].values[::-1] #but dont reverse time column
```
The final version of the photon-modelling database would therefore have the same layout as the following:

<img width="631" alt="Screenshot 2023-04-11 at 22 48 18" src="https://user-images.githubusercontent.com/79797035/231295506-ee92b11e-c880-4bdb-a3ba-a90f72ac2abd.png">

For modelling the particles post-collision, I first had to write functions which would calculate electron and photon recoil angles, as well as electron velocity from the inputted energies using the equations mentioned earlier, and then pass these values into additional functions that would calculate the components of velocity for each particle. *(see modeller.py lines 59-82)*

I then began trying to write a function that would calculate these components with all the incoming components of photon velocity being non-zero, however soon realised it would be far easier and more logical to start with a function that required only one component to be non-zero (ie, photon only moving in one direction). I also here decided to write separate functions for however many components of photon velocity were non-zero, as mathematically these separate methods would be less complex than one method that could be used in all three scenarios.

This function showing movement in one dimension proved easiest to write, as it employed only basic trigonemtry for mathematical calculations[^8]. I initially wrote two separate versions of function, one for the electron and one for the photon, but once these two were finished I realised I could prevent duplicate code and improve efficiency by merging the two and using [selection statements](#selection).

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
The greatest challenge I faced was writing the next two functions where more than one component of photon velocity was non-zero, and in fact I wrote 9 different versions before I found a mathematical solution that would produce accurate outputs consistently. Most of my efforts went into finding a method using vector projections to calculate the components of the second velocity vector from the first[^9]. However, as I had limited understanding of these vector properties, I struggled to make progress. Below is one of these attempted functions:

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

I then realised that resolving the incoming velocity vector into a component horizontal parallel to an axis would help avoid use of complex vector methods. To do this, I calculated the angle between the incoming vector and x axis, and used this in conjunction with the angle between the incoming and outgoing vectors to find the angle between the outgoing vector and x axis.

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

However, this function did not always produce a vector with the correct orientation on the plot. Finally, I realised that as the incoming and outgoing vectors would always be in one identical plane, the components of the vectors in this identical plane must be in the same ratio as the magnitudes of the vectors. As I could calculate this ratio of magnitudes, knowing the scalar velocities of the incoming and outgoing particles, I could therefore apply the same scale factor to the two parallel components in that plane, as the adjacent component and magnitude of each vector would form two similar triangles. The other, perpendicular component could be operated on independently, and could be calculated using basic trigonometry.

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

Next, I realised that I needed to create 'filler' databases which could be merged with the databases containing position data. This would lead to passing three databases to my ```Animator``` class, so providing data for three trajectories and three subplots. I wrote the following function to create a 'filler' database for electron movement pre collision, incoming photon movement post collision, and outgoing photon movement pre collision.

```python
def filler_databases(time):
    feature_list = ['t', 'rx', 'ry', 'rz', 'r_mag', 'vx', 'vy', 'vz', 'v_mag']
    df = pd.DataFrame(0, index=np.arange(len(time)), columns=feature_list) #create empty database as long as specified time period
    df['t'] = df.index
    return df
```

To ensure the transition between databases would be seamless once merged, which was important for the ```t``` column as this would be the only variable in the filler database that changed, I increased the time values of the second database by the last value of the first.

```python
def format_databases(df, dftimefrom):
    df['t'] = df['t'].apply(lambda x: x + dftimefrom.iloc[-1].at['t']) #add the last time value from the previous database to enure no jumps in 't' column
    return df
```

Finally, an instance of the ```Animator``` class could be created, and the three databases could be passed to it. Over in ```visualiser.py```, the last function to be written was the ```visualise()``` function, which would plot the information about each particle at each second on the graphs, and serve as the ```func``` parameter for ```FuncAnimation``` as mentioned earlier. The following function updates the trajectory and subplots for each particle at each second by accessing the corresponding elements from the databases created by the modeller. *(see visualiser.py lines 146-170)*

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

![unknown](https://user-images.githubusercontent.com/79797035/236675232-942246c8-2fd8-401e-9252-d4aac6308f3c.png)

After this session I also recieved student feedback on user-percieved benefits and limitations of the code. Benefits included the use of color in the simulation and the use of three dimensions. Limitations included the following:
- Clarity of axis labels - in response, I added distance scales to the main plot
- Size of subplots - unfortunately, I was unable to change this, as matplotlib's GridSpec auto-adjusts the size of plots to enure they are all cleanly formatted within a window
- Efficiency - if more time was available to me, I would attempt to use multiprocessing to execute the initialisation and modelling functions at the same time (ie, build the plots while the dataframes were being created). However, this would force me to restructure my initialisation functions so that the databases were not required by the ```__init___``` function, and were rather needed by the animator's configuration function instead. This would allow the two processes to run independently, side by side.
- No information on wavelengths shown - I experimented with using ```np.sin()``` to generate sine waves with peak spacing that showed photon wavelengths, but found that the differences in photon wavelengths pre and post collision were so small that it was very difficult to distinguish any change. It was also impossible to reconcile the distance scale of the main plot (1 unit = 10^8m) with the necessary distance scale for showing particle wavelengths (1 unit = 10^-10m), and if any more subplots were added to the window, they would be very small and the window would appear cluttered.

#### Ease of Use

Feedback from a computer science teacher reccomended that I added a validation process while getting user inputs, so I chose to use a series of while loops to ensure inputted data was within the valid range for each variable.

The only other reccomendation I recieved from this teacher was improving the ease of distribution of my code. I so decided to create an [executable file](#executable) that would contain all the [dependencies](#dependency) for my project, as well as the four program files. This meant that whenever I shared my code with others, they would not need to spend time downloading all the necessary libraries onto their machine. The other change I made was ensuring all the [paths](#path) I used within my code were relative, so that a user would not need the same file structure as me to run the code. I chose to use the 'auto-py-to-exe' library to create this file, as it provides users with a [Graphical User Interface](#gui) (GUI) while creating the file, whereas the library it is built on, PyInstaller use the [command line](#commandline) to achieve the same aim. As I had more than 10 dependencies to include within the final executable file, the prompts I would need to write using the command line would be very long, and so prone to errors. I did encounter a significant challenge here in that because I was writing and [compiling](#compile) my code on a computer with a UNIX based [operating system](#os), I could only compile a file that could be executed on other UNIX systems, and so not Windows machines. The only solution to this issue was to transfer my [source code](#source-code) to a Windows machine at school and compile an executable file from there. This eventually meant I could hand in two versions of my program, one for each major operating system, meaning the vast majority of users would be able to use my program. 

I also decided at this point to create a custom GUI using the ```tkinter``` library where a user could input the necessary data for the simulation to work, and choose whether to save the animation generated. This meant that a user would not need to enter input via the command line as previous, which can appear difficult to use to someone with no programming experience. I also moved the validation code for each input to within the functions that handles creating the form and processing the data from it. As ```tkinter``` was a library I had no previous experience in using, the learning curve was steep, and so I decided on a simple form layout[^10].


## IV. Skill Development

### Theoretical and Scientific

The theoretical side of my artefact proved the most challenging to understand, as it forced me to learn physics ideas and equations that ordinarily wouldn’t be encountered until undergraduate study.  Furthermore, with the programming element of my project, it was necessary to not only be familiar with these difficult concepts, but be proficient enough to recreate them within the constraints of a programming language. I had to ensure that I was considering any and all factors that might affect the accuracy of my simulation, for example, relativity concerns a different branch of physics to the one which my project was most explicitly linked to, but still needed consideration in my program. 

### Mathematical

However, it was the mathematical element of the project which created the most setbacks, as when working on a mathematical problem, progress with that part of the code would be completely halted until I found a solution. For example, during the several weeks I was trying to find a method for calculating vector components of a photon travelling in two dimensions, I could not continue writing the modelling code. To remain productive, I instead began work on my essay, and created the necessary subplots and database formatting functions. 

### Computational

I generally found the programming side of the project to be the easiest and most rewarding. As working in any programming language encourages creativity and original thinking when devising solutions to problems, I found it enjoyable to work through any challenges I faced, and never encountered any significant setbacks as the modular nature of my program allowed me to simply switch to working on a different part of my code while I tried to resolve a problem created by another.

By far, the most challenging part of the programming element of the project was understanding and implementing object orientated programming techniques. I had limited experience with using classes, and had never used an ‘__init__’ function or the ‘self’  parameter prior to beginning this project. In fact, initially I tried to use an approach that would allow me to write the visualisation code without using a class, but found that this would not allow me to add the complexity to the associated data structures that I needed. Learning how to use  ‘__init__’ did not prove too challenging, and I found that reading the related Python documentation was sufficient for understanding its place in my code. However, it took me longer to understand the purpose of ‘self’, setting me back as I had to spend more time researching the technique in order to gain a deep enough understanding of it for use in my program. 

Another completely new skill I had to learn was the use of the ```sympy``` library, which is used to create variables that can be used in algebraic functions. I first read the accompanying article to the code I analysed at the beginning of my project to understand its use, and then began drafting a solution for this part of the program without using this library. However, I then realised I would not be able to derive an equation for velocity from the equation for position any where near as efficiently as with the use of this library, so decided to use sympy after all. ```tkinter``` was another new library I had to learn to use in order to create a standalone GUI for entering data to use in the simulation. This meant that a user would not need to enter input via the command line as previous, which can appear difficult to use to someone with no programming experience. I decided on a simple form layout[^10], and used the library's [documentation](#docs) to further my knowledge.



## Glossary

<a name="abstraction">**Abstraction.**</a> The separation of unnecessary details from the information and tasks required to solve a problem.

<a name="class">**Class.**</a> Used to construct objects in a program.

<a name='constant'>**Constant.**</a> A variable whose value cannnot be changed.

<a name='command line'>**Command line.**</a> A means of interacting with a computer via successive lines of text.**</a>

<a name='compile'>**Compile.**</a> Translate computer code written in one language to another, typically a high level one to machine executable code.

<a name='docs'>**Documentation.**</a> The information that describes a piece of software to users, distributed by the developers.

<a name="decomposition">**Decomposition.**</a> The process of breaking down a problem into smaller, more simple tasks, for each an individual coded solution can be found.

<a name="dependency">**Dependency.**</a> A relationship between files where one relies on the other to run.

<a name="electronvolt">**Electronvolt.**</a> The energy gained by an electron when accelerated through a potential difference of 1 volt.

<a name="executable">**Executable.**</a> A file that contains an encoded sequence of instructions that the computer can execute immediately as the file is opened.

<a name="function">**Function.**</a> A block of code that only runs once called.

<<a name="gui">**Graphical User Interface.**</a> A form of user interface that uses graphical icons.

<a name="lab-frame">**Lab frame.**</a> A frame of reference centered on where an experiment occurs in space.

<a name="library">**Library.**</a> A collection of reusable chunks of code written to carry out a specific set of tasks.

<a name="object">**Object.**</a> A collection of data, and the operations that can be performed on this data.

<a name="oop">**Object-orientated programming.**</a> A type of programming based on the concept of objects

<a name="os">**Operating system.**</a> The program that manages all other applications and processes on a computer, including hardware.

<a name="path">**Path.**</a> A string of characters used to uniquely identify a location in a file structure

<a name="pp">**Procedural programming.**</a> A type of programming where instructions are created and executed in a specific order to carry out a series of operations on a set of objects.

<a name='selection'>**Selection.**</a> A statement that tests one or more conditions and executes instructions based on which are true.

<a name='source-code'>**Source code.**</a> Programming statements written in a human-readable way, formatted to be easily understood by other programmers.

<a name='variable'>**Variable.**</a> A name used to reference an object.

‌
[^1]: D’Alessandris, P. (2017). 4.2: Compton Scattering. [online] Physics LibreTexts. Available at: https://phys.libretexts.org/Bookshelves/Modern_Physics/Book%3A_Spiral_Modern_Physics_(D%27Alessandris)/4%3A_The_Photon/4.2%3A_Compton_Scattering [Accessed 26 Mar. 2023].

[^2]: Parker, N. (2020). Massive Meets Massless: Compton Scattering Revisited | Physics Forums. [online] Physics Forums Insights. Available at: https://www.physicsforums.com/insights/massive-meets-massless-compton-scattering-revisited/ [Accessed 26 Mar. 2023].

[^3]: Physics LibreTexts. (2020). 27.3: Relativistic Quantities. [online] Available at: https://phys.libretexts.org/Bookshelves/University_Physics/Book%3A_Physics_(Boundless)/27%3A__Special_Relativity/27.3%3A_Relativistic_Quantities [Accessed 12 Apr. 2023].

[^4]: Davies, A. (2022). kinematics_visualisaion.py (Commit 18da47a)[Source code]. Available at: https://github.com/ad-1/3DKinematicsVisualisation/blob/master/kinematics_visualisaion.py

[^5]: The Matplotlib development team (n.d.). Animations using Matplotlib — Matplotlib 3.7.1 documentation. [online] matplotlib.org. Available at: https://matplotlib.org/stable/tutorials/introductory/animation_tutorial.html [Accessed 25 Apr. 2023].

[^6]: The Matplotlib development team (n.d.). Artist tutorial — Matplotlib 3.7.1 documentation. [online] matplotlib.org. Available at: https://matplotlib.org/stable/tutorials/intermediate/artists.html [Accessed 25 Apr. 2023].

[^7]: Fitzpatrick, R. (2011). Scattering in the Laboratory Frame. [online] farside.ph.utexas.edu. Available at: https://farside.ph.utexas.edu/teaching/336k/Newton/node52.html [Accessed 9 May 2023].

[^8]: L Bostock and S Chandler (1994). Core maths for A-level. Cheltenham: Thornes, pp.68–71, 450–463.

‌[^9]: Department of Mathematics, Oregon State University (1996). Dot Products and Projections. [online] sites.science.oregonstate.edu. Available at: https://sites.science.oregonstate.edu/math/home/programs/undergrad/CalculusQuestStudyGuides/vcalc/dotprod/dotprod.html [Accessed 9 May 2023].

‌[^10]: Amos, D. (2022). Python GUI Programming With Tkinter – Real Python. [online] realpython.com. Available at: https://realpython.com/python-gui-tkinter/ [Accessed 9 May 2023].

‌
‌

‌
‌
