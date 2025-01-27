from random import randint
import sys
import os

first_normal_ascii_symbol = ' '
last_normal_ascii_symbol = '~'
offset = ord(first_normal_ascii_symbol)
symbol_size = ord(last_normal_ascii_symbol) - offset

def to_symbolic(number: int, min_length = 0) -> str:
    symbolic = ""
    while number > 0:
        symbolic = chr(number%symbol_size + offset) + symbolic
        number //= symbol_size
    if min_length != 0:
        while len(symbolic) < min_length:
            symbolic = first_normal_ascii_symbol + symbolic
    return symbolic

def to_int(symbolic: str) -> int:
    number = 0
    for symbol in symbolic:
        number *= symbol_size
        number += ord(symbol) - offset
    return number

def serialize(l:list[int], path=None) -> str| None:
    min_simbolic_size = len(to_symbolic(max(l)))
    serialized = "".join([to_symbolic(e, min_simbolic_size) for e in l])
    serialized = str(min_simbolic_size) + serialized
    if path == None:
        return serialized
    with open(path, "w", encoding="ASCII") as file:
        file.write(serialized)

def deserialize(serialized: str=None, path=None) -> list[int]:
    desrialized = []
    if path != None:
        with open(path, "r", encoding="ASCII") as file:
            serialized = file.read()
    if serialized == None:
        raise Exception("No argument was passed to the function")
    symbolic_size = int(serialized[0])
    for offset in range(1, len(serialized), symbolic_size):
        desrialized.append(to_int(serialized[offset:offset + symbolic_size]))
    return desrialized