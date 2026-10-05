# Week 1.2, Session 1: Task 5

prices={"apple":21,"orange":30,"banana":45}
print(prices["apple"])
prices["apple"]=25
print(prices["apple"])

prices["kiwi"]=55
print(prices)





rivers = {
    "London": "Thames",
    "Leeds": "Aire",
    "Liverpool": "Mersey"
}

print(rivers)

# Add two new entries to the rivers database
rivers["Cairo"]="Nile"
rivers["Sarawak"]="Rajang"
print(rivers)

# Display all the keys
print(rivers.keys())

# Display all the values
print(rivers.values())

# Display all the key:value pairs, as tuples
print(rivers.items())

# Delete an entry from the rivers database
rivers.pop("Sarawak")
print(rivers)