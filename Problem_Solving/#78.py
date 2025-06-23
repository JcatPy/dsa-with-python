def subsets(nums):
    res, sol = [], []
    n = len(nums)

    def dfs(i):
        if i >= n:
            res.append(tuple(sol))
            return

        sol.append(nums[i])
        dfs(i + 1)

        sol.pop()
        dfs(i + 1)

    dfs(0)
    return res
