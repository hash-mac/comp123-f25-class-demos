import timeit
import random

# --- Setup Parameters ---
# Number of elements in our data structures
DATA_SIZE = 10_000_000
# Number of times to repeat the test for better averaging
NUM_TRIALS = 10

# Create the data
keys_to_use = list(range(DATA_SIZE))
# Randomly select a key that we know exists for the lookup test
random_key = random.choice(keys_to_use)

# 1. Create a Dictionary and a List
data_dict = {k: f"value_{k}" for k in keys_to_use}
data_list = keys_to_use

# The list lookup will search for the key's index (itself)
# We need to find the index of the random_key in the list
list_lookup_value = random_key

print(f"--- Performance Comparison (Data Size: {DATA_SIZE:,}) ---")

# =======================================================
# Test 1: Element Lookup (Accessing an element)
# =======================================================
print("\n[TEST 1: Element Lookup]")

# --- Dictionary Lookup (O(1) average time complexity) ---
dict_lookup_code = f"x = data_dict[{random_key}]"
dict_time = timeit.timeit(
    stmt=dict_lookup_code,
    globals={'data_dict': data_dict, 'random_key': random_key},
    number=NUM_TRIALS
)
print(f"Dictionary Time (Lookup): {dict_time / NUM_TRIALS:.6f} seconds/trial")

# --- List Lookup (O(n) average time complexity for searching by value) ---
list_lookup_code = f"x = data_list.index({list_lookup_value})"
# NOTE: list.index() must scan the list until it finds the value, which is O(n)
list_time = timeit.timeit(
    stmt=list_lookup_code,
    globals={'data_list': data_list, 'list_lookup_value': list_lookup_value},
    number=NUM_TRIALS
)
print(f"List Time (Lookup by Value): {list_time / NUM_TRIALS:.6f} seconds/trial")

# =======================================================
# Test 2: Element Insertion (Adding an element)
# =======================================================
print("\n[TEST 2: Element Insertion]")
new_key = DATA_SIZE + 1 # Key guaranteed not to exist yet

# --- Dictionary Insertion (O(1) average time complexity) ---
dict_insert_code = f"data_dict[{new_key}] = 'new_value'"
dict_time_insert = timeit.timeit(
    stmt=dict_insert_code,
    globals={'data_dict': data_dict, 'new_key': new_key},
    number=NUM_TRIALS
)
print(f"Dictionary Time (Insertion): {dict_time_insert / NUM_TRIALS:.6f} seconds/trial")

# --- List Insertion (O(1) average for append(), but O(n) for insert(0, ...) or insert(n/2, ...) ---
# We'll use list.append(), which is the most common and fastest insertion ($O(1)$ amortized)
list_insert_code = f"data_list.append({new_key})"
list_time_insert = timeit.timeit(
    stmt=list_insert_code,
    globals={'data_list': data_list, 'new_key': new_key},
    number=NUM_TRIALS
)
print(f"List Time (Append): {list_time_insert / NUM_TRIALS:.6f} seconds/trial")

# --- List Insertion at Start (Worst-case insertion is O(n)) ---
# This is slow because all existing elements must be shifted.
list_insert_start_code = f"data_list.insert(0, {new_key})"
list_time_insert_start = timeit.timeit(
    stmt=list_insert_start_code,
    globals={'data_list': data_list, 'new_key': new_key},
    number=NUM_TRIALS
)
print(f"List Time (Insert at Start (Worst Case)): {list_time_insert_start / NUM_TRIALS:.6f} seconds/trial")
