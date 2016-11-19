"""
	Author: Aoife McDonagh
	ID Number: 13411348
	Class: 4BP
	
	This script contains the GUI code and starts the application.
	It allows selection of a dataset. 
	Preprocessing of the dataset occurs here.
"""

import Tkinter as tk
import DecisionTree # Import the decision tree script

class C45Application(tk.Frame):
	def __init__(self, master = None):
		tk.Frame.__init__(self, master, background="white")
		self.grid()
		self.setupGUI()
		
	def setupGUI(self):
		self.quitButton = tk.Button(self, text='Quit', command=self.quit)
		self.quitButton.grid()
		
		# Put a text box for user input (proportions, csv file)
		e = Entry(self)
		e.pack()
		
		# need command that partitions the dataset once the CSV file is selected
		# i.e. calling the partition_dataset function
		
		# put an enter command that will start the creation of a decision tree
		
		# button that will print the decision tree, calling the decision tree's print_tree() function

	"""
	Function that performs preprocessing and partitioning of the dataset.
	"""		
def partition_dataset(location, training_proportion):
	dataset = genfromtxt(location, delimiter =',', dtype = None) # Read data in from CSV file
	numpy.random.shuffle(dataset) # Shuffle the dataset
	
	cutoff = int(dataset.size*training_proportion) # Point which splits the training and testing data
	training_data, testing_data = dataset[:cutoff], dataset[cutoff:] # instantiate training, testing datasets
	
	print("\n\nTraining Data: \n\n")
	print(training_data)
	
	print("\n\nTesting Data: \n\n")
	print(testing_data)
		
def main():
	root = tk()
	root.geometry("250x150+300+300")
	app = C45Application(root)
	app.master.title('C4.5 GUI')
	app.mainloop()
	
if __name__ == '__main__':
	main()

