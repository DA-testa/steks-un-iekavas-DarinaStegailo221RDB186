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
            b = Bracket (next, i + 1)
            opening_brackets_stack.append(b)

        if next in ")]}":
            # Process closing bracket, write your code here
            if not opening_brackets_stack:
                return i + 1
            pop = opening_brackets_stack.pop()
            if not are_matching(pop.char, next):
                return i + 1

    if opening_brackets_stack:
        return opening_brackets_stack[0].position

    return "Success"

def main():
    # Printing answer, write your code here
    i = input("F or I")
    if "F" in i:
        file = input("Enter file name: ")
        with open(file, "r", encoding="latinl") as f:
            text = f.read()
        mismatch = find_mismatch(text)
        if mismatch == "Success":
            print("Success")
        else:
            print(mismatch)
    elif "I" in i:
        text = input()
        mismatch = find_mismatch(text)
        if mismatch == "Sucess":
            print("Success")
        else:
            print(mismatch)

if __name__ == "__main__":
    main()
