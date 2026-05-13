favChai = [
    "Masala Chai",
    "Green tea",
    "lemon chai",
    "Elaichi Chai",
    "Green tea",
    "Masala Chai",
]

unique_chai = {chai for chai in favChai}

print(unique_chai)

recipes = {
    "Masala Chai": ["ginger", "cardamom", "clove"],
    "Elaichi Chai": ["cardamom", "milk"],
    "Spicy Chai": ["ginger", "black pepper", "clove"],
}

unique_spices = {spice for ingredients in recipes.values() for spice in ingredients}

print(unique_spices)