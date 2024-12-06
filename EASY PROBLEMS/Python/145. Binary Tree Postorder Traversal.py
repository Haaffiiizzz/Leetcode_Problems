def postorder(root):
    return postorder(root.left) + postorder(root.right) + [root.val] if root else []
return postorder(root)