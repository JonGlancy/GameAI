import math, random, timeit

class CellSpacePartition:
	def __init__(self, width, height, n):
		self.width = width
		self.height = height
		self.n = n

		self.cells = [[[] for _ in xrange(n)] for _ in xrange(n)]

	def positionToIndex(self, pos):
		x, y = pos
		i = math.floor(x * self.n / self.width)
		j = math.floor(y * self.n / self.height)
		return int(i),int(j)

	def getNeighbours(self, pos, radius):
		x, y = pos
		x_min, y_min = self.positionToIndex([x - radius,y - radius])
		x_max, y_max = self.positionToIndex([x + radius,y + radius])

		x_min, y_min = max(0, x_min), max(0, y_min)
		x_max, y_max = min(self.n-1, x_max), min(self.n-1, y_max)
		m_neighbours = []
		for i in xrange(x_min, x_max+1):
			for j in xrange(y_min, y_max+1):
				m_neighbours += self.cells[i][j]
		return m_neighbours

class MovingEntity:
	def __init__(self, pos, grid):
		self.pos = pos
		self.grid = grid
		i,j = self.grid.positionToIndex(pos)
		self.index = (i,j)
		self.grid.cells[i][j].append(self)

	def update(self):
		new_index = self.grid.positionToIndex(self.pos)
		if new_index != self.index:
			old_cell = self.grid.cells[self.index[0]][self.index[1]]
			new_cell = self.grid.cells[new_index[0]][new_index[1]]

			old_cell.remove(self)
			old_cell.append(self)

if __name__ == '__main__':

	n_agents = 2000
	n_cells  = 10

	def dist_squared(vec1, vec2):
		x1, y1 = vec1
		x2, y2 = vec2
		return (x2-x1)**2 + (y2-y1)**2

	def test1():
		total = 0
		radius = 5
		for agent in agents:
			neighbours = agent.grid.getNeighbours(agent.pos, radius)
			for other in neighbours:
				if agent!=other:
					if dist_squared(agent.pos, other.pos) < radius:
						total += 1
			agent.update()
		print total

	def test0():
		total = 0
		radius = 5
		for agent in agents:
			for other in agents:
				if agent!=other:
					if dist_squared(agent.pos, other.pos) < radius:
						total += 1
			agent.update()
		print total

	grid = CellSpacePartition(100,100,n_cells)

	agents = []
	for _ in xrange(n_agents):
		pos = [random.random()*100, random.random()*100]
		agents.append(MovingEntity(pos, grid))

	repeats = 1
	print str(n_agents) + ' agents'
	print str(n_cells**2) + ' grid cells'
	print str(timeit.Timer(test0).timeit(number=repeats)/repeats)+'s without partitioning'
	print str(timeit.Timer(test1).timeit(number=repeats)/repeats)+'s with partitioning'
