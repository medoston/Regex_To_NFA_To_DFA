from INFIX import*
from Construct_Tree import*
from STATES import*


DFA=[]
#------------------------------------------------------------------------------
#----------------------------printing function---------------------------------
def print_States_t(states,Q,infinit_loop_breacker):

    if states in infinit_loop_breacker:
        return

    infinit_loop_breacker.append(states)

    for ss in list(states.next_state):
        output= 'q'+ str(Q[states]) + "\t\t" + ss + "\t\t" 
        Df= str(Q[states]) + " " +  ss 
        for Next in states.next_state[ss]:
            if Next not in Q:
                Q[Next] = 1 + sorted(Q.values())[-1]
            output = output + "q" + str(Q[Next]) + " "
            Df = Df + " " + str(Q[Next]) + " "
        DFA.append(Df)
        print(output)
        for sn in states.next_state[ss]:
            print_States_t(sn,Q,infinit_loop_breacker)

#------------------------------------------------------------------------------
#-----------------------------designing----------------------------------------

def print_T(states):
    print("State"+"\t\t" + "Symbol" +"\t\t" + "Next state")
    print("------------------------------------------------------------------------------")
    #print_States(states[0], [], {states[0]:0})
    print_States_t(states[0],{states[0]:0},[])
    
    print("------------------------------------------------------------------------------")
    print("----------------------------------THANKS--------------------------------------")
    print("------------------------------------------------------------------------------\n\n")

print("------------------------------------------------------------------------------")
print("------------------------------NFA Constructor---------------------------------")
print("------------------------------------------------------------------------------")

#------------------------------------------------------------------------------
#------------------------------------main--------------------------------------
#------------------------------------------------------------------------------
Regular_exp = input("-Enter The Regular Expression: ")
print("------------------------------------------------------------------------------")

obj = InfixConversion(len(Regular_exp))
Regular_exp_INFIX=obj.INFIX(Regular_exp)
Thompson_Tree = Tree(Regular_exp_INFIX)
states= NFA(Thompson_Tree)

print_T(states)
# print(DFA)



#------------------------------------------------------------------------------


#------------------------------------------------------------------------------
#------------------------------Test_cases--------------------------------------

# ---------------------(a+b)-------------------------
# State           Symbol                  Next state
# q0              epsilon                 q1 q2
# q1              a                       q3
# q3              epsilon                 q4
# q2              b                       q5
# q5              epsilon                 q4

#------------------(a+b).(a+b)----------------------
# State           Symbol                  Next state
# q0              epsilon                 q1 q2
# q1              a                       q3
# q3              epsilon                 q4
# q4              epsilon                 q5
# q5              epsilon                 q6 q7
# q6              a                       q8
# q8              epsilon                 q9
# q7              b                       q10
# q10             epsilon                 q9
# q2              b                       q11
# q11             epsilon                 q4

#------------------(a+b)*.(a+b)----------------------
# State           Symbol                  Next state
# q0              epsilon                 q1 q2
# q1              epsilon                 q3 q4
# q3              a                       q5
# q5              epsilon                 q6
# q6              epsilon                 q1 q2
# q2              epsilon                 q7
# q7              epsilon                 q8 q9
# q8              a                       q10
# q10             epsilon                 q11
# q9              b                       q12
# q12             epsilon                 q11
# q4              b                       q13
# q13             epsilon                 q6
