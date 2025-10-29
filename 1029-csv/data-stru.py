def print_ds_details(msg, ds):
    print()
    print(msg)
    print(type(ds))

    if type(ds) is dict:
        for k, v in ds.items():
            print("\t", type(k), type(v))

        return

    for i in ds:
        print("\t", type(i))


# a list of numbers
ln = [1, 2, 3, 4]
print_ds_details("list of numbers", ln)

# a list of lists
ll = [[1, 2], [3, 4]]
print_ds_details("list of lists", ll)

# a list of tuples
lt = [(1, 2), (3, 4)]
print_ds_details("list of tuples", lt)

# a list of sets
ls = [{1, 2}, {3, 4}]
print_ds_details("list of sets", ls)

# a list of dictionaries
ld = [{1: 2}, {3: 4}]
print_ds_details("list of dictionaries", ld)

# a list of mix of above
lnd = [1, (2,), {3}, {4: 5}]
print_ds_details("list of mix of above", lnd)

# a dictionary of lists
# not possible but can have a dictionary that maps numbers to list as follows
dl = {1: [2], 3: [4]}
print_ds_details("dictionary of lists (NOT POSSIBLE)", dl)

# a dictionary of dictionaries
# not possible but can have a dictionary that maps numbers to dictionaries
dd = {1: {2: 3}, 3: {4: 5}}
print_ds_details("dictionary of dictionaries (NOT POSSIBLE)", dd)
