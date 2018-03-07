import sys
import random
### http://oldhome.schmorp.de/marc/pdb/index.html

class Point:
	# Init function
	def __init__(self, x = 0, y = 0):
		self.x = x
		self.y = y
	# String representation
	def __str__(self):
		return 'Point({},{})'.format(self.x, self.y)

class Dimension:
	# Init function
	def __init__(self, width = 0, height = 0):
		self.width = width
		self.height = height
	def center(self):
		return Point(self.width/2.0,self.height/2.0)
	# String representation
	def __str__(self):
		return 'Dimension({}x{})'.format(self.width, self.height)

class Rectangle:
	# Init function
	def __init__(self, x = 0 , y = 0, width = 0, height = 0):
		self.x = x
		self.y = y
		self.width = width
		self.height = height
	def center(self):
		return Point(self.x + self.width/2.0 , self.y + self.height/2.0)
	
	# String representation
	def __str__(self):
		return 'Rectangle({}x{})'.format(self.width, self.height)


def add(a,b):
	return a + b

class AbstractGimpPlugin:
	def name(self):
		return self.__class__.__name__
	def log(self, msg):
		sys.stderr.write( "[LOG][" + self.name() + "]" + str(msg) +"\n" )
	def drawing_bounds(self,image):
		exists, x1, y1, x2, y2 = gimp_selection_bounds (image)
		if not exists:
			return Rectangle(0,0,gimp_image_width(image),gimp_image_height(image))
		else:
			return Rectangle(x1,y2,x2-x1,y2-y1)
		
