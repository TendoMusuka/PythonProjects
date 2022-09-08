def pre_order(root):
    if root == []:
        return root
    else:
        print(root.data)
        pre_order(root.left)
        pre_order(root.right)


def in_order(root):
    if root == []:
        return root
    else:
        pre_order(root.left)
        print(root.data)
        pre_order(root.right)

def post_order(root):
    if root == []:
        return root
    else:
        pre_order(root.left)
        pre_order(root.right)
        print(root.data)


print(pre_order([1,2,3,4,5]))