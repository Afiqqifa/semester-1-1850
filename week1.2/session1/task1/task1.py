# Week 1.2, Session 1: Task 1

# Create a shopping list

shopping = ["eggs", "milk", "flour", "carrots"]
print(shopping)

# We forgot something, so add it to list

shopping.append("bananas")
print(shopping)

# We bought something, so remove it from list

shopping.remove("eggs")
print(shopping)

# Replace bananas with grapes
indexitem=shopping.index("bananas")
shopping.insert(indexitem,"grapes")
shopping.remove("bananas")
print(shopping)

# Add yoghurt, just after milk
indexitem2=shopping.index("flour")
shopping.insert(indexitem2,"yoghurt")
print(shopping)