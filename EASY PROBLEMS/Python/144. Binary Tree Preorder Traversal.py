def preorder(root):
    return [root.val] + preorder(root.left) + preorder(root.right) if root else []

return preorder(root)