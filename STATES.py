

#-----------------_init_priority---------------------
priority = {'A': 1, '.': 2, '+': 3,'*': 4}
#----------------------------------------------------
#--------------------------------------------------------------------
class STATES:
    def __init__(self):
        self.next_state = {}
#--------------------------------------------------------------------


def NFA(Thompson_Tree):
#----------------------------Char------------------------------------
    if Thompson_Tree.type == priority['A']:

        start_state = STATES()
        end_state = STATES()
        #------setting an end state for the start state 
        start_state.next_state[Thompson_Tree.value] = [end_state]#the end state is embty here
        return start_state, end_state
#--------------------------------------------------------------------

#----------------------------Mul-------------------------------------
    elif Thompson_Tree.type == priority['.']:

        left_nfa  = NFA(Thompson_Tree.left)
        right_nfa = NFA(Thompson_Tree.right)
        #setting the next state for the left to the start of the right nfa 
        left_nfa[1].next_state['ε'] = [right_nfa[0]]
        return left_nfa[0], right_nfa[1]
#--------------------------------------------------------------------

#---------------------------plus-------------------------------------
    elif Thompson_Tree.type == priority['+']:

        start_state = STATES()
        end_state   = STATES()
        up_nfa   = NFA(Thompson_Tree.left)
        down_nfa = NFA(Thompson_Tree.right)
        #setteing the next state for the start to the start of the up and down states
        start_state.next_state['ε'] = [up_nfa[0], down_nfa[0]]
        #setting the next state of the up and down states to an end states 
        up_nfa[1].next_state['ε'] = [end_state]
        down_nfa[1].next_state['ε'] = [end_state]

        return start_state, end_state
#--------------------------------------------------------------------

#---------------------------astric-----------------------------------
    elif Thompson_Tree.type == priority['*']:
        start_state = STATES()
        end_state   = STATES()
        sub_nfa = NFA(Thompson_Tree.left)
        #setting the next state of the start state to the start state of the sub, end state
        start_state.next_state['ε'] = [sub_nfa[0], end_state]
        #setting the next state of the end state of the sub to the start of the sub and end
        #to apply recursion 
        sub_nfa[1].next_state['ε'] = [sub_nfa[0], end_state]
        return start_state, end_state
#--------------------------------------------------------------------