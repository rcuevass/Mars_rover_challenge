"""

Module to do a complete test of Mars Rover challenge.
We make use of unittest from Python.


It is set up to show POSITIVE testing of whole code

This test module test contains MarsRoverTest class 
with two functions:

    1) test_upper : Very simple function to learning
                    the basis of unittest

    2) test_main_MarsRover : Actual function that performs
                             the desired end-to-end testing


"""

# Import unittest for testing
import unittest

# We import sys Pyhton library to be sure we set up the correct
# path location to import library to be tested...
import sys

# IMPORTANT --> User needs to change this path to where her/his
# lib folder is located
#sys.path.insert(0, '/path/to/folder/lib/')
sys.path.insert(0, '/Users/rogeliocuevassaavedra/mars_rover/lib/')
# ... and we do so
# Import main module; it is going to be tested end-to-end
import main_MarsRover


class MarsRoverTest(unittest.TestCase):


    def test_upper_lower(self):

        """ Learning to use unittest """

        self.assertEqual('rover'.upper(), 'ROVER')
        self.assertEqual('ROVER'.lower(), 'rover')
        self.assertEqual('roVer'.upper(), 'ROVER')


    def test_main_MarsRover(self):

        """ 
            Function that does a complete test of the 
            Mars Rover Mission
        """

        # Let's provide input as a user would.
        # We use the two cases provided by the problem statement

        # The user is welcome to add as many tests as (s)he wishes

        # The input will contain two rovers. 
        input = '5 5\n1 2 N\nLMLMLMLMM\n3 3 E\nMMRMMRMRRM'
        
        # Set expected output
        output = '1 3 N\n5 1 E\n'
    
        # We create dipatcher, as we did in the actual program,
        # from main_MarsRover class contained in main_MarsRover
        # module
        dispatcher = main_MarsRover.main_MarsRover()

        # We parse input provided...
        dispatcher.input_parser(input)

        # ... and dispatch input once it has been parsed
        dispatcher.dispatch_input()

        # We get the output to be displayed by using the 
        # display_output function found in main_MarsRover class...
        display_output = dispatcher.display_output()

        # ... and finally do the test using Pyhton's unittest
        self.assertEquals(display_output, output)


if __name__ == '__main__':

    # Doing the test...
    unittest.main()
