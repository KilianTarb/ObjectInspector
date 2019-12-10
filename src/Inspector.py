import tkinter

# Main application window


class Inspector():
	buttonWidth = 15
	buttonHeight = 1

    # Initalises the window and it's components
	def CreateUIComponents(self):
		self.window = tkinter.Tk()
		self.window.title("Object Inspector")

		# Create frames
		self.textAreaFrame = tkinter.Frame(self.window)
		self.textAreaFrame.pack(side="top")
		self.buttonAreaFrame = tkinter.Frame(self.window)
		self.buttonAreaFrame.pack(side="bottom")

		# Create buttons
		self.submitBtn = tkinter.Button(self.window, text="Submit")
		self.submitBtn.config(width=self.buttonWidth, height=self.buttonHeight)
		self.submitBtn.pack(side="right")
		self.clearBtn = tkinter.Button(self.window, text="Clear")
		self.clearBtn.config(width=self.buttonWidth, height=self.buttonHeight)
		self.clearBtn.pack(side="right")

		# Start loop
		self.window.mainloop()

	def __init__(self):
		self.CreateUIComponents()
