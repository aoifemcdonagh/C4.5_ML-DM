""" 
	Author: Aoife McDonagh
	ID Number: 13411348
	Script to perform Machine Learning using Gaussian Mixture Models
"""

import Tkinter as tk
import GMM_start 		# Import the python script containing the GMM code

class GMMApplication(tk.Frame):
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
		
		
		# Put an enter command that will run the GMM script with the correct proportion and csv file
		
def main():
	root = tk()
	root.geometry("250x150+300+300")
	app = GMMApplication(root)
	app.master.title('GMM GUI')
	app.mainloop()
	
if __name__ == '__main__':
	main()

