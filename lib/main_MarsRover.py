"""

This is the main/driver for the excecution of the Mars Rover Challenge
It contains: 
			I. class main_MarsRover
			II. function main() for excecution


					I. CLASS MAIN_MARSROVER

The class main_MarsRover contains the following functions:

	1) __init__ : A typical initialization function

	2) welcome_message: Displays header and brief instruction

	3) move: Moves rover one unit on the grid in the direction the
			 the rover is facing

	4) L_rotate: Rotates rover 90 degrees counterclockwise

	5) R_rotate: Rotates rover 90 degress clockwise

	6) input_parser : Parses input from the command line

	7) instruction_parser : Parses instructions from the command line

	8) corner_parser : Parses the given upper corner

	9) controller_heading_check: Verifies heading to controller
									 is correct 

	10) heading_checker: Verifies that headings given are allowed

	11) parse_add_rover: Parses each rover given and adds them as they come

	12) dispatch_input: Dispatches inputs received for rover to controller

	13) display_output: Displays the final positon of rovers


"""

# We import the math module to make use of Pi
import math as mt
# We import os to do basic interaction with command line
import os
# Import sys library that allows interaction with the interpreter
import sys
# We import library that handles moves and rotations of a rover
import rotatemove

# Main and only class of this program
class main_MarsRover(object):

	""" IMPORTANT: This code, particularly this class, is written
				   in order to consider future extensions of 
				   more general commands and heading of a rover.
				   For instance, we created a dictionary of headings 
				   in terms of the rotation values of rover around 
				   the Z-axis as opposed to set a simple list or 
				   strings such as 'NSEW'

	"""

	# We set a dictionary to handle heading of rovers
	# N = North, associated with theta = 90 degrees
	# S = North, associated with theta = 270 degrees 
	# E = North, associated with theta = 0 degrees
	# W = North, associated with theta = 180 degrees
	Headings = {'N':mt.pi/2,'S':3*mt.pi/2,'E':0,'W':mt.pi}



	# We set a list to capture the allowed commands
	# L = Left
	# R = Right
	# M = Move
	Commands = ['L', 'R', 'M']


	def __init__(self):

		""" Simple and typical initialization """
		
		# Initialize controller
		self.commander = None
		
		# Initialize array to keep track of instruction
		self.Commands = []

		# Initialize array to keep track of rovers
		self.rovers = []


	def welcome_message(self):

		""" Function to display welcoming and brief instruction 
			for the user """

		# We display instructions for the user
		print '   '
		print '*'*40
		print '*                                      *'
		print '*      MARS ROVER CHALLENGE            *'
		print '*                                      *'
		print '*'*40
		print '   '
		
		print 'You will be asked to enter: '
		print ' 1. Upper-right corner of grid '
		print ' 2. Rover position and heading '
		print ' 3. Sequence of commands ' 
		print '   '
		print 'You can enter information for more than one rover.'
		print 'When you are finished providing rovers and its information'
		print 'please hit enter when you are asked again Enter x y Headg.:'
		print '   '
		print '     Have fun!!!'
		print '   '


	def move(self, rover_id):

		""" Function that moves rover ONE (1) grid position forward 

			Argument: 

				rover_id.- A label that identifies rover to keep track of it
		"""


		# Self-explanatory action of the function
		# Notice here we allow to move the rover only one unit
		self.commander.move(rover_id, 1)

	def L_rotate(self, rover_id):

		""" Function that rotates rover 90 degrees counterclockwise 

			Argument: 

				rover_id.- A label that identifies rover to keep track of it
		"""

		# Self-explanatory action of the function
		self.commander.rotate(rover_id,  mt.pi/2, 0)

	def R_rotate(self, rover_id):

		""" Function that rotates rover 90 degrees clockwise 

			Argument: 

				rover_id.- A label that identifies rover to keep track of it
		"""

		# Self-explanatory action of the function
		self.commander.rotate(rover_id, -mt.pi/2, 0)


	def input_parser(self, input):

		""" Function that parses input strings 

			Argument:

				input.- Instructions received by user from 
						command line (prompt)
		"""

		#
		# We split input commands at the "chomp" \n
		input = input.split('\n')
		# We initialize corner..
		corner = self.corner_parser(input[0])
		# ... as well as controller
		self.commander = rotatemove.RotateMove(((0, 0, 0),corner)) 
		#                                                          

		# For the first line in the input command...
		for line in input[1::2]:
			# ... we parse it to get information about location and 
			# heading of rover
			self.parse_add_rover(line)
		# For the second line in the input command...
		for line in input[2::2]:
			# ... we parse it to get information regarding motion
			# commands for the corresponding rover
			self.instruction_parser(line)



	def instruction_parser(self, input):

		""" Function that parses and adds string instructions 

			Argument:

				input.- Instructions received by user from 
						command line (prompt)
		"""


		# It appends instructions from the command line to the Commands array
		# previous initilialized
		self.Commands.append([strg for strg in input.strip()])
		


	def corner_parser(self, corner):

		""" Function that parses the upper corner provided 

			Argument:

				corner.- Coordinates of the upper corner provided
						 by user from command line
		"""


		# We use try to feed the tuple for the upper corner.
		# In case we do not receive the format expected...
		try:
			# We return the needed tuple with integers
			# uc = uppper corner
			return tuple([int(uc) for uc in corner.strip().split(' ')] + [0])
		# ... we rise an exception with a message
		except ValueError, e:

			print '   '
			print ' ='*25
			print '   '
			print '      CORNER HAS NOT BEEN CORRECTLY SPECIFIED! '
			print '   '
			print ' ='*25
			print '   '
			raise ValueError('Corner must be a (int , int) pair!')



	def controller_heading_check(self, heading_val):

 
		""" It checks correct heading of roller

			Argument:

				heading_val.- Value of angle (rads) associated
							  with an allowed heading

			Returns: 

				heading_key.- Cardinal point associated with 
							  value of angle provided in heading_val

		"""

		if not heading_val in self.Headings.values():
			print '   '
			print ' ='*25
			print '   '
			print '      THERE IS AN ISSUE WITH ROVERS HEADING! '
			print '   '
			print ' ='*25
			raise Exception('Controller heading unkwnon %s' 
							% str(heading_val))
		else:
			for heading_key in self.Headings.keys():
				if self.Headings[heading_key] == heading_val:
					return heading_key

   

	def heading_checker(self, heading):

		""" Function that verifies that headings given are allowed 

			Argument:

				heading.- Value of heading provided by user 
						  (key in dictionary)

			Returns:

				Heading[heading].- Angular value associated with 
								   cardinal point (value in dictionary)

		"""

		# If a heading given is NOT in the valid set (N,S,E,W)....
		# (notice it is associated with keys of Headings dictionary)
		if not heading in self.Headings.keys():
			# ... we display a message of warning and raise exception
			print '   '
			print ' ='*25
			print '   '
			print '   A NON-VALID HEADINGS HAS BEEN PROVIDED! '
			print '   '
			print ' ='*25
			print '   '
			raise Exception('User provided a non-valid heading %s' 
							% str(heading))

		# ... otherwise we proceed with the headings given
		else:
			return self.Headings[heading]



	def parse_add_rover(self, input):

		""" Function that parses a given rover and adds more rovers 


			Argument:

				input.- String that represents a rover given by user
						(xCoor,yCoor,Card.Point)

		"""

		# Firstly we strip and split line and feed it to the rover.
		rover = input.strip().split(' ')
		# We make sure the heading is capitalized to have correct matching
		# with keys in dictionary
		rover[2] = rover[2].upper() 
		# Since we are expecting an input of three elements (e.g 1 3 N), we make sure 
		# that's the case....
		if len(rover) == 3:
			# We expect the user enters a tuple pertaining Coordinates (x y)
			# and heading (N or S or E or W)...
			try:
				position = tuple([int(v) for v in rover[0:2]] + [0])
			#
			# ... if we do not receive what we expected then we raise 
			# and error message...

			#except ValueError, e:
			except ValueError:
				print '   '
				print ' ='*25
				print '   '
				print '      POSITION HAS NOT BEEN CORRECTLY SPECIFIED! '
				print '   '
				print ' ='*25
				print '   '
				raise ValueError('Rover position has not been correctly specified!')

			heading = (self.heading_checker(rover[-1]), mt.pi/2)
			self.commander.add_rover(input, position, heading)
			self.rovers.append(input) #rover id starting position and heading
		# ... in case the line given has no three elements, we raise an exception
		elif len(rover) <> 3:
			print '   '
			print ' ='*25
			print '   '
			print '      ROVER HAS NOT BEEN CORRECTLY SPECIFIED!'
			print '   '
			print ' ='*25
			print '   '
			raise Exception('Check coordinates and heading given!')

	
	def dispatch_input(self):

		""" Function that dispatches rover input to Controller """
		# For every pair of rover and Commands given...
		for rover, Commands in zip(self.rovers, self.Commands):
			# ... we loop over instructions in the given Command
			# to see if corresponds to Left, Right, or Move
			for instruction in Commands:
				# If Left we use the L_rotate function...
				if instruction == 'L':
					self.L_rotate(rover)
				# If Right we use the R_rotate function
				elif instruction == 'R':
					self.R_rotate(rover)
				# If Move we make the rover move with the move function
				elif instruction == 'M':
					self.move(rover)
				# If none of the above then we rais and exception
				else:
					print '   '
					print ' ='*25
					print '   '
					print '      AN UNKNOWN INSTRUCTION HAS BEEN GIVEN!'
					print '   '
					print ' ='*25
					print '   '
					raise Exception('Unknown instruction given %s' % str(instruction))



	def display_output(self):

		""" Function that provides final position of rovers 

			Returns:
					output.- Final position of rover to displayed 
							 in screen for user's information

		"""

		output = ""


		# For every rover in the collection...
		for rover in self.rovers:
			r = self.commander.get_rover(rover)
			heading = self.controller_heading_check(r.heading[0])
			output += '%d %d %s\n' % (r.position[0], r.position[1], heading)

		return output



"""

					II. MAIN (EXECUTION) FUNCTION

"""

def main():

	""" Main (driver) program for Mars Rover challenge  
	Just excecute python main_MarsRover.py """
	

	# Let's clean screen for user
	os.system('clear')

	# Create dispatcher from class
	dispatcher = main_MarsRover()

	# We display welcome message for user
	dispatcher.welcome_message()

	# After instructions have been displayed we pause code 
	# until user hits enter...
	raw_input("Press enter to begin the mission...")

	# ... and clear screen again to avoid confusion
	os.system('clear')

	# We set a blank input
	input = ''

	# Display guidance for user
	print 'Please provide upper-right corner of grid as a pair'
	print 'E.g. 5 5'
	# We receive coordiantes as raw input from line command
	corner = raw_input('Enter upper-right corner of grid  (X Y): ')
	# We add upper corner provided to input 
	input += corner + '\n'
	# While user keeps providing information regarding rovers...
	while(True): 
		# Request position and heading...
		print ' '
		print 'Please enter rover position and heading,'  
		print 'E.g. 1 2 N OR 3 3 E OR ...'
		print ' '
		print 'If you have already entered at least one set'
		print 'of position and heading you can hit enter to'
		print 'see final position of rovers. Otherwise,'
		print 'you can add more rovers if you wish'
		print ' '
		# ... and receive it as raw input
		r = raw_input('Enter (xCoord yCoord Headg.):')
		# If there is no info receieved...
		if r == '':
			# ... break..
			break
		# ... otherwise keep adding input.
		else:
			input += r + '\n'

		# Request sequence of commands....
		print 'Please enter sequence of commands'
		print 'E.g. LMLMLMLMM OR MMRMMRMRRM OR ...'
		print ' '
		# ... and get them as raw input while upper casing them
		# to assure correct matching with list [L,R,M]
		Commands = raw_input('Enter commands for this rover:').upper()
		# ... and keep accumulating them.
		input += Commands + '\n'
   

	# We strip input from "chomp"
	# In case the last element of input is a "chomp", we handle it...
	if input[-1] == '\n':
		input = input[:-1]
	# ... otherswise leave input as is
	else:
		input = input

	
	# Parse the provided input
	dispatcher.input_parser(input)
	# Dispatch the instructions provided e.g. LRMMMLRMM
	dispatcher.dispatch_input()
	# After cleaning screen to avoid confusion ...
	os.system('clear')
	# ...print a message announcing final positions of rovers...
	print '   '
	print '*'*40
	print '*                                      *'
	print '*   FINAL POSITION(S) OF ROVER(S)      *'
	print '*                                      *'
	print '*'*40
	print '   '
	# ...along with positions themselves
	print dispatcher.display_output()



if __name__ == '__main__':
	main()
