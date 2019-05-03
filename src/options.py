import sys

class Options:

	##
	#	Constructor:
	#	Set up default options and check if an option was passed as an argument
	# through the command line
	#
	def __init__(self):
		self.default_option = '--iata'
		self.options = [
			'--help',
			'--cities',
			'--coords',
			'--iata',
			'--names',
			'--full'
		]

		args = sys.argv
		
		if len(args) > 1:
			if len(args) > 2:
				self.configureMultipleOptions(args)
			else:	
				self.configureOption(args[1])
		else:
			self.configureOption(None)
	
	## 
	# Method that configures program options based on arguments
	# passed in the command line
	#
	def configureOption(self, option):
		if option not in self.options or option == None:
			self.selected_option = self.default_option
			return 0

		self.selected_option = option
		return 1


	## 
	# Same as configureOption() but used when executing
	# the main script with multiple arguments
	#
	def configureMultipleOptions(self, options):
		options = options[1:] # Remove 'main.py' from args
		for option in options:
			if option not in self.options:
				self.selected_option = self.default_option
				return 0

		self.selected_option = list(options)
		return 1

	
	##
	# Command line arguments getter
	#
	@staticmethod
	def get_args():
		return sys.argv



