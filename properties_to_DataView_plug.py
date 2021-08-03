"""
################
The unofficial plugins DataView can show table view in Obsidian which is like the Database in Notion.
To create a table by the properties created in Notion databases, the lines of 'property:' should change to 'property::' in .md files.
This code modifies the 'property:' lines to 'property::' lines.
################
"""

import os
from re import compile, search

path = r'your nodes folder path' 
properties = ['property1','property2'] # your notion properties list

# file paths
root_files_path = []
for root , dirs, files in os.walk(path, True):
    for file in files:
        root_files_path.append(os.path.join(root,file))

# 'property:' -> 'property::' 
def properties_to_DataView_plug(line,properties):
    for text in properties:
        regex_text =  "^%s:\s(.+)" % text
        regex_text_result = search(regex_text,line)
        if regex_text_result:
            line = line.replace(text,text+':')
    return line


# main codes
for file_path in root_files_path:
    if file_path[-3:] == '.md':
        print('file_path',file_path)
        with open(file_path,'r',encoding = 'utf-8') as file:
            file = file.readlines()
        write_lines = []
        for line in file:
            line = properties_to_DataView_plug(line,properties)
            write_lines.append(line)
        with open(file_path,'w',encoding = 'utf-8') as file:
            file.writelines(write_lines)
