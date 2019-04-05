from graphics import *


def createMainWindow():
	main_window = GraphWin("Battleship Game", 1500, 750)
	main_window.setBackground(color_rgb(0, 0, 0))

	return main_window


if __name__ == '__main__':
	createMainWindow().getMouse()

