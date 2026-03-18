# -------- LIST MANAGER --------
nums = [44, 12, 88, 5, 33, 88, 7]

# 1. Append 99
nums.append(99)
print(nums)

# 2. Insert 0 at index 2
nums.insert(2, 0)
print(nums)

# 3. Remove first 88
nums.remove(88)
print(nums)

# 4. Sort ascending
nums.sort()
print(nums)

# 5. Pop last item
nums.pop()
print(nums)

# 6. Count of 88
print("Count of 88:", nums.count(88))

# 7. Index of 33
print("Index of 33:", nums.index(33))


# -------- SET (UNIQUE VISITORS) --------
visitors = ["user1", "user2", "user1", "user3", "user2"]

unique_visitors = set(visitors)
print("Unique visitors:", unique_visitors)

# Check if a user visited
user = "user1"
print(user, "visited?" , user in unique_visitors)
