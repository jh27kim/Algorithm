# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.ans = -1e9
        def dfs(root):
            if root:
                l = dfs(root.left)
                r = dfs(root.right)
                ans = root.val
                ans = max(ans, l + ans)
                ans = max(ans, r + ans)
                self.ans = max(self.ans, ans)
                return max(root.val, root.val + max(l, r))
            else:
                return 0

        dfs(root)
        return self.ans


root = [1,2,3]
sol = Solution()
answer = sol.maxPathSum(root)
print(answer)
