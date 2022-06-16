
from Project_Main import*


temp=DFA


#------------------------starting state----------------------
def start_arr(nfa):
    Df_start_array=[]
    for i in range(len(nfa)):

        if i == 0 :
            s=nfa[0].replace("ε", "")
            f=s
            s_without_zero=s.split()
            int_s_without_zero=list(map(int, s_without_zero))
            continue

        else:

            if nfa[i][1] !=" ":
                temp22 = nfa[i][0] + nfa[i][1]
                exist = int_s_without_zero.count(int(temp22))

                if exist <= 0:
                    continue
            
            

            for j in nfa[i]:
            
                if s.find(j) != -1:
                    if nfa[i].find("ε") != -1:
                        t=nfa[i].replace("ε", "")
    
                        f = f + t
                         
                        break
                    else:
                        break
                else:
                    break
#------------------------------------------------------------
           


#--------------remove_repeted_elements_from_the_string-------
    rep = f.split()
    starting = list(set(rep))

    return starting


trial= start_arr(temp)
#-------------------------------------------------------------

#-----function that returns ep transitions--------------------
def indx(element):
    f=""
    if len(element) > 1:
        for i in range(len(temp)):
            if (temp[i][0] + temp[i][1]) == element:    
                f = f + temp[i]
        return f

    else:
        for i in range(len(temp)):
            if temp[i][0] == element:
                f = f + temp[i]
        return f
#-------------------------------------------------------------

#----------------next ep transition---------------------------
def eps(starting,final):
    arr=[]
    for j in starting:
        temp_55=str(indx(str(final)))
        if temp_55.find("ε") != -1:
            temp15=temp_55.replace("ε", "") 
            temp115= temp15.split()
            
            Cc=list(map(int, temp115))
            
            for i in Cc:
                arr.append(i)

            # Cc=list(map(int, temp115))
            # print(Cc)

            # arr.append(Cc[1])
            final=arr[-1]
            continue
    return arr
#-------------------------------------------------------------

#-----------------removing Duplicates -----------
def Duplicates(arr):
    new_arr=[]
    for i in arr:
        if i not in new_arr:
            new_arr.append(i)
    return new_arr
#-------------------------------------------------------------

#-----constructing the DFA-----------------------

def con_DFA(starting):
    A=[]
    B=[]
    C=[]

    for i in starting:
        temp_5=str(indx(i))

#----------------------ep CASE-------------------

        if temp_5.find("ε") != -1:
            continue



#----------------------A CASE--------------------
        if temp_5.find("a") != -1:
            temp6=temp_5.replace("a", "")
            temp7= temp6.split()
            A=list(map(int, temp7))
            A.remove(int(i))
            A_com=eps(starting,A[-1])
            if len(A_com)>0:
                for va in A_com:
                    A.append(va)

#----------------------B CASE--------------------

        if temp_5.find("b") != -1:
            temp8=temp_5.replace("b", "")
            temp9= temp8.split()
            B=list(map(int, temp9))
            B.remove(int(i))
            B_com=eps(starting,B[-1])
            if len(B_com)>0:
                for vb in B_com:
                    B.append(vb)

#----------------------C CASE--------------------
        if temp_5.find("c") != -1:

            temp10=temp_5.replace("c", "")
            temp11= temp10.split()
            C=list(map(int, temp11))
            C.remove(int(i))
            C_com=eps(starting,C[-1])
            if len(C_com)>0:
                for vc in C_com:
                    C.append(vc)

    A=Duplicates(A)
    B=Duplicates(B)
    C=Duplicates(C)


    return A,B,C

#-------------------------------------------------------------

#---------------------DFA States------------------------------
def DFA_States():

    arr=[]
    arr.append(con_DFA(trial))

    for i in range(100):
        for j in arr[i]:
            arr.append(con_DFA(str(j)))


    new_arr=[]
    new_arr.append(list(map(int, trial)))
    for z in range(len(arr)):
        for b in range(len(arr[z])):
            if arr[z][b] not in new_arr:
                # print(i)
                new_arr.append(arr[z][b])
    
    arr_dfa=Duplicates(new_arr)
    arr_dfa.remove([])
    return arr_dfa
#-------------------------------------------------------------


#-------------------------------------------------------------
#----------------------------main-----------------------------
states=DFA_States()
DFA_st_CHAR=['A','B','C','D','E','F','G','H','I','J']
start_state_dfa=[]

print("------------------------------------------------------------------------------")
print("------------------------------------DFA---------------------------------------\n")
print("------------------------------------------------------------------------------")
print("DFA states\t a\t\tb\t\t\tc\n")
print("------------------------------------------------------------------------------")

#----------testing phase init------------
A_test=[]
B_test=[]
C_test=[]
#----------------------------------------

for mx in range(len(states)):

    Ax,Bx,Cx = con_DFA(str(states[mx]))
    print(f"{DFA_st_CHAR[mx]} \t ----->  {Ax}\t\t{Bx}\t\t\t{Cx} ")
    if DFA_st_CHAR[mx]=="A":
        A_test=states[mx]

    if DFA_st_CHAR[mx]=="B":
        B_test="a"

    if DFA_st_CHAR[mx]=="C":
        C_test="b"

    start_state_dfa.append(f"{DFA_st_CHAR[mx]} ----->  {Ax}\t{Bx}\t{Cx} ")

print("------------------------------------------------------------------------------")
print("----------------------------------THANKS--------------------------------------")
print("------------------------------------------------------------------------------")



test=input("\n\n Enterthe testing case: ")
# print(start_state_dfa)

# opiip=start_state_dfa.split('----->')
# print(opiip)
# print(A_test,B_test,C_test)
# #  printing the values of the Dfa states
# lanm=[]
# for iou in start_state_dfa:
#     x=iou.split("----->")
#     mnnb=x[1].split("\t")

if test==B_test:
    print("Accepted")
elif test==C_test:
    print("Accepted")
else:
    print("regected")