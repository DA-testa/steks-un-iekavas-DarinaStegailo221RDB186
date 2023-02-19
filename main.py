# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next in "([{":
            # Process opening bracket, write your code here
            b = Bracket (i, next)
            opening_brackets_stack.append(b)

        if next in ")]}":
            # Process closing bracket, write your code here
            if not opening_brackets_stack:
                return i + 1
            p = opening_brackets_stack.pop()
            if (p.char == '('and next !=')') or (p.char == '['and next !=']') or (p.char == '{'and next !='}'):
                return i+1       
        if opening_brackets_stack:
            return opening_brackets_stack[0].position + 1
        return "Success"


def main():
     # Printing answer, write your code here
    i = input("F or I")
    if i =="F":
        j = input()
        with open(j,"r") as x:
            text = x.readline().strip()
        else:
            text = input()
            mismatch = find_mismatch(text)
            print (mismatch)

if __name__ == "__main__":
    main()   
