import tkinter


class inspector():
	"""
	Object Inspector root window.
	"""

	root_padding_x = 10
	root_padding_y = 10

	btn_frame_height = 300
	btn_width = 15
	btn_height = 1
	btn_padding_x = 5
	btn_padding_y = 5

	txt_padding_x = 10
	txt_padding_y = 10

	def create_ui_components(self):
		""" 
		Initalises the root and it's components.
		"""

		self.root = tkinter.Tk()
		self.root.geometry("850x500")
		self.root.config(padx=self.root_padding_x, pady=self.root_padding_y)
		self.root.title("Object Inspector")
	
		

		self.create_frames()
		self.create_text_areas()
		self.create_buttons()

	def create_frames(self):
		"""
		Creates the widget containers.
		"""

		self.txt_area_frame = tkinter.Frame(self.root, bg="green")
		self.txt_area_frame.pack(side="top", expand=True, fill=tkinter.BOTH)

		self.btn_area_frame = tkinter.Frame(self.root, bg="blue", height=self.btn_frame_height)
		self.btn_area_frame.pack(side="bottom", fill=tkinter.BOTH)

	def create_text_areas(self):
		"""
		Define and initalise the text areas.
		"""

		self.txt_input_area = tkinter.Text(self.txt_area_frame)
		self.txt_input_area.config(padx=self.txt_padding_x, pady=self.txt_padding_y)
		self.txt_input_area.pack(expand=True, fill=tkinter.BOTH)

	def create_buttons(self):
		"""
		Define and initalise the buttons.
		"""
		
		self.submit_btn = tkinter.Button(self.btn_area_frame, text="Submit")
		self.submit_btn.config(width=self.btn_width, height=self.btn_height)
		self.submit_btn.pack(side="right", padx=self.btn_padding_x, pady=self.btn_padding_y)

		self.clear_btn = tkinter.Button(self.btn_area_frame, text="Clear")
		self.clear_btn.config(width=self.btn_width, height=self.btn_height)
		self.clear_btn.pack(side="right", padx=self.btn_padding_x, pady=self.btn_padding_y)

	def __init__(self):
		self.create_ui_components()
		self.root.mainloop()
