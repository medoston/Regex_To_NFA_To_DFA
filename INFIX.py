
class InfixConversion:

#-----------------------------------------------------------
#--------------initializing the class variables..-----------
	def __init__(self, regular_exp_len):
		self.top = -1
		self.capacity = regular_exp_len
		#------setting the stack array-----
		self.array = []
		#------setting priority------------
		self.output = []
		self.priority = {'|': 1, '*': 3, '.': 2}
#-----------------------------------------------------------

#-----------------------------------------------------------
#---------checking if the top arr if it's empty-------------
	def check_Empty(self):
		# return True if the stack is empty
		if self.top == -1: 
			check=True
		else:
			check=False

		return check
#-----------------------------------------------------------

#-----------------------------------------------------------
	#function that returns the last element of the stack
	def pop(self):
		if not self.check_Empty():
			self.top -= 1
			return self.array.pop()
		else:
			return "$"
#-----------------------------------------------------------

#-----------------------------------------------------------
	# Push the elements to the stack
	def stk_push(self, op):
		self.top += 1
		self.array.append(op)
#-----------------------------------------------------------

#-----------------------------------------------------------
	# function that checks if the element is alphabitic (a~z)
	def alpha_check(self, ch):
		return ch.isalpha()
#-----------------------------------------------------------

#-----------------------------------------------------------
	#checks if the priority of the operator is less than
	#the top of the stack or not
	def Priority_top_check(self, i):
		try:
			priority_operator = self.priority[i]
			top_stack = self.priority[self.check_top()]

			if priority_operator <= top_stack:
				return True
			else:
				return False
		except KeyError:
			return False
#-----------------------------------------------------------

#-----------------------------------------------------------
	#function that returns the value on the top of the stack
	def check_top(self):
		return self.array[-1]
#-----------------------------------------------------------

#-----------------------------------------------------------
	def INFIX(self, exp):
		for i in exp:
			# If the character is an operand,
			# add it to output
			if self.alpha_check(i):
				self.output.append(i)

			# If the character is an '(', push it to stack
			elif i == '(':
				self.stk_push(i)
			# If the scanned character is an ')' pop until '(' 
			elif i == ')':
				while((not self.check_Empty()) and
					self.check_top() != '('):
					a = self.pop()
					self.output.append(a)
				if (not self.check_Empty() and self.check_top() != '('):
					return -1
				else:
					self.pop()

			else:
				while(not self.check_Empty() and self.Priority_top_check(i)):
					# pass cases like a^b^c
					if i == "." and self.array[-1] == i:
						break
					self.output.append(self.pop())
				self.stk_push(i)

		# pop all the operator from the stack
		while not self.check_Empty():
			self.output.append(self.pop())
		out = "".join(self.output)
		return out
#-----------------------------------------------------------
