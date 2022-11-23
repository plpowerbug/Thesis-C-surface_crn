#this is a test file to test file read2gate.py
import os
from itertools import combinations, permutations
def num_to_bit(num):
    max_bit=2**(num)
    
    bit_list =[]
    i = 0
    for i in range(max_bit):
        bit = bin(i).replace("0b", "")
        while len(str(bit))<num:
            bit="0"+str(bit)
        bit_list.append(bit)
    return bit_list   


def test_1(input_num,f):
    
    signals = ['0','1']

    check= 0
    list_input = num_to_bit(input_num)

    print("helo")
    print(list_input)
    x = "FIRST_INPUT_LOC 1"
    y = "FIRST_INPUT_LOC 0"
    j = 0
    for input in list_input:
        print(input)
        new = open(r"newconnection"+str(j)+".txt","w+")
        f = open("connection.txt", "r+")
        j = j + 1
    # each sentence becomes an element in the list l
        l = f.readlines()
        # acts as a counter to know the
        # index of the element to be replaced
        c = 0 
        for i in l:  
            if (x in i)  and (len(input)>c):
                
                print(i)
                print(c)
                # Replacement carries the value
                # of the text to be replaced
                i = i.replace(x, "FIRST_INPUT_LOC "+input[c])
                c = c + 1
                #os.system('python3 read2gate.py')
                # changes are made in the list
    
            elif (y in i)  and (len(input)>c):

                # Replacement carries the valu
                # of the text to be replaced
                i = i.replace(y, "FIRST_INPUT_LOC "+input[c])
                c = c + 1
                # changes are made in the list
                #i = Replacement
                print (i)
        
            new.writelines(i)   
        print(l)
        new.close()
    f.close()


if __name__ == "__main__":
    input = open("connection.txt", "r+") 
  
    test_1(2,input)
    num_to_bit(4)
