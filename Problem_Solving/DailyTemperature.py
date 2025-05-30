def dailyTemperatures(temperatures):
    n = len(temperatures)
    result = [0] * n
    stack = []  # stack will store indices

    for i in range(0, n):
        while stack and temperatures[i] > temperatures[stack[-1]]:
            prev = stack.pop()
            result[prev] = i - prev
        stack.append(i)
    return result







