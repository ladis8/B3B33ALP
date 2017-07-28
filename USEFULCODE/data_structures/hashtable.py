

a = {}
a [3] = 5
print(a)
a [3] = 4
b = {1:2,4:6}
a.update(b)
print(a)


def find_prime(n):
    pass





class Hashtable:
    def __init__(self, n=13):
        #self.size = find_prime(n)
        self.size = n
        self.keys = [[] for _ in range (self.size)]
        self.values = [[] for _ in  range (self.size)]
        self.count = 0
        self.maximumloadfactor = 0.75

    def __repr__(self):
        return str ([list (zip(self.keys[i], self.values[i])) for i in range(self.size)])


    #does not need any hashtable, works generally
def find_index (l,key):
        for index,listkey in enumerate(l):
            if key == listkey:
                return index
        return None

    #need hashtable
def get (hashtable, key):
        m = hash (key) % hashtable.size #number of bucket
        i = find_index(hashtable.keys [m], key)
        return None  if i is None else hashtable.values [m][i]

    # need hashtable
    #implemented with open
def put(hashtable, key, value):
        m = hash (key) % hashtable.size #number of bucket
        index = find_index(hashtable.keys [m], key)
        if index is not None:
            hashtable.values [m] [index] = value #prepis
        else:   #vytvor
            hashtable.values [m].append(value)
            hashtable.keys [m].append(key)
            hashtable.count +=1

        if hashtable.count > hashtable.size * hashtable.maximumloadfactor: #pokud je tabulka zaplnena, zvetsi jeji velikost
            return grow_table(hashtable)
        else:
            return hashtable
def delete (hashtable, key):
    m = hash (key) %hashtable.size
    i = find_index(hashtable.keys[m], key)
    if i is not None:
        value = hashtable.values [m] [i]
        hashtable.keys [m].remove (key)
        hashtable.values [m].remove (value)

def grow_table(self, hashtable):
        newhashtable = Hashtable(2*hashtable.size) # vytvor tabulku s 2* vetsi velikosti

        for i in range (hashtable.size): #okopiruj vsechny polozky do nove tabulky
            keys = self.keys[i]
            values = self.values [i]
            for j in range (len(keys)):
                self.put(self, newhashtable, keys[j], values[j])

        return newhashtable
def items (hashtable):
    return [list(zip(hashtable.keys[i], hashtable.values[i])) for i in range(hashtable.size)]


hashtable = Hashtable()
put(hashtable, 'pi', 3.145)
put (hashtable, 16, 2.145)
put (hashtable, 14, 2.145)
put (hashtable, 3, 2.145)
put (hashtable, 3, 2.1)
print (items(hashtable))
delete (hashtable, 'pi')
print (get(hashtable, 3))
print (items(hashtable))
delete (hashtable, 16)
print(hashtable)
