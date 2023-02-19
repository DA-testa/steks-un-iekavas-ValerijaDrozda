## Valerija Drozda 221RDB450

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])

def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]

def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next in "([{":
            opening_brackets_stack.append(next)
        if next in ")]}":
            if((len(opening_brackets_stack) == 0) or not (are_matching(opening_brackets_stack[-1], next))):
                return i+1
            opening_brackets_stack.pop()
    return 0
    
def main():
    choice = input("Choose input: ")
    if "F" in choice:
        path = input("Enter path to file: ")
        with open(path, "r") as file:
            text = file.read()
            mismatch = find_mismatch(text)
            if mismatch == 0:
                print("Success")
            else:
                print(mismatch)
    elif "I" in choice:
        text = input()
        mismatch = find_mismatch(text)
        if mismatch == 0:
            print("Success")
        else:
            print(mismatch)
    else:
        print("Invalid input choice.")

if __name__ == "__main__":
    main()
