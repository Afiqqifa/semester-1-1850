# Week 1.6, Session 1: Task 5

# Write a program here that uses the QuakeFeed and QuakeDataset
# classes to download earthquake data from a USGS data feed,
# analyze it and display the results

# See README.md for full details of what is required and what
# program output should look like
from feed import QuakeFeed
from dataset import QuakeDataset

level=input("Enter a feed level (e.g., 'significant', '4.5', '2.5', '1.0'): ")
period=input("Enter a feed period (e.g., 'hour', 'day', 'week', 'month'): ")

feed=QuakeFeed(level,period)
dataset=QuakeDataset(feed)
dataset.read_feed()

print(f"Dataset contains {len(dataset)} quakes from feed: {feed}")
print(f"Mean depth: {dataset.mean_depth():.2f} km")
print(f"Mean magnitude: {dataset.mean_magnitude():.2f}")

strongest_quake=dataset.strongest_quake()
shallowest_quake=dataset.shallowest_quake()
print(f"Strongest quake: {strongest_quake.when}")
print(f"Shallowest quake: {shallowest_quake.when}")
print(f"Magnitude of strongest quake: {strongest_quake.magnitude}")
print(f"Depth of strongest quake: {strongest_quake.depth} km")
print(f"Magnitude of shallowest quake: {shallowest_quake.magnitude}")
print(f"Depth of shallowest quake: {shallowest_quake.depth} km")