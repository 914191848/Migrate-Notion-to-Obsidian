# Migrate-Notion-to-Obsidian
Migrate Notion to Obsidian

# properties_to_DataView_plug

The unofficial plugins **[DataView](https://github.com/blacksmithgu/obsidian-dataview)** can show table view in **[Obsidian](https://obsidian.md/)** which is like the Database in **[Notion](https://www.notion.so)**.

To create a table by the properties created in Notion databases, the lines of 'property:' should change to 'property::' in .md files.

This code modifies the 'property:' lines to 'property::' lines.
##'property:'&'property::' lines
### 'property:' lines in Notion Export md files
``` md
Date: June 12, 2021 4:11 PM
Tags: #abc
```

### 'property::' lines for Dataview usage
``` md
Date:: June 12, 2021 4:11 PM
Tags:: #abc
```

## Usage
1. Backup your files!!!
2. Modify following lines to you need:
    path = r'your nodes folder path' 
    properties = ['property1','property2,'] # your notion properties list
3. Run
