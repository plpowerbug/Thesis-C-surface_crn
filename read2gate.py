import os
import SurfaceCRNQueueSimulator
import sys
import numpy as np

def color_map():
    check = 0
    check2 = 0
    colors=""
    signals = []
    states =[]
    signal_state=[]
    stateadd = []
    states2add =[]
    state =[]
    states2 =[]
    fileout.write(str("!START_COLORMAP\n")) 
   
    check = 0
    initial=[]
    # initialise signal_state
    
    signal_state=[[9]*15 for _ in range(20)]
        
    for line in file1:
        #read color map in not gate file
        if "!START_COLORMAP" in str(line):
            check = 1
        if ( "!END_COLORMAP" in  str(line)) :
            break
        signal2=[]
        check3=0
        if check == 1 and "!START_COLORMAP" not in str(line) and "{" in str(line):       
            signal2 = str(line).split("} ")
            curr = 0
            for k in range (15):
                if signal_state[k][0] == 9 and check3==0:
                    check3=1
                    curr  = k
                    signal_state[k][0] = signal2[0]
                    
            signals. append(signal2[0])
            if len(signal2)>1:
                state = str(signal2[1]).split(": ")
                if len(signal_state)>curr:
                    if (len(signal_state[curr])>14):
                        signal_state[curr][14]=state[1]
            #get states
            if len(state)>1:
                states2 = str(state[0]).split(", ")
            for s in states2:
                if s not in states:
                    states.append(s)
                    #add to 2d array
                    j = 0
                    for j in range(0,20):
                        if len(signal_state)>curr:
                            if (len(signal_state[curr])>j):
                                if signal_state[curr][j] == 9:
                                    signal_state[curr][j] = s
                                    
                                    break             
                #goback to first file and add states 
    for line in file3:
        if "!START_COLORMAP" in str(line):
            check2 = 1
        if ( "!END_COLORMAP" in  str(line)) :
            break
        if check2 ==1 and "!START_COLORMAP" not in str(line) and "{" in str(line):
            #This is to put all species together
            stateadd = str(line).split("} ")
            if stateadd[0] not in signals:#
                signals. append(stateadd[0])
                i = 0
                for i in range(0,15):
                    if signal_state[i][0] == 9:
                        signal_state[i][0] = stateadd[0]
                        break
                if len(stateadd)>1:
                    stateadd = stateadd[1].split(": ")
                    if len(signal_state)>i:
                        if (len(signal_state[i])>14):
                            signal_state[i][14]=stateadd[1]
                   
                if len(stateadd)>1:
                    states2add = str(stateadd[0]).split(", ")
                for s2 in  states2add:
                    if s2 not in states:
                        states.append(s2)
                        j = 0
                        for j in range(0,20):
                            if len(signal_state)>i:
                                if (len(signal_state[i])>j):
                                    if signal_state[i][j] == 9:
                                        signal_state[i][j] = s2
                                        break   
            else:
                #insert states
                for i in range(0,15):
                    if signal_state[i][0] == stateadd[0]:
                        if len(stateadd)>1:
                            stateadd = stateadd[1].split(": ")
                            if len(signal_state)>i:
                                if (len(signal_state[i])>14):
                                    signal_state[i][14]=stateadd[1]
                        if len(stateadd)>1:
                            states2add = str(stateadd[0]).split(", ")
                        for s2 in  states2add:
                            if s2 not in states:
                                states.append(s2)
                                j = 0
                                for j in range(0,20):
                                    if len(signal_state)>i:
                                        if (len(signal_state[i])>j):
                                            if signal_state[i][j] == 9:
                                                signal_state[i][j] = s2
                                                break
                        break
                    
            #get states
            
    for i in range(0,15):
        colors =""
        
        if len(signal_state)>i:
            if (len(signal_state[i])>0) :
                if signal_state[i][0] != 9:
                    colors= colors +signal_state[i][0]+"} "
                else:
                    break
        for j in range(0,20):
            if len(signal_state)>i+1:
                if (len(signal_state[i])>j+2) :###########J+1
                    if signal_state[i][j+1] != 9:
                        colors= colors +signal_state[i][j+1]
                    if signal_state[i][j+2] != 9:
                        colors= colors +", "
                    if signal_state[i][j+2] == 9:
                        break
        colors = colors +": "+ str(signal_state[i][14]  )      
        fileout.write(colors)
        
    colors =""
    #start write color map
    #end template of rules
    fileout.write(str("!END_COLORMAP\n"))   
def top_left_of_the_gate_to_be_copied(file):
    '''this is copy the gate's initial state to array'''
    s=[]
    s_no_space =[]
    twoD_array=[]
    row = 0
    c = 0
    coloum = 0
    check = 0
    for index, line in enumerate(file):
        #read color map in not gate file
        if "!START_INIT_STATE" in str(line):
            check = 1
        if ( "!END_INIT_STATE" in  str(line)) :
            break
        if check == 1 and "!START_INIT_STATE" not in str(line):
            s = str(line).split(" ")
            c = 0
            for i in s:
                for character in '\n':
                    i = i.replace(character, '')
                if i.isalnum():
                    s_no_space.insert(c,i)
                    c = c + 1             
            #coloum = len(s_no_space)
            if s_no_space != []:
                twoD_array.append(s_no_space)
                coloum = len(s_no_space)
            s_no_space = []
            row= row + 1
    print(twoD_array)
    ROW = len(twoD_array)
    print(len(twoD_array))
    print(coloum)
    return twoD_array
def top_left_destination_at_the_merged_gate(first, second):
    '''this is used when the output of the gate is in the top_left of the final circuit '''
    row = len(first)+len(second)
    coloum = 0

    if len(first)>0 and len(second)>0:   
        coloum = len(first[0])+len(second[0])
    final_2D=[]
    temp_r =[]
    temp_i = []
    if len(second)>0:   
        temp_i = ["I"]*(len(second[0])+3)##add one space in the middle
    
    for i in  first:
        temp_r = i + temp_i
        final_2D.append(temp_r)
    if len(first)>0:
        temp_i = ["I"]*(len(first[0])+3)
    final_2D.append(["I"]*(coloum+3))
    for i in  second:
        temp_r = temp_i + i
        final_2D.append(temp_r)
        
    print(final_2D)
    return final_2D

def connect_right_left(output1,output2,input1,input2,final_array):
    '''connect first intial state's output to second intial state input'''
    ##check whether output is in right or bottom 
    ##check input is in top and left
    ##example output of first is [4][5]   input is 【11】【9]
    ##should [4][5+1] then [4][5+1+1]~[11][5+!+1] then [11][9-1]
    if len(final_array)>output1:
        if len(final_array[output1])>output2+1:
            final_array[output1][output2+1]="B"


    for i in range (output1,input1+1):
        if len(final_array)>i:
            if len(final_array[i])>output2+3:
                final_array[i][output2+2]="B"
                final_array[input1][output2+3]="B"
    
    if len(final_array)>input1:
            if len(final_array[input1])>input2-1:
                final_array[input1][input2-1]="B"
                final_array[input1][input2]="B"
    
    print(final_array)
    return final_array
def connect_bottom_left(output1,output2,input1,input2,final_array):
    '''connect first intial state's output to second intial state input'''
    ##check whether output is in right or bottom 
    ##check input is in top and left
    ##example output of first is [4][5]   input is 【11】【9]
    ##should [5][5] then [5+1][5]~[11][5] then [11][6]~  [11][9-1]
    if len(final_array)>output1+1:
        if len(final_array[output1+1])>output2:
            final_array[output1+1][output2]="B"

    for i in range (output1,input1+1):
        if len(final_array)>i:
            if len(final_array[i])>output2:
                final_array[i][output2]="B"

    for i in range (output2,input2):
        if len(final_array)>input1:
            if len(final_array[input1])>i:
                final_array[input1][i]="B"

    print(final_array)
    return
def connect_bottom_top(output1,output2,input1,input2,final_array):
    '''connect first intial state's output to second intial state input'''
    ##check whether output is in right or bottom 
    ##check input is in top and left
    ##example output of first is [4][5]   input is 
    if len(final_array)>output1+1 and len(final_array)>input1-1:
            if len(final_array[input1-1])>input2 and len(final_array[output1+1])>output2 :
                final_array[output1+1][output2]="B"
                final_array[input1-1][input2]="B"

    for i in range (output1,input1+1):
        if len(final_array)>output1+1:
            if len(final_array[output1+1])>i:
                final_array[output1+1][i]="B"

    return
def connect_right_top(output1,output2,input1,input2,final_array):
    '''this is filling the wire to the right_top coordinate in the intial state'''
    if len(final_array)>output1 and len(final_array)>input1-1:
            if len(final_array[input1-1])>input2 and len(final_array[output1])>output2+1 :
                final_array[output1][output2+1]="B"
                final_array[input1-1][input2]="B"
                for i in range (output2,input2+1):
                    final_array[output1][i]="B"
                for i in range (output1,input1+1):
                    final_array[i][input2]="B"   
                    
    return

def init_state():
    '''this is to make gates' init_state together'''
    s=[]
    #initialist the state with I
    two_D_array = []
    #Declaring an empty 1D list.
    b_column = []
    #Initialize the column to Zeroes.
    for j in range(0, 20):
        b_column.append("I")
    #Append the column to each row.
    for i in range(0, 20):
        two_D_array.append(b_column)
    check = 0
    row = 0
    lastsize = 0
    for index, line in enumerate(file1):
        #read initial state in not gate file
        if "!START_INIT_STATE" in str(line):
            check = 1
        if ( "!END_INIT_STATE" in  str(line)) :
            break
        s = str(line).split(" ")
        
        for j in range(0, 20):
            for i in s :
                two_D_array[row][j] = i
                lastsize = lastsize +1
            row = row +1
    for index, line in enumerate(file3):
        #read initial state in not gate file
        if "!START_INIT_STATE" in str(line):
            check = 1
        if ( "!END_INIT_STATE" in  str(line)) :
            break
        s = str(line).split(" ")
        check2 = 0
        for j in range(lastsize, 20):
            for i in s :
                two_D_array[row][j] = i
            row = row +1   
        

if __name__ == "__main__":
    
    input_num=0
    for input_num in range(4):
        con = open("newconnection"+str(input_num)+".txt","r")#this file created from autotest.py
        fileout = open(r"Myfileout"+str(input_num)+".txt","w+")
        arrayout = open(r"checkarray.txt","w+")

        check = 0
        #set up the running setting
        fileout.write(str("# Run settings\n"))
        fileout.write(str("pixels_per_node    = 20\n"))
        fileout.write(str("speedup_factor     = 100\n"))
        fileout.write(str("max_duration       = 200\n"))
        fileout.write(str("debug              = False\n"))
        fileout.write(str("node_display       = Color\n"))
        fileout.write(str("fps                =60\n"))
        fileout.write(str("#rng_seed           = 123123123\n"))
        transition_rules = ""
        first_output = ""    
        first_output_r=0
        first_output_c=0
        first_input = ""
        first_input_r=0
        first_input_c=0
        and_first_input_r=0
        and_first_input_c=0
        first_size_r=0
        first_size_c=0
        sec_output_r=0
        sec_output_c=0
        sec_input_r=0
        sec_input_c=0
        sec_size_r=0
        sec_size_c=0
        output_r = 0
        output_c = 0

        s=[]
        s_no_space =[]
        gates=[]
        g=[]
        for index, line in enumerate(con):
            if "!START_GATE_SUMMARY"  in str(line):
                check = 1
            if ( "!END" in  str(line)) :
                break
            if check == 1 and "!START_GATE_SUMMARY" not in str(line):
                g = str(line).split(" ")
                gates.append(g[0])
        check= 0
        for index, line in enumerate(con):
            if "!START_CONNECTION"  in str(line):
                check = 1
            if ( "!END_CONNECTION" in  str(line)) :
                break
            if check == 1 and "!START_CONNECTION" not in str(line):
                g=[]
                g = str(line).split(" ")
                if len(g)>6:
                    first_output = g[2]
                    first_input = g[6]
        print(gates)
        check = 0
        file_1 = open(str(g[0])+".txt","r")
        for index, line in enumerate(file_1):
            #read color map in not gate file
            if "# Template"  in str(line):
                check = 1

            if ( "# END Template" in  str(line)) :
                break
            if check == 1 and "! FIRST_GATE_SIZE" in str(line) :
                s = str(line).split(",")
                for i in s:
                    if '\n' in i:
                        i = i.replace('\n','')
                    if i.isalnum():
                        s_no_space.append(i)
                first_size_r = s_no_space[0]
                first_size_c = s_no_space[1]
            if check == 1 and "! FIRST_OUTPUT_LOC" in str(line) and first_output == "FIRST_OUTPUT_LOC":
                s = str(line).split(",")
                for i in s:
                    if '\n' in i:
                        i = i.replace('\n','')
                    if i.isalnum():
                        s_no_space.append(i)
                first_output_r = s_no_space[2]
                first_output_c = s_no_space[3]
            if check == 1 and "! FIRST_INPUT_LOC" in str(line):
                s = str(line).split(",")
                for i in s:
                    if '\n' in i:
                        i = i.replace('\n','')
                    if i.isalnum():
                        s_no_space.append(i)
                first_input_r = s_no_space[4]
                first_input_c = s_no_space[5]
        check = 0
        file_2 = open(str(g[4])+".txt","rb")
        print(g[4])
        for index, line in enumerate(file_2):
            #read color map in not gate file
            print(line)
            if "# Template" in str(line):
                check = 1
            if ( "# END Template" in  str(line)) :
                break
            if check == 1 and "! SECOND_GATE_SIZE" in str(line):
                s = str(line).split(",")
                for i in s:
                    if '\\r\\n' in i:
                        i = i.replace('\\r\\n\'','')
                        print(i)
                    if '\n' in i:
                        i = i.replace('\n','')
                    if i.isalnum():
                        s_no_space.append(i)
                print(s_no_space)
                print(s)
                sec_size_r = s_no_space[6]
                sec_size_c = s_no_space[7]
                print(sec_size_r)
                print(sec_size_c)
            if check == 1 and "! SECOND_OUTPUT_LOC" in str(line):
                s = str(line).split(",")
                for i in s:
                    if '\\r\\n' in i:
                        i = i.replace('\\r\\n\'','')
                    if '\n' in i:
                        i = i.replace('\n','')
                    if i.isalnum():
                        s_no_space.append(i)
                sec_output_r = s_no_space[8]
                sec_output_c = s_no_space[9]
            if check == 1 and "! SECOND_INPUT_LOC" in str(line) and first_input  == "SECOND_INPUT_LOC":
                s = str(line).split(",")
                for i in s:
                    if '\\r\\n' in i:
                        i = i.replace('\\r\\n\'','')
                        print(i)
                    if '\n' in i:
                        i = i.replace('\n','')
                    if i.isalnum():
                        s_no_space.append(i)
                sec_input_r = s_no_space[10]
                sec_input_c = s_no_space[11]
            #if "! SECOND_INPUT_LOC" in str(line): Changed on 27/10/2022 debug connection to manifest
            if "! FIRST_INPUT_LOC" in str(line):
                s = str(line).split(",")
                for i in s:
                    if '\\r\\n' in i:
                        i = i.replace('\\r\\n\'','')
                        print(i)
                    if '\n' in i:
                        i = i.replace('\n','')
                    if i.isalnum():
                        s_no_space.append(i)
                and_first_input_r = s_no_space[12]
                and_first_input_c = s_no_space[13]
                print("and_first_input_r and c"+str(and_first_input_r)+str(and_first_input_c))
        #with draw external input and output
        
        check = 0
        file1 = open(str(g[0])+".txt","r")
        file3 = open(str(g[4])+".txt","r",encoding='utf-8')
        for line in file1:
            if "!START_TRANSITION_RULES" in str(line):
                check = 1
            if ( "!END_TRANSITION_RULES" in  str(line)) :
                break
            if check == 1: 
                transition_rules =  str(transition_rules)+" "+str(line)
                fileout.write(str(line))    
        check = 0
        for index, line in enumerate(file3):
            if "!START_TRANSITION_RULES" in str(line):
                check = 1
            if ( "!END_TRANSITION_RULES" in  str(line)) :
                break
            if check == 1 and "!START_TRANSITION_RULES" not in str(line):       
                if str(line) not in transition_rules:
                    fileout.write(str(line))
                    transition_rules =  str(transition_rules)+" "+str(line)
        #end of rules
        fileout.write(str("!END_TRANSITION_RULES\n"))   
    
        #color map
        color_map()
        check = 0
        
        print(first_output_r) 
        print(first_output_c)
        print(first_input_r)
        print(first_input_c)
        print(first_size_r)
        print(first_size_c)
        print(sec_output_r)
        print(sec_output_c)
        print(sec_input_r)
        print(sec_input_c)
        print(and_first_input_r)
        print(and_first_input_c)
        print(sec_size_r)
        print(sec_size_c)      
                
        a1 = top_left_of_the_gate_to_be_copied(file1)
        a2 = top_left_of_the_gate_to_be_copied(file3)
        print("this is a1")
        print(a1)
        print("this is a2")
        print(a2)
        check= 0
        for index, line in enumerate(con):
            if "!START_EXTERNAL_INPUT" in str(line):
                check = 1
            if ( "!END_EXTERNAL_INPUT" in  str(line)) :
                break
            if check == 1 and "!START_EXTERNAL_INPUT" not in str(line):
                gg=[]
                gg = str(line).split(" ")
                #g[3] is the input signal from external
                if len(gg)>3:
                    if '\n' in gg[3]:
                        gg[3] = gg[3].replace('\n','')
                    if gg[0]==g[0] and gg[2]=="FIRST_INPUT_LOC":
                        a1[int(first_input_r)][int(first_input_c)]=gg[3]
                       
                    if gg[0]==g[4] and gg[2]=="FIRST_INPUT_LOC":
                        a2[int(and_first_input_r)][int(and_first_input_c)]=gg[3]
                     
   
        f = top_left_destination_at_the_merged_gate(a1,a2)
        print(f)
        final_array = connect_right_left(int(first_output_r),int(first_output_c),int(first_input_r)+int(first_size_r)+1,int(first_input_c)+int(first_size_c)+3,f)#OUTPUTIN [4][2] INPUT IN [1][0] SIZE OF FIRSTIS [6][3]
 
        arrayout.write(str(final_array))
        arrayout.write(str(s_no_space))
        #init_state()
        check = 0
        for line in file1:
            if  "!START_INIT_STATE"  in  str(line):
                check = 1
            if check == 1:       
                fileout.write(str(line))
            if ( "!END_INIT_STATE" in  str(line)) :
                break
        fileout.write(str("!START_INIT_STATE\n")) 
        #write out initial state
        #print array
        for i in final_array:
            for j in i:
                fileout.write(str(j)+"  ")
            fileout.write("\n")
        fileout.write(str("!END_INIT_STATE\n"))   
        
        fileout.close()
        file1.close() 
        con.close()
        file3.close()
        arrayout.close()
        file_1.close()
        file_2.close()
        call_sys="python3 SurfaceCRNQueueSimulator.py -m Myfileout"+str(input_num)+".txt"
        os.system(call_sys)

