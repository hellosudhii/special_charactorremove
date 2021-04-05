# Sudhi Jose
import csv
import string
import os
_filelims = [];
def main():
    thisdir = os.getcwd()
    for r, d, f in os.walk(thisdir):
        for file in f:
            if file.endswith(".csv"):
                _filelims.append(os.path.join(r,file))
    for lims in _filelims:
        reader(lims,os.path.basename(lims))
def reader(filename,output_file):
    with open (filename,'r',encoding="utf-8") as csvfile:
        writers(csvfile,"out"+output_file)
def writers(csvfile,output_file):
    # add specail charactor
    remove_bar =  ["#","$"] 
    line = ''
    with open (output_file,"w",newline = "") as ofile:
        newf = csv.writer(ofile)
        for x in csvfile:
            line = str(x)
            for sp in remove_bar:
                line = str.replace(line,sp,'')
            print("output"+line)
            newf.writerow(line.split(','))
 
if __name__=="__main__":
    main()