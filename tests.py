from dynamicArray import *


da = DynArray()
for i in range(1):
    da.append(i)
    print (da[i])

print("self count", da.count)
print("self capacity", da.capacity)

# da.insert(1, 99)
da.delete(0)



print("d. count", da.count)
print("d. capacity", da.capacity)


for i in range(da.count):
    # print("d. count", da.count)
    print (da[i])


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

def deleteTEST1():
    print("delete test 1")
    daTest = DynArray()
    for i in range(50):
        daTest.append(i)

    daTest.delete(0)

    if daTest.count == 49 and daTest.capacity == 64 and daTest[0] == 1:
        print("TEST OK")
    else:
        print("TEST ERROR")

deleteTEST1()

def deleteTEST2():
    print("delete test 2")
    daTest = DynArray()
    for i in range(8):
        daTest.append(i)

    daTest.delete(0)

    if daTest.count == 7 and daTest.capacity == 16 and daTest[0] == 1:
        print("TEST OK")
    else:
        print("TEST ERROR")

deleteTEST2()

# def deleteTEST3():
#     print("delete test 3")
#     daTest = DynArray()
#     for i in range(8):
#         daTest.append(i)
#
#     daTest.delete(10)
#
# deleteTEST3()

print(int(10.665555))