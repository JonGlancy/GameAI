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

	def addMember(self, entity):
		i,j = self.positionToIndex(entity.position)
		entity.index = (i,j)
		self.cells[i][j].append(entity)

class BaseEntity:
	def __init__(self, position, grid):
		self.position = position
		self.grid = grid
		self.grid.addMember(self)

	def update(self):
		pass

class MovingEntity(BaseEntity):
	def update(self):
		new_index = self.grid.positionToIndex(self.position)
		if new_index != self.index:
			old_cell = self.grid.cells[self.index[0]][self.index[1]]
			new_cell = self.grid.cells[new_index[0]][new_index[1]]

			old_cell.remove(self)
			old_cell.append(self)

if __name__ == '__main__':

	n_agents = 5000
	n_cells  = 15

	def dist_squared(vec1, vec2):
		x1, y1 = vec1
		x2, y2 = vec2
		return (x2-x1)**2 + (y2-y1)**2

	def test1():
		total = 0
		radius = 5
		for agent in agents:
			neighbours = agent.grid.getNeighbours(agent.position, radius)
			for other in neighbours:
				if agent!=other:
					if dist_squared(agent.position, other.position) < radius:
						total += 1
			agent.update()

	def test0():
		total = 0
		radius = 5
		for agent in agents:
			for other in agents:
				if agent!=other:
					if dist_squared(agent.position, other.position) < radius:
						total += 1
			agent.update()

	grid = CellSpacePartition(100,100,n_cells)

	agents = []
	for _ in xrange(n_agents):
		pos = [random.random()*100, random.random()*100]
		agents.append(MovingEntity(pos, grid))

	repeats = 10
	print str(n_agents) + ' agents'
	print str(n_cells**2) + ' grid cells'
	a = timeit.Timer(test0).timeit(number=repeats)/repeats
	b = timeit.Timer(test1).timeit(number=repeats)/repeats
	print a, b, a/b