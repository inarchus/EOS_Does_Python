from graphics import *


class WinLossTie:
	win = 3
	tie = 2
	loss = 1
	none = 0


def createMainWindow():
	window = GraphWin("TicTacToe Game", 750, 750)
	window.setBackground(color_rgb(0, 0, 0))

	return window


def setupGame(window, n):

	board = [['' for _ in range(n)] for _ in range(n)]

	for i in range(n):
		for j in range(n):
			r = Rectangle(Point(100 + 550 * i // n, 100 + 550 * j // n), Point(100 + 550 * (i + 1) // n, 100 + 550 * (j + 1) // n))
			r.setOutline('white')
			r.draw(window)

	return board


def checkForWin(board, player_symbol):
	"""
		:param the board is a two dimensional array, of the size of the board.  (3x3 to start)
		:return: WinLossTie.win if a win, tie if tie and loss if loss, else return WinLossTie.none
	"""
	n = len(board)

	computer_symbol = 'o' if player_symbol == 'x' else 'x'

	for row in range(n):
		win_scan = 0
		loss_scan = 0

		for col in range(n):
			if board[row][col] == player_symbol:
				win_scan += 1
			if board[row][col] == computer_symbol:
				loss_scan += 1
		if win_scan == n:
			return WinLossTie.win
		if loss_scan == n:
			return WinLossTie.loss

	for col in range(n):
		count = 0
		win_scan = 0
		loss_scan = 0

		for row in range(n):
			# counting for a tie
			if board[row][col] in [player_symbol, computer_symbol]:
				count += 1
			if board[row][col] == player_symbol:
				win_scan += 1
			if board[row][col] == computer_symbol:
				loss_scan += 1
		if win_scan == n:
			return WinLossTie.win
		if loss_scan == n:
			return WinLossTie.loss

	for i in range(n):
		win_scan = 0
		loss_scan = 0

		if board[i][i] == player_symbol:
			win_scan += 1
		if board[i][i] == computer_symbol:
			loss_scan += 1
	if win_scan == n:
		return WinLossTie.win
	if loss_scan == n:
		return WinLossTie.loss

	if n ** 2 == count:
		return WinLossTie.tie

	return WinLossTie.none


def drawMove(window, symbol, position):
	if symbol == 'x':
		pass
	elif symbol == 'o':


def computerMove(window, board, player_symbol, difficulty='easy'):
	pass


def playerMove(window, board, player_symbol):
	pt = window.getMouse()
	n = len(board)
	for i in range(n):
		for j in range(n):
			if 100 + 550 * i // n < pt.getX() < 100 + 550 * (i + 1) // n and 100 + 550 * j // n < pt.getY() < 100 + 550 * (j + 1) // n:
				if not board[i][j]:
					board[i][j] = player_symbol
				else:
					print('invalid move', i + 1, j + 1)


def playGame(window, board, n, player_symbol='x'):

	turn = 0

	while not checkForWin(board, player_symbol):
		if not turn % 2:
			if player_symbol == 'x':
				playerMove(window, board, player_symbol)
			else:
				computerMove(window, board, player_symbol)
		else:
			if player_symbol == 'o':
				playerMove(window, board, player_symbol)
			else:
				computerMove(window, board, player_symbol)

		turn += 1

	return checkForWin(board, player_symbol)


if __name__ == '__main__':
	main_window = createMainWindow()
	board = setupGame(main_window, 3)
	winner = playGame(main_window, board, 3)
	print(winner)
	print('click to close')
	main_window.getMouse()
