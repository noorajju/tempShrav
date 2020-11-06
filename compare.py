#!/usr/bin/env python
# coding: utf-8

import csv
print("Noor")
""" 
Python:3.6

Requirement: Search for each record in File1 is to be made in File2.
Concatenation of First five values in .csv makes the keys. 
An array of 6th to 10th element makes a value.
Key obtained from File1 is used to search record in File2. 
If the record is found then their corresponding Values are compared
The result of the search is saved in an out.csv file which is a copy of File1 
but has three additional columns for each record their definition is as,
['Key Found/Not Found', 'Value Match/Not_Match', 0/|Index_of_mismatched_element_in_file1| Value_of_Element_In_File_1|Value_of_Element_In_File_2]

"""
# This added on 11/6/2020
# This function makes a key_value pair (dictionary) from the input .csv files
def make_key_value(file_name):
    file_key_value = {}
    with open('{}.csv'.format(file_name), 'rt', newline='') as file:
        for i, r in enumerate(csv.reader(file)):
            file_key_value[''.join(r[0:d])]=r[5:n_cols]
    return file_key_value

# This function makes a key_value pair (dictionary) from the input .csv files
def create_output_array():
    global list_of_list
    with open('file1.csv','rt',newline='') as file:
        reader = csv.reader(file)
        for line in reader:
            list_of_list.append(line)

# This function first serches for each record from file1 in file2 based on key.
# Finds a match between values if key found.
# On every else: outputs corresponding value            
def compare_function():
    i = 0
    global list_of_list
    for k1,v1 in file1_key_value.items():
        if k1 in file2_key_value.keys():
            list_of_list[i].append('Key_Match')
            if v1==file2_key_value[k1]:
                list_of_list[i].append('Value_Match')
                list_of_list[i].append(0)
            else:  
                list_of_list[i].append('Value_Not_Match')
                value_error = "|"
                for index in range(5):
                    if v1[index]!=file2_key_value[k1][index]:
                        value_error = value_error+str(index)+"_"+v1[index]+"_"+file2_key_value[k1][index]+"|"
                list_of_list[i].append(value_error)           
        else:
            list_of_list[i].append('Key_Not_Found')
            list_of_list[i].append(0)
            list_of_list[i].append(0)
        i+=1

# Creates an output.csv similar to File1 with 3 additional columns
# ['Key Found/Not Found', 'Value Match/Not_Match', 0/|Index_of_mismatched_element_in_file1| Value_of_Element_In_File_1|Value_of_Element_In_File_2]

def write_to_result():
    global list_of_list
    with open("out.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(list_of_list)


#------------------------------------------------------------------------------------------------------------------------
# Code for this part has to be updated as per the configuration file.

n_cols = 10 #Number of columns
d = 5 # Number of first d columns that form keys
l = n_cols - d # Number of elements in value array
file1_key_value = make_key_value('file1')
file2_key_value = make_key_value('file2')
list_of_list = []
#------------------------------------------------------------------------------------------------------------------------


create_output_array()
compare_function()
write_to_result()





