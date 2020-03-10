# '''
# Linked List hash table key/value pair
# '''
# Starting project
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''
    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.size = 0
        self.storage = [None] * capacity


    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        # result
        hashsum = 0 

        # loop through key, and each character in key
        for idx, c in enumerate(key):
        # index of the character + length of key
            hashsum += (idx + len(key)) ** ord(c)
        # mod self.capacity
            hashsum = hashsum % self.capacity
        
        return hashsum


    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        '''
        hash= 5381
        for c in key:
            hash = (hash * 33) + ord(c)
        return hash


    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash(key) % self.capacity


    def insert(self, key, value):
        '''
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Fill this in.
        '''
        # # increment internal size by 1
        # self.size += 1
        # # find index in array
        # index = self._hash(key)
        # # find the node
        # node = self.storage[index]
        # # if none, assign to new node
        # if node is None:
        #     self.storage[index] = LinkedPair(key, value)
        #     return
        # # otherwise, collision occurs
        # prev = node
        # # loop until not none
        # while node is not None:
        #     prev = node
        #     node = node.next
        # prev.next = LinkedPair(key, value)

        new_hash_index = LinkedPair(key, value)
        hash_index = self._hash_mod(key)

        if self.storage[hash_index] is not None: 
            # bucket already exists
            if self.storage[hash_index].key == key:  
            # checking if the first node in bucket is the key we're looking for
                self.storage[hash_index] = new_hash_index  
                # if it is, replace the node with the new node
                return
            current = self.storage[hash_index]  
            # not the correct key
            while current.next is not None:   
                # iterate through until we find the key
                if current.key == key:   
                    # once found, update node to new node values
                    current = new_hash_index
                    break
                current = current.next
            current.next = new_hash_index
        else:
            self.storage[hash_index] = new_hash_index

    



    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
        # index = self._hash_mod(key)
        # # find the node
        # node = self.storage[index]
        # while node is not None and node.key != key:
        #     prev = node
        #     node = node.next
        # # if nothing found, return none
        # if node is None:
        #     return None
        # # else found node, decrement size by 1 and store value in temporary variable
        # else:
        #     self.size -= 1
        #     result = node.value
        #     if prev is None:
        #         node = None
        #     else:
        #         prev.next = prev.next.next
        #     # return data value of found node
        #     return result

        bucket = self._hash_mod(key)
        if self.storage[bucket] is not None:
            if self.storage[bucket].key == key:
                self.storage[bucket] = None
                return
            else:
                while self.storage[bucket].key is not key and self.storage[bucket] is not None:
                    self.storage[bucket] = self.storage[bucket].next
                self.storage[bucket] = None
                return
        else:
            print("The key is not found")




    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        index = self._hash(key)
        # find the node
        node = self.storage[index]
        while node is not None and node.key != key:
            node = node.next
        # if we reach the end of the linked list and find nothing
        if node is None:
            return None
        else:
            return node.value


    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        # self.capacity *= 2
        # new_storage = [None] * self.capacity
        # for i in range(self.size):
        #     new_storage[i] = self.storage[i]
        # self.storage = new_storage
        # self.capacity = self.capacity * 2
        # self.capacity = self.capacity + [None] * 2
        # self.storage *= 2
        # new_storage = [None] * self.capacity

        # for i in range(self.size):
        #     new_storage[i] = self.storage[i]
        # self.storage = new_storage
        temp_storage = self.storage
        self.capacity = self.capacity * 2
        self.storage = [None] * self.capacity

        for bucket in temp_storage:
            if bucket is None:
                pass
            elif bucket.next is None:
                self.insert(bucket.key, bucket.value)
            else:
                while bucket is not None:
                    self.insert(bucket.key, bucket.value)
                    bucket = bucket.next



if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")
