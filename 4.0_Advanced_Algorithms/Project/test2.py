from queue import PriorityQueue



q  = PriorityQueue()

q.put((2,'Gabriel'))
q.put((1,'Oduori'))
q.put((3,'Sleep'))  



while not q.empty():
    next_item = q.get()
    print(next_item)