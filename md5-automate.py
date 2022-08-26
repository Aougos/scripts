import hashlib
import pandas as pd
import csv

def converter():
    # adjust the file path 
    data = pd.read_csv("[file-path]")
    
    # adjust which of the data in the file that you want to be process based on the header
    temp = []
    for x in range(len(data.[column])):
        hash = hashlib.md5(data.[column][x].encode()).hexdigest()
        temp.append(hash)
    
    # adjust file output path, where is the data go out
    with open('[file-output]', 'w') as out:
        for row in temp:
            out.write("%s\n" % row)

if __name__ == '__main__':
    converter()