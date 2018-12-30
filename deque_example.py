# Import double ended queue, last in first out.
from collections import deque

# Create a queue with maximum length of 10.
dq = deque(range(10), maxlen=10)
print(dq)

# Rotate the queue 3 times.
dq.rotate(3)
print(dq)

# Rotate the queue backwards 4 times.
dq.rotate(-4)
print(dq)

# Append to the left side of the queue.
dq.appendleft(-1)
print(dq)

# Extend the end of the queue, pushes from the right.
dq.extend([11, 22, 33])
print(dq)

# Extend the left of the queue, pushes from the left.
dq.extendleft([10, 20, 30, 40])
print(dq)