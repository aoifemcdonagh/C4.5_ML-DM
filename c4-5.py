"""
	Author: Aoife McDonagh
	ID Number: 13411348
	Class: 4BP
	
	This script implements the C4.5 classification algorithm created by Ross Quinlan.
	It creates decision trees to classify data and prints them out.
"""

import numpy
import math

def partition_dataset(location, training_proportion):
	dataset = genfromtxt(location, delimiter =',', dtype = None) # Read data in from CSV file
	numpy.random.shuffle(dataset) # Shuffle the dataset
	
	cutoff = int(dataset.size*training_proportion) # Point which splits the training and testing data
	training_data, testing_data = dataset[:cutoff], dataset[cutoff:] # instantiate training, testing datasets
	
	print("\n\nTraining Data: \n\n")
	print(training_data)
	
	print("\n\nTesting Data: \n\n")
	print(testing_data)
	
def check_base_cases(): # check if any base cases have been satisfied.
 	
	
def calculate_entropy():
	

def main():
	csvfile = sys.argv[1] 

if __name__ == "__main__":
	main() # Execute main function