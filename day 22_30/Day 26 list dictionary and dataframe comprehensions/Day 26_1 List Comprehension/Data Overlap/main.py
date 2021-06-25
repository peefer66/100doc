'''
Create a list of the common numbers in the two text files
'''

file1_path = r'C:\Users\pfiel\Documents\Python\100doc\day 22_30\Day 26 List Comprehension\Data Overlap\file1.txt'
file2_path = r'C:\Users\pfiel\Documents\Python\100doc\day 22_30\Day 26 List Comprehension\Data Overlap\file2.txt'

# open and read both text files
with open(file1_path,'r') as f1:
    # strip the \n from each element and convert into an integer
    file_list1 = [int(i.strip()) for i in f1.readlines()]
    
with open(file2_path,'r') as f2:
    file_list2 = [int(i.strip()) for i in f2.readlines()]
    
# list the numbers common to each
result = [n for n in file_list1 if n in file_list2]

print(result)