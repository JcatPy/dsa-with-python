def evalRPN(self, tokens):
    op = "+-/*"
    stack = []

    for i in tokens:
        if not stack:
            stack.append(int(i))
        elif i in op:
            o1 = stack.pop()
            o2 = stack.pop()
            if i == "+":
                stack.append(o2 + o1)
            elif i == "-":
                stack.append(o2 - o1)
            elif i == "*":
                stack.append(o1 * o2)
            elif i == "/":
                stack.append(int(float(o2) / o1))
        else:
            stack.append(int(i))

    return stack.pop()

