from collections import deque

dq = deque(range(10), maxlen=10)
print(dq)

dq.rotate(3)
print(dq)

dq.rotate(-4)
print(dq)

dq.appendleft(-1)
print(dq)

