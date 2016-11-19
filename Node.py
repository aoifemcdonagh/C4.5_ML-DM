"""
	Author: Aoife McDonagh
	ID Number: 13411348
	Class: 4BP
	
	Class for Nodes in a decision tree.
"""

class Node:
	"""
	Function to initialise a node
	Parameters:
		@data:			All data points underneath this node.
		@parent_node: 	Node which is directly above this node object
		@subnodes: 		A list of subnodes belonging to the node.
		@attribute:		Attribute that splits the node
		@result: 		Result at this particular node. This will be None for non-leaf nodes, not None for leaf nodes.
	"""
	def __init__(data = None, parent_node = None, subnodes = None, attribute = None, result=None):
		self.data = data
		self.parent_node = parent_node
		self.subnodes = subnodes
		self.attribute = attribute
		self.result = result
		
		if self.check_base_cases == True:	# check if base cases are satisfied
			self.make_leaf_node()			# make the node a leaf node
		else: 								# if they are not satisfied, split node on an attribute
	
	
	"""
	Function that checks if any of the base cases are satisfied
	Returns 1 if any case is satisfied
	Returns 0 if all cases are unsatisfied.
	
	The appropriate actions are taken within this function for any case that is satisfied.
	This means that the function calling it does not have to implement code in response to
	a satisfied base case.
	"""	
	def check_base_cases():
		satisfied = False;					# initial instantiation of variable representing if any cases are satisfied
		# are all the data points in the same class?
		
		# do no attributes provide any info gain?
		
		# is an unseen class encountered?
		
		return satisfied
		
		
	"""
	Function to split the node's dataset into subnodes on the condtion that no base cases are satisfied.
	Involves the recursive instantiation of sub nodes.
	All sub nodes will have this node as a parent
	"""
	def split():
	
	
	"""
	Function to print the node 
	Recursively prints all of its child nodes
	"""
	def print_node():
		# some printing of the nodes own information
		
		for node in subnodes:				# recursively print the info for all sub nodes
			node.print_node()

	
	"""
	Function that makes this node a leaf node.
	Need to give a value to @result variable
	"""
	def make_leaf_node():
		
	