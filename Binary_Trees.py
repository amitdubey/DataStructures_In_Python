import collections
from typing import List
import functools
#from typing import BinaryTreeNode
class BinaryTreeNode:
    def __init__(self,data=None, left=None, right=None):
        self.data = data
        self.left=left
        self.right=right
        
    def traversal(self,root)->None:
        if root:
            print('Preorder %d'%root.data)
        traversal(root.left)
        print('inorder %d' %root.data)
        traversal(root.right)
        print('postorder: %d' %root.data)
        
    def is_balanced_b_tree(self, tree)-> bool:
        balanceStatuswithheight =collections.nametuple(
            'balancedStatusWithHeight',('balanced','height'))
        def check_balance(tree):
            if not tree:
                return balanceStatuswithheight(True,-1)
            left_result =check_balance(tree.left)
            if not left_result.balanced:
                return balanceStatuswithheight(False,0)
            right_result = check_balance(tree.right)
            if not right_result.balanced:
                return balanceStatuswithheight(False,0)
            is_balanced =abs(left_result.height - right_result.height) <=1
            height =max(left_result.height,right_result.height)
            return balanceStatuswithheight(is_balanced,height)
        return check_balance(tree).balanced
    
    
    """check if the tree is symmetric 
        return False     
            """
    def is_symmetric(self,tree) ->bool:
        def check_symmetric(subtree_0, subtree_1):
            if not subtree_0 and not subtree_1:
                return True
            elif subtree_1 and subtree_0:
                return (subtree_0.data==subtree_1.data 
                        and check_symmetric(subtree_0.left, subtree_1.right) 
                        and check_symmetric(subtree_0.right,subtree_1.left))
            return False
        return not tree or check_symmetric(tree.left,tree.right)
            
    
    def sum_root_to_leaf(self, tree)->int:
        def sum_root_leaf_helper(tree,partial_path_sum=0):
            if not tree:
                return 0 
            partial_path_sum = partial_path_sum * 2 + tree.data
            if not tree.left and not tree.right:
                return partial_path_sum
            return (sum_root_leaf_helper(tree.left, partial_path_sum)+ sum_root_leaf_helper(tree.right,partial_path_sum))
        return sum_root_leaf_helper(tree)
    
    def preorder_traversal(self,tree) -> List[int]:
        result = []
        in_process = [(tree, False)]
        while in_process:
            node, node_processed = in_process.pop()
            if node:
                if node_processed:
                    result.append(node.data)
                else:
                    in_process.append((node.right, False))
                    in_process.append((node.left, False))
                    in_process.append((node, True))
            return result
    
    
    
if __name__ == '__main__':
    N =BinaryTreeNode()
    tree = N(1, N(2, N(4), N(5, N(8), None)),
             N(3, N(6, None, N(9)), N(7, None, N(10, N(11), N(12)))))

    # assert generate_inorder(tree) == [4, 2, 8, 5, 1, 6, 9, 3, 7, 11, 10, 12]
    # assert generate_preorder(tree) == [1, 2, 4, 5, 8, 3, 6, 9, 7, 10, 11, 12]
    # assert generate_postorder(tree) == [4, 8, 5, 2, 9, 6, 11, 12, 10, 7, 3, 1]

    # path = TreePath().with_left().with_left().with_right().with_left()
    # assert str(path) == "root->left->left->right->left"
       
