import ctypes


class DynArray:

    def __init__(self):
        self.count = 0
        self.capacity = 16
        self.array = self.make_array(self.capacity)

    def __len__(self):
        return self.count

    def make_array(self, new_capacity):
        return (new_capacity * ctypes.py_object)()

    def __getitem__(self, i):
        if i < 0 or i >= self.count:
            raise IndexError('Index is out of bounds')
        return self.array[i]

    def resize(self, new_capacity):
        new_array = self.make_array(new_capacity)
        for i in range(self.count):
            new_array[i] = self.array[i]
        self.array = new_array
        self.capacity = new_capacity

    def append(self, itm):
        if self.count == self.capacity:
            self.resize(2 * self.capacity)
        self.array[self.count] = itm
        self.count += 1

    def insert(self, i, itm):

        if i < 0 or i > self.count:
            raise IndexError('Index is out of bounds')

        self.append(itm)
        len  = self.count - 1

        while i != len:
            buf = self.array[len - 1]
            self.array[len - 1] = self.array[len]
            self.array[len] = buf

            len -= 1


    def delete(self, i):

        if i < 0 or i > self.count:
            raise IndexError('Index is out of bounds')

        len = self.count - 1
        j = 0
        k = 0
        self.capacity = 16
        new_array = self.make_array(self.capacity)

        while j != len:

            if j == i:
                if j == self.count:
                    continue
                else:
                    k += 1

            new_array[j] = self.array[k]

            if k == len:
                j += 1
                continue

            j += 1
            k += 1

        self.array = new_array
        self.count -= 1

        if self.count < (self.capacity / 2):
            self.capacity = int((self.capacity) / 1.5)

da = DynArray()
for i in range(8):
    da.append(i)
    print (da[i])

print("self count", da.count)

da.insert(1, 99)

da.delete(1)


print("d. count", da.count)
print("d. capacity", da.capacity)


for i in range(da.count):
    # print("d. count", da.count)
    print (da[i])

print("capacity", da.capacity)


# TESTS
def insertTEST1():
    print("Insert test 1")
    daTest = DynArray()
    for i in range(15):
        daTest.append(i)

    daTest.insert(1,99)

    if daTest.count == 16 and daTest.capacity == 16 and daTest[1] == 99:
        print("TEST OK")
    else:
        print("TEST ERROR")

insertTEST1()

def insertTEST2():
    print("Insert test 2")
    daTest = DynArray()
    for i in range(16):
        daTest.append(i)

    daTest.insert(16, 99)

    if daTest.count == 17 and daTest.capacity == 32 and daTest[16] == 99:
        print("TEST OK")
    else:
        print("TEST ERROR")

insertTEST2()

# def insertTEST3():
#     print("Insert test 3")
#     daTest = DynArray()
#     for i in range(16):
#         daTest.append(i)
#
#     daTest.insert(52, 99)
#
# insertTEST3()