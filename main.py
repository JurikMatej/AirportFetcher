from src.api import Api
from src.options import Options 
import sys

##
# Execute the program based on the option given by user
#
def main():
	options = Options()
	opt = options.selected_option

	# Main decision tree

	# Single argument given
	if type(opt) is str:
		if opt == '--help':
			help()

		elif opt == '--cities':
			Api.get_cities()
			# more_info()
		
		elif opt == '--coords':
			Api.get_coords()
			# more_info()

		elif opt == '--iata':
			Api.get_iata()
			# more_info()

		elif opt == '--names':
			Api.get_names()
			# more_info()

		elif opt == '--full':
			Api.get_full()
			# more_info()

	# Multiple arguments 
	elif type(opt) is list:
		# If --help is given as an argument with any other
		# arguments, print out just the help message
		if '--help' in opt:
			help()

		# If --full is given as an argument with any other 
		# arguments, use the convenient get_full() Api method
		elif '--full' in opt:
			Api.get_full()

		else:
			Api.get_mixed(opt)


##
# Print out base information about program 
# and how to use it
#
def help():
	print('\n\nA python program that fetches data about airports in the United Kingdom from the Kiwi Locations API. ')
	print('Author: Matej Jurík, Pegas I.T.')
	print('------------------------------')
	print('How to use: ')
	print('	Use one of the options specified below to get wanted output:')
	print('	"python main.py --cities" for cities with airports')
	print('	"python main.py --coords" for coordinates of each airport')
	print('	"python main.py --iata"   for IATA codes')
	print('	"python main.py --names"  for names of the airport')
	print('	"python main.py --full"   to print every detail from each airport')
	print('\nAll data is formatted in JSON')


##
# Let user know where to look for info about 
# this program
#
def more_info():
	print('Run "python main.py --help" for more information')


# Run program
if __name__ == "__main__":
	main()
