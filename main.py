from random import randint
import sys
import os


def serialize(l:list[int], path=None) -> str| None:
    serialized = "".join([chr(i//128) + chr(i%128) for i in l])
    if path == None:
        return serialized
    with open(path, "w", encoding="ASCII") as file:
        file.write(serialized)

def deserialize(serialized: str=None, path=None) -> list[int]:
    l = []
    if path != None:
        with open(path, "r", encoding="ASCII") as file:
            serialized = file.read()
    if serialized == None:
        raise Exception("No argument was passed to the function")
    for i in range(0, len(serialized),2):
        l.append(ord(serialized[i])*128 + ord(serialized[i+1]))
    return l

if __name__ == "__main__":
    l = [randint(100,300) for i in range(900)]
    path = r".\data.txt"

    s = serialize(l)
    print(sum([sys.getsizeof(i) for i in l])+sys.getsizeof(l))
    print(sys.getsizeof(s))

    serialize(l, path)
    print(os.stat(path).st_size)

    l2 = deserialize(s)
    l3 = deserialize(s)
    print(l2 == l)
    print(l3 == l)