"""

This module contains the class MoveRotates


                    CLASS MOVEROTATES


Such a class contains the following functions:

    1) rotate: performs rotations of rover around Z axis

    2) move: performs displacements of rover on the grid

"""


# We import the math module to make use of Pi
import math as mt
# We import library that keeps track of rovers and actions on them
import setmanager


class RotateMove(setmanager.Manager):

    """ Class that specifies rotations and displacements of rover """


    def rotate(self, rover_id, phi, theta):
        
        """ Function that rotates rover around the Z axis 

            Arguments: 

                rover_id.- A label that identifies rover to keep track of it

                phi.- Angular value that provides longitude of rover 
                
                theta.- Angular value that provides latitude of rover
        
        
        IMPORTANT NOTE: In general we could allow a rover to face any direction
                    in 3D given by two angles (spherical coordianates)

                    In spherical coordianates (r,theta,phi) phi is the angle
                    that allows rotations around the Z axis (longitude)
                    while theta is the angle meassured from the Z axis 
                    (latitude)

                    The present request of the program allows only four 
                    cardinal points. We therefore allow phi to
                    be multiple of Pi/2 only and theta = 0

        """
        # We only allow rotations by 90 degrees around the Z axis
        # and no changes in the latitude (theta = 0)
        # We make sure this is the case...
        if ( theta == 0. ) and ( phi % (mt.pi/2) ) == 0.:
            # If consistent, we set id of the rover
            r = self.get_rover(rover_id)
            # and set longitud and latitude values...
            lon, lat = r.heading
            lat += theta
            lon += phi
            # ... from which the heading is obtained
            r.heading = (lon, lat)
        #  
        # ... otherwise we rise an exception
        else:

            print '   '
            print ' ='*25
            print '   '
            print '   THERE SEEMS TO BE AN ISSUE WITH ROVERS ROTATION! '
            print '   '
            print ' ='*25
            print '   '
            
            raise Exception('These rotations performed on rover are not allowed')



    def move(self, rover_id, displacement):
        

        """ Function that performes displacements on rover

            Arguments: 

                rover_id.- A label that identifies rover to keep track of it

                displacement.- Value that provides the magnitud of displacement
                               the rover will experiment 
                
        
        IMPORTANT NOTE: In general we could allow a rover to move by any
                        amount we wish and by non-integer intervals

                        The present request of the program,however, allows 
                        displacement by one unit and in integer increments
                        AND only to move forward within in the grid

                        Position of rover is updated and kept track of so that
                        the rover does not end up outside of the grid or runs
                        into another rover

                        In the future this function can be modified to relax
                        conditions and allow rovers to move backwards and 
                        fractional distances
        
        """
       
        # We first make sure the displacement is positive and an inyteger
        if isinstance(displacement, int) and displacement > 0:
            # If so we proceed to get rover's id...
            r = self.get_rover(rover_id)
            # ... initialize its cartesian coordiantes...
            x, y, z = r.position
            # ...get spherial locational information (heading)
            phi, theta = r.heading
            # and get the actual cartesian coordinates from the
            # spherical ones.
            # Notice we are enforcing the coordinates of rover to 
            # be integer
            x += int(mt.sin(theta)*mt.cos(phi))
            y += int(mt.sin(theta)*mt.sin(phi))
            z += int(mt.cos(theta))


            # We check the position is allowed
            self.check_position((x, y, z))
            r.position = (x, y, z)
            # ... and update displacement
            self.move(rover_id, displacement - 1)

        # In case the displacement is negative we rise an exception...
        elif displacement < 0:

            print '   '
            print ' ='*25
            print '   '
            print '   LOOKS LIKE YOU ARE TRYING TO MOVE THE ROLLER BACKWARDS! '
            print '   '
            print ' ='*25
            print '   '

            raise Exception('The rover is allowed to only move forward')

        # ...and rise another one if the displacement is not an integer
        elif not isinstance(displacement, int):

            print '   '
            print ' ='*25
            print '   '
            print '   LOOKS LIKE YOU ARE TRYING TO MOVE ROLLER BY A '
            print '   FRACTIONAL AMOUNT! '
            print '   '
            print ' ='*25
            print '   '

            raise Exception('Displacement is only allowed in integer units')


    