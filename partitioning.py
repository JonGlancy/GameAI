import math

class Cell:
	def __init__(self, center, width, height):
		x,y = center
		top_left = [x - width/2, y + height/2]
		bottom_right = [x+width/2, y-height/2]
		self.members = []

	def addMember(self, member):
		self.members.append(member)

	def removeMember(self, member):
		self.members.remove(member)

class CellSpacePartition:
	def __init__(self, width, height, n):
		self.width = width
		self.height = height
		self.n = n

		self.cells = [[] for _ in xrange(n)]
		for i in xrange(n):
			for j in xrange(n):
				center = (i+0.5)*(width/n), (j+0.5)*(height/n)
				self.cells[i].append(Cell(center, width/n, height/n))
				self.cells[i][j].addMember(str(i)+', '+str(j))

	def getNeighbours(self, pos, radius):
		x, y = pos
		x_min, y_min = self.positionToIndex([x - radius,y - radius])
		x_max, y_max = self.positionToIndex([x + radius,y + radius])

		x_min, y_min = max(0, x_min), max(0, y_min)
		x_max, y_max = min(self.n-1, x_max), min(self.n-1, y_max)
		m_neighbours = []
		for i in xrange(x_min, x_max+1):
			for j in xrange(y_min, y_max+1):
				cell = self.cells[i][j]
				m_neighbours += cell.members
		return m_neighbours
	
	def positionToIndex(self, pos):
		x, y = pos
		i = math.floor(x * self.n / self.width)
		j = math.floor(y * self.n / self.height)
		return int(i),int(j)


grid = CellSpacePartition(100,100,10)
neighbours = grid.getNeighbours([20,20],10)
print neighbours,'-', len(neighbours), 'cells'
