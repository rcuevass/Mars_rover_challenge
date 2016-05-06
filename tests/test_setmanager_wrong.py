
"""

Module to test manager library used in the 
MarsRover Challenge program. 

We make use of unittest from Python.

This test module test contains TestManager class 
with three functions:

    1) test_available_position : Function that tests rotations function
                                 that tracks availability of positions for 
                                 different rovers

    2) test_rover_inside_grid : Function that tests function checking if
                                rover is within grid boundaries  

    3) test_add_rovers : Function that tests function adding rovers to mission

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
# Import manager as is going to be tested
import setmanager


class TestManager(unittest.TestCase):


    def test_available_position(self):

        """ 
            Function that tests the performance of the 
            test_available_position from manager module
        """

        """
            IMPORTANT: The following tests have been rescticed to the
                       XY plane. It can, however, be extended to a
                       3D space by setting z to a number different 
                       from zero
        """

        # We first set grid providing lower left and upper right corners...
        test_manager = setmanager.Manager(((0, 0, 0), (5, 5, 0)))

        # ... add a rover with given id to a postion with given heading
        test_manager.add_rover('id_1', (3, 3, 0), (0, mt.pi/2))

        # We now execute the following comprehension list varying values of 
        # x, y (we can also vary z if we extend to 3D) and check if the 
        # position (x,y,0) equals the given (3,3,0) for this example. In case
        # it coincides with the position (3,3,0) we assert False 
        # (position already taken)... 
        [self.assertFalse(test_manager.available_position((x, y, 0))) if (x, y, 0) == (3, 3, 0) 
                # ... otherwise (position not taken) we assert True
                else self.assertTrue(test_manager.available_position((x, y, 0)))
                # This is done for values of x and y in the square [0,5] X [0,5]
                for x in range(6) for y in range(6)]



    def test_rover_inside_grid(self):

        """ Function that tests the 
            test_rover_inside_grid function """


        # We first set grid providing lower left and upper right corners
        test_manager = setmanager.Manager(((0, 0, 0), (5, 5, 0)))

        # Let's test some points that are indeed inside the grid...
        self.assertTrue(test_manager.rover_inside_grid((0, 0, 0)))
        self.assertTrue(test_manager.rover_inside_grid((5, 5, 0)))

        # ...and some other that are not
        self.assertFalse(test_manager.rover_inside_grid((0, 6, 0)))
        self.assertFalse(test_manager.rover_inside_grid((-1, 0, 0)))

        # Let's even take one rover out of the XY plane
        self.assertFalse(test_manager.rover_inside_grid((3, 3, 1)))

        # Let's do another test that is, in purpouse, asserted as True 
        # when is actuallly False

        """ IMPORTANT : The user is welcome to comment out the following
                        line out to see the effects of this testing
        """
        #self.assertTrue(test_manager.rover_inside_grid((0, -2, 0)))

       
    def test_add_rovers(self):
        
        """ Function that tests adding of rover """

        # We first set  grid providing lower left and upper right corners
        test_manager = setmanager.Manager(((0, 0, 0), (5, 5, 0)))

        # We now add a rover with given id, position and heading
        test_manager.add_rover('id_1', (3, 4, 0), (mt.pi/2, 0))

        """ IMPORTANT : The following line is set up wronlgy on purpouse
                        to see the effect of a false/positive test
        """

        # And test if the adding was succesfully performed
        self.assertTrue('id_2' in test_manager.rovers.keys())




if __name__ == '__main__':
    unittest.main()
