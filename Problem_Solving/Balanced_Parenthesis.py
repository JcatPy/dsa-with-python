def isValid(s):
    stack = []
    reverse_dict = {'(': ')', '{': '}', '[': ']'}

    for i in s:
        if (i == '(' or i == '{' or i == '['):
            stack.append(i)

        elif i in reverse_dict.values():
            if not stack or reverse_dict[stack.pop()] != i:
                return False
    return not stack

