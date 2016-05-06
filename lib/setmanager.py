"""

This module controlls the managing of rover(s). 
It contains: 
            I. class SetRover
            II. class Manager

"""

# We import the math module to make use of Pi
import math as mt

"""

                    I. CLASS SETROVER 


The class Rover contains the following functions:

    1) __init__ : A typical initialization function

    2) get_heading: Obtains heading...very straightforward

    3) get_position: Obtains position...very straightforward

    4) set_heading: Sets heading of rover up

    5) set_position: Sets position of rover up



    IMPORTANT: This class is intended to be general enough to consider a future
               mission in which a rover is allowed to move in a three-dimensional 
               space, move in more than one direction (backwards, forward, left, right).

               The module presented here MAY not been extensively implemented to consider
               this future implementations but I believe is a good start


"""


class SetRover(object):


    def __init__(self, position, heading):

        """ Function that initialises a rover 

            Arguments: 

                position.- As name suggests, position of rover 

                heading.- As name suggests, heading of rover 
                

        """

        # Set position and heading
        self.position = position
        self.heading = heading


    def get_heading(self):

        """ Obtains a rover's heading """

        return self._heading

    def get_position(self):

        """ Obtains a rover's position """

        return self._position


    def set_heading(self, heading):

        """ Sets up a rover's heading 

            Arguments: 

                heading.- As name suggests, heading of rover 
                

        """


        # We check if the heading is a tuple with the expected length...
        if isinstance(heading, tuple) and len(heading) == 2:
            # ... if so we proceed to get the corresponding headings
            # via modulo 2*Pi
            self._heading = (heading[0] % (2*mt.pi), heading[1] % (2*mt.pi))
        else:
            # We display an error message and rise an exception otherwise

            print '   '
            print ' ='*25
            print '   '
            print '   LOOKS LIKE THE HEADING PROVIDED DOES NOT HAVE '
            print '   THE EXPECTED SHAPE '
            print '   '
            print ' ='*25
            print '   '


            raise ValueError('The heading provided does not have length 2')


    def set_position(self, position):

        """ Sets up a rover's position 

            Arguments: 

                position.- As name suggests, heading of rover 
                
        """

        # We check if the position of rover is a tuple with expected 
        # length.
        # In case it is...
        if isinstance(position, tuple) and len(position) == 3:
            # ... we just set the position
            self._position = position
        else:
            # We display a message error and rise an exception otherwise


            print '   '
            print ' ='*25
            print '   '
            print '   LOOKS LIKE THE POSITION PROVIDED DOES NOT HAVE '
            print '   THE EXPECTED SHAPE '
            print '   '
            print ' ='*25
            print '   '

            raise ValueError('The position provided does not have length 3')


    # We obtain position and heading from property of class
    # This was intended for LEARNING purposes....I had not used property before...
    position = property(get_position, set_position, None)
    heading = property(get_heading, set_heading, None)



"""

                    II. CLASS MANAGER


The class Manager contains the following functions:

    1) __init__ : A typical initialization function


    2) get_rover: Provides object of rover assigned to a given id 

    3) check_position: It checks if a given rover position is 
                       already taken or not

    4) add_rover: Add rolles to the mission. Checks if there is
                  duplicity in rovers ids

    5) rover_inside_grid: Verifies that current rover position
                          is inside the grid

    6) available_position: Checks availability of rover position

    7) get_corner: Gets corner

    8) set_corner: Sets corner

"""


class Manager(object):

    def __init__(self, corner):

        """ We initialise the manager by specifying opposite 
            corner of the grid (lower left and upper right) 

            Argument: 

                corner.- As name suggests, position of rover 
                
                

        """


        # We set an empty dictionary to keep track of rovers
        self.rovers = {}
        # Initialise corner
        self.corner = corner


    def get_rover(self, rover_id):

        """ Function that provides object of rover assigned to 
            a rover id (rover_id) 

            Argument: 

                rover_id.- A label that identifies rover to keep track of it
             

        """
       
        # We check if a given rover is not in the set of rovers
        # given by keys in rovers dictionary...
        if not rover_id in self.rovers.keys():
            # ... if not found, display an error message
            # and raise an exception

            print '   '
            print ' ='*25
            print '   '
            print '      YOU SEEM TO HAVE LOST A ROVER!!! '
            print '      WHAT HAPPENED TO ' , rover_id , ' ROVER?'
            print '   '
            print ' ='*25

            raise Exception('We cannot find %s rover' % str(rover_id))
        # In case the rover is indeed in the set of rovers we proceed
        # to add it to dictionary
        else:
            return self.rovers[rover_id]



    def check_position(self, position):

        
        """ Function that checks the provided position is allowed

            Argument: 

                position.- As name suggests, position of rover
             

        """

        if not isinstance(position, tuple) and len(corner) == 3:


            print '   '
            print ' ='*25
            print '   '
            print '   LOOKS LIKE THE ROVER POSITION DOES NOT HAVE '
            print '   THE EXPECTED SHAPE '
            print '   '
            print ' ='*25
            print '   '

            raise Exception('Rovers position seem to have the wrong shape')
        if not (isinstance(position[0], int) and isinstance(position[1], int) 
            and isinstance(position[2], int)):


            print '   '
            print ' ='*25
            print '   '
            print '   LOOKS LIKE THE ROVER POSITION ARE FRACTIONAL '
            print '   '
            print ' ='*25
            print '   '

            raise Exception('Rovers position is fractional')
        if not self.available_position(position):



            print '   '
            print ' ='*25
            print '   '
            print '   IT SEEMS LIKE ONE OF YOUR ROVERS IS TRYING TO TAKE '
            print '   A POSITION THAT IS ALREADY OCCUPIED '
            print '   '
            print ' ='*25
            print '   '

            raise Exception('Rover already occupies %s' % str(position))
        elif not self.rover_inside_grid(position):

            """ IMPORTANT:
                This code is intended to be as general as considering (x,y,z)
                coordinates. However, given the current description of the problem
                we only print (x,y) coordiantes as the rover is considered 
                to move in a 2D grid 
            """

            pos2D = position[:2]


            print '   '
            print ' ='*25
            print '   '
            print ' WARNING! -- ROVER FOUND IN ' , pos2D 
            print ' POSITION OUTSIDE OF THE GRID'
            print '   '
            print ' ='*25
            print '   '

            raise Exception('Position %s is out of grid' % str(pos2D))

    def add_rover(self, rover_id, position, heading):

        """ Function that adds a rover to the manager. 
            It checks that the rover being added has a unique id
            and is not attempting to take an already-occupied 
            position 


            Arguments: 

                rover_id.- A label that identifies rover to keep track of it

                position.- Position of rover with label rover_id
                
                heading.- Heading of rover with label rover_id
        
        """

        # We first check position...
        self.check_position(position)
        # ... and then proceed to check whether position has been taken
        # by exploring keys in dictionary
        if not rover_id in self.rovers.keys():
            # If it has not been taken we add to dictionary...
            self.rovers[rover_id] = SetRover(position, heading)
        else:
            # ... otherwise we display an error message and raise an exception

            print '   '
            print ' ='*25
            print '   '
            print '      LOOKS LIKE YOU ARE TRYING TO DUPLICATE ROVER IDS!!! '
            print '      ROVER ' , rover_id , ' ALREADY EXISTS'
            print '   '
            print ' ='*25


            raise Exception('Rover id %s is already taken' % str(rover_id))



    def rover_inside_grid(self, position):

        """ Function that checks if the current position of rover is 
            within grid boundaries 

            Argument:

                position.- Position of rover 


            IMPORTANT NOTE :
                            This function considers the general case of 
                            3D space (x,y,z)

        """

        # We get coordiantes from position
        x, y, z = position

        # We use auxiliary variables to avoid lengthy and confusing 
        # programming instructions....

        # Let's get "min" and "max" values of X, Y and Z according
        # to the corner given
        # For x: 
        x1 = self.corner[0][0] ; x2 = self.corner[1][0]
        # For y: 
        y1 = self.corner[0][1] ; y2 = self.corner[1][1]
        # For z: 
        z1 = self.corner[0][2] ; z2 = self.corner[1][2]

        return (True if ( (x1 <= x <= x2 or x2 <= x <= x1) and 
                          (y1 <= y <= y2 or y2 <= y <= y1) and
                          (z1 <= z <= z2 or z2 <= z <= z1) ) 
                else False)


    def available_position(self, position):

        """ Function that checks whether the provided position is available 

            Argument:

                position.- Position of rover 

        """

        # The value to be retunred is simplified by the use of 
        # lists comprehension: It returns returns True if position is
        # available and False otherwise.
        return (False if position in [r.position for r in self.rovers.values()] 
                else True)


    def get_corner(self):

        """ Function that obtains corner from manager """

        return self._corner


    def set_corner(self, corner):

        """ Function that sets up corner from manager


            Argument:

                corner.- As name suggests, corner provided

            IMPORTANT: Notice this function consideres the possible
                       extension of the code to have the rover moving
                       in a 3D space
        """

        # We check if corner is a tuple and has two coordinates (X,Y)...
        if isinstance(corner, tuple) and len(corner) == 2:
            if (isinstance(corner[0], tuple) and len(corner[0]) == 3 and 
                isinstance(corner[1], tuple) and len(corner[1]) == 3):
                self._corner = corner
            else:


                print '   '
                print ' ='*25
                print '   '
                print '   LOOKS LIKE THE SHAPE OF CORNER PROVIDED IS WRONG '
                print '   '
                print ' ='*25
                print '   '

                raise Exception('The corner does not have the proper length')            
        else:

            print '   '
            print ' ='*25
            print '   '
            print '   LOOKS LIKE THE SHAPE OF CORNER PROVIDED IS WRONG '
            print '   '
            print ' ='*25
            print '   '

            raise Exception('The corner does not have the proper length')



    # Get corner from corresponding class property
    # This was intended for LEARNING purposes....I had not used property before...
    corner = property(get_corner, set_corner, None)
