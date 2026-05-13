def serve_order():
    yield "order 1: Burger"
    yield "order 2: Spring roll"
    yield "order 3: Momos"

stall = serve_order()

# for order in stall:
#     print(order)

def  get_order_list():
    return ["order 1", "order 2", "order 3"]

# generator function

def get_order_gen():
    yield "order 1"
    yield "order 2"
    yield "order 3"

order = get_order_gen()
print(next(order))
print(next(order))
print(next(order))