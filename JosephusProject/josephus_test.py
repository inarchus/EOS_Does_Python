import tkinter as tk
import random
from threading import Thread


class JosephusThread(Thread):
	def __init__(self, jt):
		super().__init__()
		self.test = jt
	
	def run(self):
		if self.test.candidate:
			for i, (n, k) in enumerate(self.test.test_input):
				self.test.answers[i] = self.test.josephus(n, k)
				if self.test.candidate(n, k) == self.test.josephus(n, k):
					self.test.cell[i]['background'] = 'green'
				else:
					self.test.cell[i]['background'] = 'red'


class JosephusTest(tk.Tk):
	
	def __init__(self, candidate_function):
		super().__init__()
		self.geometry('1300x300')
		self.title('Josephus Test')
		self.candidate = candidate_function
		
		self.j_thread = JosephusThread(self)
		self.bottom_frame = tk.Frame(self)
		self.run_button = tk.Button(self.bottom_frame, text='Run Test', command=self.j_thread.start)
		self.answer_label = tk.Label(self.bottom_frame, text='')
		
		self.red_green_frame = tk.Frame(self)
		self.test_input = [(random.randint(2, 250), random.randint(2, 250)) for _ in range(100)]
		self.answers = [-1 for _ in range(100)]
		self.cell = [tk.Button(self.red_green_frame, background='grey', text='Test %i, n=%i, k=%i' % ((i + 1), self.test_input[i][0], self.test_input[i][1]), command=lambda index=i: self.display_answer(index) ) for i in range(100)]
		
		for i in range(100):
			self.cell[i].grid(row=i // 10, column= i % 10, sticky='news')

		self.run_button.pack(side=tk.LEFT)
		self.answer_label.pack(side=tk.RIGHT)
		self.bottom_frame.pack(side=tk.BOTTOM, fill='x')
		self.red_green_frame.pack(fill=tk.BOTH, expand=True)
		
	def display_answer(self, i):
		if self.answers[i] == -1:
			self.answers[i] = self.josephus(*self.test_input[i])
		self.answer_label['text'] = 'The survivor is: ' + str(self.answers[i])

	def runTest(self):
		if self.candidate:
			for i, (n, k) in enumerate(self.test_input):
				if self.candidate(n, k) == self.josephus(n, k):
					self.cell[i]['background'] = 'green'
				else:
					self.cell[i]['background'] = 'red'
		
	@staticmethod
	def josephus(n, k):
		k %= n
		
		eliminations = 0
		current = 0
		soldiers = [True for _ in range(n)]
		
		while eliminations < n - 1:
			i = 0
			count = 0
			while count < k:
				if soldiers[(i + current) % n]:
					count += 1
				i += 1
				
			i -= 1
			current = (i + current) % n
			soldiers[current] = False
			eliminations += 1

		return soldiers.index(True)

try:
	import josephus
	test = JosephusTest(josephus.josephus)
	test.mainloop()
except ImportError:
	print('There was an import error, make sure the file is in the right place with the name josephus.py')
	
