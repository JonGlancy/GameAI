import math, random

class Cave:
	def __init__(self, width, height):
		self.width = width
		self.height = height
		self.state = [[int(random.random()<0.40) for _ in range(height)] for _ in range(width)]

	def __str__(self):
		board = ''
		for row in [list(i) for i in zip(*self.state)]:
			for ele in row:
				if ele == 1:
					board += '#'
				else:
					board += '.'
			board += '\n'
		return board


	def neighbours(self, cell, n):
		x, y = cell
		for i in range(-n, n+1):
			for j in range(-n, n+1):
				yield x+i, y+j

	def count(self, cell, n):
		living_neighbours = 0
		for x, y in self.neighbours(cell, n):
			if x<0 or x>=self.width or y<0 or y>=self.height:
				#off the map
				living_neighbours += 2
			else:
				living_neighbours += self.state[x][y]
		return living_neighbours

	def phase1(self, t):
		for _ in range(t):
			next_state = [[0]*self.height for _ in range(self.width)]
			for x in range(self.width):
				for y in range(self.height):
					cell = (x,y)
					wall_count_1 = self.count(cell, 1)
					wall_count_2 = self.count(cell, 2)
					if wall_count_1 >= 5 or wall_count_2 <=3:
						next_state[x][y] = 1
					else: 
						next_state[x][y] = 0
			self.state = next_state

	def phase2(self, t):
		for _ in range(t):
			next_state = [[0]*self.height for _ in range(self.width)]
			for x in range(self.width):
				for y in range(self.height):
					cell = (x,y)
					wall_count_1 = self.count(cell, 1)
					if wall_count_1 >= 5:
						next_state[x][y] = 1
					else: 
						next_state[x][y] = 0
			self.state = next_state

	def generate(self):
		self.state = [[int(random.random()<0.40) for _ in range(self.height)] for _ in range(self.width)]
		self.phase1(4)
		self.phase2(3)

		
if __name__ == '__main__':
	cave = Cave(50,50)
	cave.generate()
	print cave

