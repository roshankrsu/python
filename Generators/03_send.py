def order_food():
    print("Welcome ! What would you like to order ?")
    order = yield 
    while True:
        print(f"Preparing: {order}")
        order = yield

stall = order_food()
next(stall) # start the generator

stall.send("Burger")
stall.send("Tiramisu")
