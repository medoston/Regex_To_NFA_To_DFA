#---------------------constructing the Thompson Tree-----------------------------
# -------------------------------------------------------------------------------

class TomTree:

    def __init__(self, type, value=None):

        self.type = type
        self.value = value
        self.left = None
        self.right = None
    
#-------------------_init_priority-----------------------
priority = {'A': 1, '.': 2, '+': 3,'*': 4}
stack_obj=[]
#--------------------------------------------------------

#--------------------------------------------------------
#-----------------plus_Function--------------------------
#storing the '+' and the charachters before and after it  
def plus(i):
    obj_tree = TomTree(priority[i])
    obj_tree.right = stack_obj.pop()
    obj_tree.left = stack_obj.pop()
    return obj_tree
#--------------------------------------------------------
#-----------------plus_Function--------------------------
#storing the '.' and the charachters before and after it 
def Mul(i):
    obj_tree = TomTree(priority[i])
    obj_tree.right = stack_obj.pop()
    obj_tree.left = stack_obj.pop()
    return obj_tree
#--------------------------------------------------------
#-----------------plus_Function--------------------------
#storing the '*' and the charachters before and after it 
def ast(i):
    obj_tree = TomTree(priority[i])
    obj_tree.left = stack_obj.pop()
    return obj_tree

#--------------------------------------------------------

#--------------------------------------------------------
#-------------------Main_Function------------------------
def Tree(exp):

    for i in exp:
        if i.isalpha():
            stack_obj.append(TomTree(priority['A'], i))

        else:
            if i == "+":
                obj_tree = plus(i)
            elif i == ".":
                obj_tree = Mul(i)
            elif i == "*":
                obj_tree = ast(i)
            stack_obj.append(obj_tree)

    return stack_obj[0]
# -------------------------------------------------------------------------------
