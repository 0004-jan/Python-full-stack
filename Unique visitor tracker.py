visitors = ["alice", "bob", "alice", "carol", "bob", "dave", "alice"]

# 1. Total visits
print("Total visits:", len(visitors))

# 2. Unique visitors
unique = set(visitors)
print("Unique visitors:", unique)

# 3. Count of unique visitors
print("Unique count:", len(unique))

# 4. Check if "eve" visited
print("Did eve visit?", "eve" in unique)

# 5. Check if "bob" visited
print("Did bob visit?", "bob" in unique)
