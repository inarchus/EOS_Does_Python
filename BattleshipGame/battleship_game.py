import tkinter as tk


class BattleshipGame:
	board_size = 10
	
	def __init__(self):
		pass
	
	def user_move(self, i, j):
		pass
	
	def get_computer_move(self):
		pass
	
	def check_win_state(self):
		pass
	
	def x(self):
		pass


class BattleshipWindow(tk.Tk):
	def __init__(self):
		super().__init__()
		self.geometry('800x800')
		self.title('Battleship!')
		self.create_menu()
		self.create_game_canvas()
	
	def create_menu(self):
		menu_bar = tk.Menu(self)
		main_menu = tk.Menu(self, tearoff=0)
		menu_bar.add_cascade(label='Game', menu=main_menu)
		main_menu.add_command(label='New Game', command=self.new_game)
		main_menu.add_command(label='Exit Game', command=self.destroy)
		self.config(menu=menu_bar)
		
	def create_game_canvas(self):
		pass
	
	def draw_game_state(self):
		pass
	
	def new_game(self):
		pass


battleship_window = BattleshipWindow()
battleship_window.mainloop()
