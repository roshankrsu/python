def infinite_chai():
    count = 1
    while True:
        yield f"Refil #{count}"
        count += 1

refill = infinite_chai()
user2 = infinite_chai()

for _ in range(7):
    print(next(refill))

for _ in range(4):
    print(next(user2))