from .user_input import yes_or_no, select_categories

class TreeNode:
    def __init__ (self, value, question, is_cat = False):
        """when adding a node, the value will be the class, 
        each node will ask a question to traverse it,
        if is_cat is true that means the select_category method will be called
        which means the end of the tree traversal, returning the class."""
        self.value = value
        self.question = question
        self.children = []
        self.is_cat = is_cat
    
    def add_child (self, node):
        self.node = node
        self.children.append(node)
    
    def traverse (self):
        current_node = self
        while current_node.children != []:
            if current_node.is_cat == True:
                break
            
            answer = None
            print(f"\n {current_node.question} ")
            answer = yes_or_no()
            current_node = current_node.children[answer]
        print(f"\n {current_node.question} ")
        answer = select_categories(current_node.value)
        return answer


            
        
        

