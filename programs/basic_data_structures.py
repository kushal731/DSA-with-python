def setoperation():
    s1 = {11, 44, 55, 99}
    s2 = {22, 11, 66}
    print("Set1 = ", s1)
    print("Set2 = ", s2)
    s1.add(77)
    print("Set after adding element 77 = ", s1)
    s1.remove(44)
    print("Set after removing element 44 = ", s1)
    print("Union of two sets = ", s1.union(s2))
    print("Intersection of two sets = ", s1.intersection(s2))
    return

def tupleoperation():
    t1 = (11, 44, 55, 99)
    t2 = (22, 11, 66)
    print("Tuple1 = ", t1)
    print("Tuple2 = ", t2)
    print("Tuple after repetating elements for 2 times ", t1 * 2)
    print("After concatenating 2 tuples = ", t1 + t2)
    print("Element at position 3 in tuple1 = ", t1[3])
    print("Elements from 1 to 3 in tuple1 = ", t1[1:4])
    return

def listoperation():
    L1 = [10, 20, 30, 40]
    L1.append(15)
    print("list after adding 15 is ", L1)
    L1.insert(3, 25)
    print("List after inserting 25 at position 3 is ", L1)
    print("Element at position 3 is ", L1[3])
    print("Elements in list from 1 to 3 is ", L1[1:4])
    return

def dictoperation():
    d1 = {1: "One", 2: "Two", 3: "Three", 4: "Four"}
    print("Dictionary value for key 2 is ", d1[2])
    print("Dictionary items =", d1.items())
    print("Keys of dictionary d1 =", d1.keys())
    print("Values of dictionary d1 =", d1.values())
    return

# Main
while(True):
    print(" Menu")
    print("1: Set Operation")
    print("2: Tuple Operation")
    print("3: List Operation")
    print("4: Dictionary Operation")
    print("5: Exit")

    option = int(input("Enter option value 1 to 5: "))
    if option == 1:
        setoperation()
    elif option == 2:
        tupleoperation()
    elif option == 3:
        listoperation()
    elif option == 4:
        dictoperation()
    else:
        print("Invalid option value")
        break