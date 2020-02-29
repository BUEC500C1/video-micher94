

# levereged from https://runestone.academy/runestone/books/published/pythonds/BasicDS/ImplementingaQueueinPython.html
class Queue:
	def __init__(self):
		self.items = []

	def isEmpty(self):
		return self.items == []

	def queueup(self, item):
		self.items.append(item)

	def queuedown(self):
		return self.items.pop(0)

	def queuelength(self):
		return len(self.items)

	def queuelist(self):
		for item in self.items:
			print(item)