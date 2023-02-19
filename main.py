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
            obs = opening_brackets_stack[-1]
            if not are_matching(obs.char, next):
                return i+1
            opening_brackets_stack.pop()

        if opening_brackets_stack:
            return obs.position
        else:
            return "Success"

def main():
    # Printing answer, write your code here
    i = input("F" or "I")
    if i == "F":
        text = input()
        mismatch = find_mismatch(text)
        print(mismatch)
    else:
        text = input()
        mismatch = find_mismatch(text)
        print(mismatch)

if __name__ == "__main__":
    main() 
