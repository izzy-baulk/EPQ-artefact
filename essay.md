# A Python program to simulate and visualise the Compton scattering effect

### [I. Abstract](#I.-Abstract)
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

Using Eo = mec2, where Eo represents the rest energy of an electron, this equation can be rearranged to give:

<img width="278" alt="image" src="https://user-images.githubusercontent.com/79797035/230788799-60cd5759-049a-4616-96c5-0ce35c455c70.png"></img>
###### Eqn 2 -  equation for compton effect using electron rest energy[^2]

### Python and Additional Libraries

Python is a high-level, general purpose programming language with support for countless graphical, scientific, and mathematical additional libraries, making it the ideal language for this simulation. A library is a collection of reusable chunks of code written to carry out a specific set of tasks, and distributed freely online. For example, graphics libraries contain code that can create 2D and 3D plots of data, and database libraries contain code that can create more complex and powerful databases than the Python programming language alone. I chose matplotlib to be my graphics library, and numpy and pandas to handle database creation and manipulation, as these are libraries built with the intention to be used in conjunction with one another, and libraries that I had previously used in other projects. Python has support for object-orientated programming (OOP), which is a type of programming based on the concept of ‘objects’, or standalone chunks of information used to describe specific items and events. Python also has support for procedural programming (PP), where instructions are created and executed in a specific order to carry out a series of operations on these objects. Both types of programming had to be utilised in my project, with OOP being vital to creating the animation behind the visualisation part of the program, and PP forming the basis of the modelling side of the code.

## IV. Methodology

### Abstraction and Decomposition

After finishing my research into Compton scattering, and confirming this phenomenon could be suitably visualised on a 3D plot, I used the processes of abstraction and decomposition to plan my program before beginning work on the code. Abstraction in programming refers to the separation of unnecessary details from the information and tasks required to solve a problem, while decomposition is the process of breaking down a problem into smaller, more simple tasks, for each an individual coded solution can be found. Abstraction first led me to decide on the following input variables, output variables, intermediate variables, and constants for my code, with variables being values used to store information under specific monikers, through which they can be defined, accessed and updated.

**INPUTS** - photon energy pre-collision (*E<sub>i</sub>*), photon energy post-collision (*E<sub>r</sub>*)
**INTERMEDIATES** - electron energy post collision (*E<sub>k</sub>*)
**OUTPUTS**- electron recoil angle (*Φ*), photon recoil angle (*θ*), electron velocity post-collision (*V*)
**CONSTANTS** - velocity of photon (*c*), electron rest energy (*E<sub>0</sub>*), electron mass (*m*)

These decisions led me to decide on choosing the below equations to carry out the necessary calculations within my program:

<img width="278" alt="image" src="https://user-images.githubusercontent.com/79797035/230789096-d4bf6c2e-861d-46e5-b7db-c5dbaab77439.png"></img>

###### Eqn 3 - equation for electron recoil angle



### Initialisation

The first step I took was to create the plots in which the data generated by my model would be outputted. I decided to work with a three-dimensional plot to make my model different to others that I researched before beginning this project, which work in two dimensions. Working in the ‘lab frame’, where the electron with which the photon collides is centred in the plot in which the animation is created, I wrote functions in visualiser.py to create the animation plot, as well as two subplots where the position and velocity of each particle could be followed throughout the simulation (LINE NUMBERS). This code also creates an empty object to store the the trajectory of each particle. Writing this code under the ‘__init__’ function allows this block of code to run automatically as soon as the ‘Animator’ class is called by the control file, without the function having to be called by name. The ‘set_axes_limits()’ method calls a number of other functions which are run during this automatic initialisation process, which create labels, titles, scales and limits for each axis for each plot, as well as initialing the origin of the graph in the centre of the plot. (LINE NUMBERS)

Also in this initialisation phase, over in modeller.py I wrote a propagation function which takes a length of time and the xyz velocity components of a particle as inputs, and creates an equation representing the change in position of the particle from these values, which is then differentiated to create an equation describing particle velocity. Then, for each second, the current time period is substituted into these equations to find the position and velocity of the particle at that given second in each direction in relation to the origin.(LINE NUMBERS) The data frame produced is then cut down to ensure no position values are beyond the limits of the axes, and the database representing the number of seconds the program runs for is similarly cut to ensure it is the same length as the database modelling the particle. (LINE NUMBERS) While creating a whole separate database to represent time seemed at this stage unnecessary, the animation method I was using required a database of this sort to set the number of frames for the animation. 


### Modelling

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

‌

‌
