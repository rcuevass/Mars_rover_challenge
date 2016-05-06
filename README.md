# MARS ROVER CHALLENGE

## 1. Details of Challenge

### 1a. Description: 

A squad of robotic rovers are to be landed by NASA on a plateau on Mars. This plateau, which is curiously rectangular, must be navigated by the rovers so that their on board cameras can get a complete view of the surrounding terrain to send back to Earth.

A rover’s position is represented by a combination of an x and y co-ordinates and a letter representing one of the four cardinal compass points. The plateau is divided up into a grid to simplify navigation. An example position might be
`0, 0, N` , which means the rover is in the bottom left corner and facing North.

In order to control a rover, NASA sends a simple string of letters. The possible letters are `L` , `R` and `M` . `L` and `R` makes the rover spin 90 degrees left or right respectively, without moving from its current spot. `M` means move forward one grid
point, and maintain the same heading. Assume that the square directly North from `(x,y)` is `(x,y+1)`.

### 1b. Input:

The problem below requires some kind of input. You are free to implement any mechanism for feeding input into your solution.

The first line of input is the upper-right coordinates of the plateau, the lower-left coordinates are assumed to be `(0,0)` . The rest of the input is information pertaining to the rovers that have been deployed. Each rover has two lines of input. The first line gives the rover’s position, and the second line is a series of instructions telling the rover how to explore the plateau.

The position is made up of two integers and a letter separated by spaces, corresponding to the x and y co-ordinates and the rover’s orientation. Each rover will be finished sequentially, which means that the second rover won’t start to move until the first one has finished moving.


### 1c. Output:

The output for each rover should be its final co-ordinates and heading.


### 1d. Example of input and output

Test Input:

`5 5`

`1 2 N`

`LMLMLMLMM`

`3 3 E`

`MMRMMRMRRM`

Expected Output:

`1 3 N`

`5 1 E`

## 2. General strategy

### 2a. Basic primitive idea. 

A basic code to tackle the challenge is relatively *straightforward* if one limits the code to make the rover do **exclusively** what is stated in the problem. For instance, the begining of a simple implementation could look like follows:

`# Set up directions`

`directs = 'NSEW'`

`# Set up vectors for change of directions`

`turns=[(0,1),(0,-1),(1,0),(-1,0)]`

`# Mappig lettered instrutions through lambda functions`

`R = lambda X, Y, dis: (X, Y, (dis + 1) % 4)`

`L = lambda X, Y, dis: (X, Y, (dis - 1 + 4) % 4)`

`M = lambda X, Y, dis: (x + turns[dis][0], y + turns[dis][1], dis)`

`# Continued code doing parsing of input and such...`

As mentioned, althogh the above exemplified simple code is functional, it limits future growing and modular improvement of it.

### 2b. A modular approach

Building up on the core idea exemplified above, the code included with this **README** file is modular and allows, in principle, to make further modifications in a simple fashion. It is modular in nature and intends to *departmentalize* actions performed from command line on rover(s). For instance, this code keeps track of rovers to avoid allowing to rovers occupy the same position, keeps track of their position to be sure there are inside the provided grid and it can be *easliy* modified to allow non-fractional displacements within the grid, more general cardinal directions (`NE`,`NW`,`SE`,`SW`,etc.) and possible extensions to allow rover move in a three-dimensional space. This is achived by doing mapping from angular values to three dimensional coordinates (spherical coordiantes mapping).

The structure of the present code is expalined in the rest of this document and the code itself has been as commented and documented as possible to make it easy to follow.

## 3. Folders and modules 

The program package includes two folders as explained below. 


###   3a. lib folder

Folder containing the main/driver module and modules utlized by it.


###   3b. test folder

Folder containing scripts that test each of the files included in the lib folder. Each of the modules in the test folder uses the [unittest Pyhton library](https://docs.python.org/2/library/unittest.html)


In the following table we summarize the content of the each folder:

Folder | Contents
--- | --- 
**lib** | main_MarsRover.py -- Driver of the code. This file executes the code by running `python main_MarsRover.py`
    | rotatemove.py -- Module that performs rotations and displacements of rovers. It is invoked by main_MarsRover.py 
    | setmanager.py -- Module that takes care of proper performance of mission: sets and gets rover, checking rover positon within grid, adding rovers to the mission, etc. It is invoked by rotatemove.py
**tests** | test-integrated-correct.py -- Module that performs an end-to-end test of the whole code. Set up to pass all tests. It invokes main/driver main_MarsRover.py
      | test_integrated_wrong.py -- Module that performs an end-to-end test of the whole code. Set up to pass one test and fail another one. Included to facilitate its usage by judge (it shows on purpouse how it catches a failed test). It invokes main/driver main_MarsRover.py
      | test_rotatemove_correct.py -- Module that performs tests on rotations and displacements of rover. It includes test on only rotations, only displacements and both rotations and displacements. Set up to pass all tests. It invokes rotatemove.py
      | test_rotatemove_wrong.py -- Module that performs tests on rotations and displacements of rover. It includes test on only rotations, only displacements and both rotations and displacements. Set up to pass all tests but one. Included to facilitate its usage by judge (it shows on purpouse how it catches a failed test). It invokes rotatemove.py
      | test_setmanager_correct.py -- Module that performs tests on setmanager. It includes tests on adding rovers to mission, checking if a position is already occupied by another rover and if current position of rover is within specified grid . Set up to pass all tests. It invokes setcontroller.py
      | test_setmanager_wrong.py -- Module that performs tests on setmanager. It includes tests on adding rovers to mission, checking if a position is already occupied by another rover and if current position of rover is within specified grid . Set up to pass all tests. Set up to pass all tests but one. Included to facilitate its usage by judge (it shows on purpouse how it catches a failed test). It invokes setcontroller.py


## 4. How to run the code and tests 

### 4a. Running the code

We simply execute in folder **lib** the command line: `python main_MarsRover.py` 
Instructions will prompt in screen. Such instructions are clear and friendly to help the user running the code.


### 4b. Running tests

The testing modules are found in the **tests** folder. The folder contains six scripts for tesing. For each script in the **lib** folder there are two scripts for testing, one to check that all tests set are passed and the other one set purpously wrong to show that the tester catches mistakes. 
In each of the testing modules there is line that sets the proper location of the **lib** folder, which is where the modules to be tested are found. The user should make sure to set this path properly, that is:

                sys.path.insert(0, '/path/to/folder/lib/')


## 5. General comments and future tests

In this code we have tried to take into consideration options to make the mission user friendly. For instance:

- We display a welcome message on screen to briefly explain how to input instructions after automatically cleaning the screen for users.
- Alphabetic characters such as cardinal points/headings (`N S E W`) and instructions on rover (`M R L`) are case insensitive. That is, the user can input such instructions in either upper or lower case letters.
- We have tried to consider as many exceptions as possible in order to inform the user what could have gone wrong with the mission.
- Final position(s) of rover(s) are also announced with a clear message after cleaning again screen for users to avoid cluttering text and confusion for users.

The short list above is not, of course, exhaustive and much more details and exceptions should be considered for continuous imporvement of the code.

Finally, as mentioned, it is possible to *easily* let rovers have more degrees of freedom for more general and *realistic mission*. These extensions, however, have not been tested and a possible natural next step could be to relax constraints provided, allow rover have these extra degrees of freedom and set new tests on such degrees of freedom.

