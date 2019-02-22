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

        if i < 0 or i > self.count or self.count == 0:
            raise IndexError('Index is out of bounds')

        len = self.count - 1
        j = 0
        k = 0

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

        if self.count < (self.capacity / 2) and self.count != 16:
            self.capacity = int((self.capacity) / 1.5)
            if self.capacity < 16:
                self.capacity = 16
