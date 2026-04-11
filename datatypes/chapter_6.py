chai_type = "Iced Tea"
customer_name = "ros"

print(f"Order for {customer_name} : {chai_type} please !")

chai_description = "Aromatic and Bold"
print(f"First word: {chai_description[:8]}")
print(f"Last word: {chai_description[12:]}")
print(f"reversef word: {chai_description[::-1]}")

label_text = "Chai Special"
encoded_label = label_text.encode("utf-8")
print(f"Non Encoded label: {label_text}")
print(f"Encoded label: {encoded_label}")
decode_label = encoded_label.decode("utf-8")
print(f"Decoded label: {decode_label}")