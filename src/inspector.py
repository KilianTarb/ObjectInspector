import tkinter
from tkinter import ttk
from .config import inspector_config as i_config


class inspector():
	"""
	Object Inspector root window.
	"""

	def create_ui_components(self):
		""" 
		Initalises the root and it's components.
		"""

		self.root = tkinter.Tk()
		self.root.geometry("850x500")
		self.root.config(padx=i_config.ROOT_PADDING_X, pady=i_config.ROOT_PADDING_Y)
		self.root.title("Object Inspector")

		self.tab_control = tkinter.ttk.Notebook(self.root)

		self.create_frames()
		self.create_text_areas()
		self.create_buttons()

		self.tab_control.pack(expand=True, fill=tkinter.BOTH)

	def create_frames(self):
		"""
		Creates the widget containers.
		"""

		self.base_frame = tkinter.Frame(self.tab_control)
		self.base_frame.pack(side="top", expand=True, fill=tkinter.BOTH)

		self.txt_area_frame = tkinter.Frame(self.base_frame, bg="green")
		self.txt_area_frame.pack(side="top", expand=True, fill=tkinter.BOTH)

		self.btn_area_frame = tkinter.Frame(self.base_frame, bg="blue", height=i_config.BTN_FRAME_HEIGHT)
		self.btn_area_frame.pack(side="bottom", fill=tkinter.BOTH)

		self.tab_control.add(self.base_frame, text="Inspector")

	def add_data_tab(self):
		self.new_tab = tkinter.Frame(self.tab_control)
		self.new_tab.pack(fill=tkinter.BOTH, expand=True)

		self.new_tab_text = tkinter.Text(self.new_tab)
		self.new_tab_text.pack(expand=True, fill=tkinter.BOTH)

		self.tab_control.add(self.new_tab)

	def create_text_areas(self):
		"""
		Define and initalise the text areas.
		"""

		self.txt_input_area = tkinter.Text(self.txt_area_frame)
		self.txt_input_area.config(padx=i_config.TXT_PADDING_X, pady=i_config.TXT_PADDING_Y)
		self.txt_input_area.pack(expand=True, fill=tkinter.BOTH)

	def clear_txt_area(self):
		self.txt_input_area.delete("1.0", tkinter.END)

	def create_buttons(self):
		"""
		Define and initalise the buttons.
		"""

		self.submit_btn = tkinter.Button(self.btn_area_frame, text="Submit")
		self.submit_btn.config(width=i_config.BTN_WIDTH, height=i_config.BTN_HEIGHT, command=self.add_data_tab)
		self.submit_btn.pack(side="right", padx=i_config.BTN_PADDING_X, pady=i_config.BTN_PADDING_Y)

		self.clear_btn = tkinter.Button(self.btn_area_frame, text="Clear")
		self.clear_btn.config(width=i_config.BTN_WIDTH, height=i_config.BTN_HEIGHT, command=self.clear_txt_area)
		self.clear_btn.pack(side="right", padx=i_config.BTN_PADDING_X, pady=i_config.BTN_PADDING_Y)

	def __init__(self):
		self.create_ui_components()
		self.root.mainloop()
