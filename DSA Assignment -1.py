#!/usr/bin/env python
# coding: utf-8

# # Q1

# In[141]:


#Write a program to find all pairs of an integer array whose sum is equal to a given number?
def find(array, len, summ):
    for i in range(len):
        for j in range(i):
            if (array[i] + array[j]) == summ:
                print(array[i], array[j])
                print("Pairs whose sum is : ", summ)
                print("Array= ", array)

array = [9,2,6,5,7,4,8,3]
summ = 11

find(array, len(array), summ)


# # Q2

# In[37]:


#Write a program to reverse an array in place? In place means you cannot create a new array. You have to update the original array.
array=[20,12,23,25,24,26,23]
print("Before reversal Array is :",array)

array.reverse()
print("After reversing Array:",array)


# # Q3

# In[60]:


#Write a program to check if two strings are a rotation of each other?
def areRotations(string1, string2):
    size1 = len(string1)
    size2 = len(string2)
    temp = ''
 
    if size1 != size2:
        return 0
    temp = string1 + string1

    if string2 in temp: 
        return True
    else: 
        return False
string1 = "abac"
string2 = "caba"
 
if areRotations(string1, string2):
    print ("Strings are rotations of each other")
else:
    print ("Strings are not rotations of each other")


# # Q4

# In[63]:


#Write a program to print the first non-repeated character from a string?
String = "ashish"
for i in String:
    count = 0
    for j in String:
        if i == j:
            count+=1

        if count > 1:
            break
    if count == 1:
        print(i,end = " ")


# # Q5

# In[131]:


#Read about the Tower of Hanoi algorithm. Write a program to implement it.
def Tower_Of_Hanoi(n , source, destination, auxiliary):
    if n==1:
        print ("Disk Move 1 from source",source,"to Destination",destination)
        return
    Tower_Of_Hanoi(n-1, source, auxiliary, destination)
    print ("Disk Move",n,"from source",source,"to Destination",destination)
    Tower_Of_Hanoi(n-1, auxiliary, destination, source)
         
n = 3
Tower_Of_Hanoi(n,'A','B','C')


# # Q6

# In[121]:


# Read about infix, prefix, and postfix expressions. Write a program to convert postfix to prefix expression.
def Operators(x):
 
    if x == "+":
        return True
 
    if x == "-":
        return True
 
    if x == "/":
        return True
 
    if x == "*":
        return True
 
    return False
 
def postToPre(post_exp):
 
    s = []
    length = len(post_exp)
 
    for i in range(length):
 
        if (Operators(post_exp[i])):
 
            
            op1 = s[-1]
            s.pop()
            op2 = s[-1]
            s.pop()
 
            
            temp = post_exp[i] + op2 + op1
            s.append(temp)
 
        else:
            s.append(post_exp[i])
 
    
    ans = ""
    for i in s:
        ans += i
    return ans
 
 

if __name__ == "__main__":
 
    post_exp = "DY-FV+"
     
    
    print("Prefix : ", postToPre(post_exp))


# # Q7

# In[136]:


#Write a program to convert prefix expression to infix expression.
def prefix_To_Infix(prefix):
    stack = []
     
    
    i = len(prefix) - 1
    while i >= 0:
        if not Operator(prefix[i]):
             
        
            stack.append(prefix[i])
            i -= 1
        else:
           
            
            str = "(" + stack.pop() + prefix[i] + stack.pop() + ")"
            stack.append(str)
            i -= 1
     
    return stack.pop()
 
def Operator(c):
    if c == "*" or c == "+" or c == "-" or c == "/" or c == "^" or c == "(" or c == ")":
        return True
    else:
        return False
 

if __name__=="__main__":
    str = "*-K/BC-/JKM"
    print(prefix_To_Infix(str))


# # Q8

# In[70]:


#Write a program to check if all the brackets are closed in a given code snippet.
def Balanced_Bracket(expr):
    string = []
    for char in expr:
        if char in ["(", "{", "["]:
            string.append(char)
        else:
            
            if not string:
                return False
            current_char = string.pop()
            
            if current_char == '(':
                if char != ")":
                    return False
            
            if current_char == '{':
                if char != "}":
                    return False
            
            if current_char == '[':
                if char != "]":
                    return False
 
    if string:
        return False
    return True
 
if __name__ == "__main__":
    expr = "{}[]()"
 
    if Balanced_Bracket(expr):
        print("Balanced")
    else:
        print("Not Balanced")


# # Q9

# In[140]:


#Write a program to reverse a stack.
class Reerse_Stack:
    def __init__(self):
        self.items = []
    def check_empty(self):
        return self.items == []
    def push_val(self, data):
        self.items.append(data)
    def pop_val(self):
        return self.items.pop()
    def print_it(self):
        for data in reversed(self.items):
            print(data)

def insert_bottom(instance, data):
    if instance.check_empty():
        instance.push_val(data)
    else:
        deleted_elem = instance.pop_val()
        insert_bottom(instance, data)
        instance.push_val(deleted_elem)
def stack_reverse(instance):
    if not instance.check_empty():
        deleted_elem = instance.pop_val()
        stack_reverse(instance)
        insert_bottom(instance, deleted_elem)

my_instance = Stack_structure()
data_list = input('Enter the elements to add to the stack: ').split()
for data in data_list:
    my_instance.push_val(int(data))

print('The reversed stack is:')
my_instance.print_it()
stack_reverse(my_instance)
print('The stack is:')
my_instance.print_it()


# # Q10

# In[137]:


#. Write a program to find the smallest number using a stack.
list1 = [25,23,65,69,75,63,21]
list1.sort()
print("Smallest number is:", list1[0])

