"""

Module to test rotatemove library used in the 
MarsRover Challenge program. 

It is set up to show NEGATIVE testing of module

We make use of unittest from Python.

This test module test contains TestRotateMove class 
with three functions:

    1) test_rotate : Function that EXCLUSIVELY tests rotations 

    2) test_move : Function that EXCLUSIVELY tests displacements 

    3) test_rotate_move : Function that tests BOTH rotations AND 
                           displacements

"""

# We import the math module to make use of Pi
import math as mt

# Import unittest for testing
import unittest

# We import sys Pyhton library to be sure ...
import sys

# we set up the correct
# path location to import library to be tested...

# IMPORTANT --> User needs to change this path to where her/his
# lib folder is located
#sys.path.insert(0, '/path/to/folder/lib/')
sys.path.insert(0, '/Users/rogeliocuevassaavedra/mars_rover/lib/')

# ... and we do so
# Import library to be tested
import rotatemove


class TestRotateMove(unittest.TestCase):

    def test_rotate(self):

        """ Function to test ONLY rotations of rover """

        # We start by creting the class for rotatemove 
        # Recall that class is created by setting lower left
        # and upper right corners of grid:
        # Dependency to follow: rotatemove.py ---> controller.py
        # The corners used here are motivated by statement of the problem
        # lower left --> (0,0,0)
        # upper right ---> (5,5,0)
        test_rotate = rotatemove.RotateMove(((0, 0, 0), (5, 5, 0)))

        # We add rover by setting it up at with position and heading given by
        # statement of the problem
        test_rotate.add_rover('id_1', (2, 1, 0), (mt.pi/2, mt.pi/2))

        # We test rotation to the right...       
        test_rotate.rotate('id_1', -mt.pi/2, 0)

        # ... and test it...
        self.assertEquals(test_rotate.get_rover('id_1').heading, (0., mt.pi/2))

        # ... and now followed by a rotation to the left      
        test_rotate.rotate('id_1', mt.pi/2, 0)

        # and test it again
        self.assertEquals(test_rotate.get_rover('id_1').heading, (mt.pi/2, mt.pi/2))
    

    def test_move(self):

        """ Function to test ONLY displacements of rover """

        # We start by creting the class for rotatemove 
        # Recall that class is created by setting lower left
        # and upper right corners of grid:
        # Dependency to follow: rotatemove.py ---> controller.py
        # The corners used here are motivated by statement of the problem
        # lower left --> (0,0,0)
        # upper right ---> (5,5,0)
        test_move = rotatemove.RotateMove(((0, 0, 0), (5, 5, 0)))

        # We add rover by setting it up at with position and heading given by
        # statement of the problem
        test_move.add_rover('id_2', (2, 1, 0), (mt.pi/2, mt.pi/2))


        # We test displacement by one unit ...      
        test_move.move('id_2', 1)

        # ... and test it...
        self.assertEquals(test_move.get_rover('id_2').position, (2,2,0))

        # followed by no displacement ...    
        test_move.move('id_2', 0)

        # ... and test it...
        self.assertEquals(test_move.get_rover('id_2').position, (2,2,0))

        # ... followed by final displacemnt by one unit    
        test_move.move('id_2', 1)
    
        # and test final position
        self.assertEquals(test_move.get_rover('id_2').position, (2,3,0))



    def test_rotate_move(self):

        """ Function to test BOTH rotations and displacements of rover """

        # We start by creting the class for rotatemove 
        # Recall that class is created by setting lower left
        # and upper right corners of grid:
        # Dependency to follow: rotatemove.py ---> controller.py
        # The corners used here are motivated by statement of the problem
        # lower left --> (0,0,0)
        # upper right ---> (5,5,0)
        test_rotate_move = rotatemove.RotateMove(((0, 0, 0), (5, 5, 0)))

        # We add rover by setting it up at with position and heading given by
        # statement of the problem
        test_rotate_move.add_rover('id_3', (2, 1, 0), (mt.pi/2, mt.pi/2))


        # We test displacement by one unit ...      
        test_rotate_move.move('id_3',1)

        # ... and test it...
        self.assertEquals(test_rotate_move.get_rover('id_3').position, (2,2,0))


        # ...followed by a rotation to the right...       
        test_rotate_move.rotate('id_3',-mt.pi/2, 0)

        # ... and test it...
        self.assertEquals(test_rotate_move.get_rover('id_3').heading, (0.,mt.pi/2))

        # ... and now followed by one unit displacement     
        test_rotate_move.move('id_3',1)

        """ IMPORTANT: We set, purpously, a wrong expected output 
                       Notice we have changes the id of rover from id_3 to id_4
        """
        self.assertEquals(test_rotate_move.get_rover('id_4').position, (3,2,0))
        
        

if __name__ == '__main__':
    unittest.main()
