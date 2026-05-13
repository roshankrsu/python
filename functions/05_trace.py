def add_gst(price, gst_rate):
    return price + (100 * gst_rate)/100

orders = [100, 150, 200]

for price in orders:
    final_amount = add_gst(price, 18)
    print(f"orginal: {price}, final with gst {final_amount}")