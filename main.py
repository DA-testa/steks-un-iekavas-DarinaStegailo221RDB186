# python3

from collections import namedtuple 
 
Bracket = namedtuple("Bracket", ["char", "position"]) 
 
 
def are_matching(left, right): 
    return (left + right) in ["()", "[]", "{}"] 
 
 
def find_mismatch(text): 
    opening_brackets_stack = [] 
    for i, next in enumerate(text): 
        if next in "([{": 
            opening_brackets_stack.append(Bracket(next, i+1)) 
        if next in ")]}": 
            if not opening_brackets_stack: 
                return i+1 
            if not are_matching(opening_brackets_stack[-1].char, next): 
                return i+1 
            opening_brackets_stack.pop() 
    if opening_brackets_stack: 
        return opening_brackets_stack[-1].position 
    else: 
        return "Success" 
 
 
def main(): 
    choice = input("Use an input to choice files or input - F or I:") 
    if choice == "F": 
        filename = input("Enter file name:") 
        with open(filename, "r") as f: 
            text = f.readline().strip() 
    else: 
        text = input("Enter the brackets:") 
    mismatch = find_mismatch(text) 
    print(mismatch) 
 
 
if name == "main": 
    main()
