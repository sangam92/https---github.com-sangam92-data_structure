def paranthesis(exprs):
    stack = []
    for char in exprs:
        if char in ["(","{","["]:
            stack.append(char)
        else:
            currchar = stack.pop()
            if currchar =="(":
                if char !=")":
                    return False
            if currchar == "{":
                if char != "}":
                    return False
            if currchar == "[":
                if char != "]":
                    return False
    if stack:
        print(stack)
        return False
    return True


if __name__ == "__main__":
    exprs = "({[]}]"

    if paranthesis:
        print("Balanced")
    else:
        print("Unbalanced")
