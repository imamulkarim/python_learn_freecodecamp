class HashTable:
    def __init__(self):
        self.collection = dict()

    def hash(self, text):
        return  sum(map(ord, text))

    def add(self, key, value):
        hash_key = self.hash(key)
        if hash_key in self.collection.keys():
            dicItem = self.collection[hash_key]
            self.collection[hash_key] = dicItem | { key: value}
        else:
            self.collection[hash_key] = {  key: value}
        #print(self.collection)

    def remove(self, key):
        hash_key = self.hash(key)
        if hash_key in self.collection.keys():
            self.collection[hash_key].pop(key, None)
        

    def lookup(self, key):
        hash_key = self.hash(key)
        if hash_key in self.collection.keys():
            return self.collection[hash_key].pop(key, None)
        


ht = HashTable()
ht.add('dear', 'friend')
ht.add('read', 'book')
ht.add('golf', 'sport')
print(ht.hash('read'))
ht.remove('readdeqw')
ht.remove('None')
print(ht.lookup('golf'))