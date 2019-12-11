import tkinter

# Main application window
class Inspector():
	windowPaddingX = 10
	windowPaddingY = 10

	buttonFrameHeight = 300
	buttonWidth = 15
	buttonHeight = 1
	buttonPaddingX = 5
	buttonPaddingY = 5

	textInputAreaPaddingX = 50
	textInputAreaPaddingY = 25

    # Initalises the window and it's components
	def CreateUIComponents(self):
		self.window = tkinter.Tk()
		self.window.geometry("850x500")
		self.window.config(padx=self.windowPaddingX, pady=self.windowPaddingY)
		self.window.title("Object Inspector")

		self.CreateFrames()
		self.CreateTextAreas()
		self.CreateButtons()


	def CreateFrames(self):
		# Create frames
		self.inspectorAreaFrame = tkinter.Frame(self.window, bg="red")
		self.inspectorAreaFrame.pack(side="top", expand=True, fill=tkinter.BOTH)

		self.textAreaFrame = tkinter.Frame(self.window, bg="green")
		self.textAreaFrame.pack(side="top", expand=True, fill=tkinter.BOTH)

		self.buttonAreaFrame = tkinter.Frame(self.window, bg="blue", height=self.buttonFrameHeight)
		self.buttonAreaFrame.pack(side="bottom", fill=tkinter.BOTH)
	

	def CreateTextAreas(self):
		self.textInputArea = tkinter.Text(self.textAreaFrame)
		self.textInputArea.config(padx=self.textInputAreaPaddingX, pady=self.textInputAreaPaddingY)
		self.textInputArea.pack(expand=True, fill=tkinter.BOTH)


	def CreateButtons(self):
		# Create buttons
		self.submitBtn = tkinter.Button(self.buttonAreaFrame, text="Submit")
		self.submitBtn.config(width=self.buttonWidth, height=self.buttonHeight)
		self.submitBtn.pack(side="right", padx=self.buttonPaddingX, pady=self.buttonPaddingY)

		self.clearBtn = tkinter.Button(self.buttonAreaFrame, text="Clear")
		self.clearBtn.config(width=self.buttonWidth, height=self.buttonHeight)
		self.clearBtn.pack(side="right", padx=self.buttonPaddingX, pady=self.buttonPaddingY)



	def __init__(self):
		self.CreateUIComponents()
		self.window.mainloop()
