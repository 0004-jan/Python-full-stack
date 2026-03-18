alice_friends = {"bob", "carol", "dave", "eve"}
bob_friends = {"carol", "frank", "eve", "grace"}

# 1. Mutual friends
print("Mutual friends:", alice_friends & bob_friends)

# 2. All unique people
print("All friends:", alice_friends | bob_friends)

# 3. Alice's friends but not Bob's
print("Only Alice's friends:", alice_friends - bob_friends)

# 4. Check if "dave" is in Bob's list
print("Is dave in Bob's friends?", "dave" in bob_friends)
