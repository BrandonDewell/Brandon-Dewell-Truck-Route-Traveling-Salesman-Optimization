# ChainingHashTable T(N) = O(N), S(N) = O(N)
class ChainingHashTable:
    # Constructor with optional initial capacity parameter.  It assigns all buckets with an empty list.
    # __init__() T(N) = O(N), S(N) = O(N)
    def __init__(self, initial_capacity=10):
        # initialize the hash table with empty bucket list entries.
        self.table = []
        for i in range(initial_capacity):
            self.table.append([])

    # inserts a new item into the hash table.
    # insert() T(N) = O(N), S(N) = O(N)
    def insert(self, key, item):  # does both insert and update.
        # get the bucket list where this item/object/package will go.
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        # update key if it is already in the bucket
        for kv in bucket_list:
            if kv[0] == key:
                kv[1] = item
                return True

        # if not, insert the item to the end of the bucket list.
        key_value = [key, item]
        bucket_list.append(key_value)
        return True

    # Searches for an item with matching key in the hash table.  It returns the item if found, or None if not found.
    # lookup() T(N) = O(N), S(N) = O(N)
    def lookup(self, key):
        # get the bucket list where this key would be.
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        # search for the key in the bucket list
        for kv in bucket_list:
            if kv[0] == key:
                return kv[1]  # value
        return None

    # removes an item with matching key from the hash table.
    # remove() T(N) = O(N) S(N) = O(N)
    def remove(self, key):
        # get the bucket list where this item will be removed from.
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        # remove the item from the bucket list if it is present.
        for kv in bucket_list:
            if kv[0] == key:
                bucket_list.remove([kv[0], kv[1]])
