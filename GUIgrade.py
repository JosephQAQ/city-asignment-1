import sys
import fileinput
import matplotlib.pyplot as plt
from tkinter import ttk
from Student import Student
from Student121 import Student121
from Student122 import Student122
import tkinter as tk
import tkinter.scrolledtext as tkst

class GUIgrade:

    student121DL=[]
    student122DL=[]
    
    def __init__(self, root, datafile):
        
        self.datafile = datafile
        self.root = root
        self.root.title("Grade Processing System")
        self.nb = ttk.Notebook(root)
        
        self.page0 = ttk.Frame(self.nb)
        
        self.editArea0 = tkst.ScrolledText(self.page0,height=15)
        self.editArea0.pack(expand=1, fill="both") 

        self.menuChoice0 = tk.IntVar()
        self.menuChoice0.set(0)
        self.menuItems0 = [('Display contents of input data file',0),
                    ('Display all valid input data for 121COM module',1),
                    ('Display all valid input data for 122COM module',2)]
        
        for (val, item) in enumerate(self.menuItems0):
            tk.Radiobutton(self.page0, 
                  text=item[0],
                  variable=self.menuChoice0,
                  command=self.showChoice0,
                  value=val).pack(anchor=tk.W)
        
        self.displayFile()
                       
        self.nb.add(self.page0, text='Data file') 
        
        self.nb.pack(expand=1, fill="both")


    def showChoice0(self):

        if self.menuChoice0.get() == 0:
            self.displayFile()
        elif self.menuChoice0.get() == 1:
            self.displayValidData('121')
        elif self.menuChoice0.get() == 2:
            self.displayValidData('122')

    def displayFile(self):
        self.editArea0.delete(1.0, tk.END) 
        self.editArea0.insert(tk.INSERT,'='*25+self.datafile+'='*25+'\n')
        for line in fileinput.input(self.datafile):
            self.editArea0.insert(tk.INSERT,line) 
                       
    def displayValidData(self,module):
        self.editArea0.delete(1.0, tk.END)
        if module == '121':            
            self.editArea0.insert(tk.INSERT,('%-10s%-10s%-15s%10s%10s%10s%10s\n'%('Module','Stud ID','Name','CW1 mark','Test mark','CW2 mark','Exam mark')))
            self.editArea0.insert(tk.INSERT,'='*75+'\n') 
        else:
            self.editArea0.insert(tk.INSERT,('%-10s%-10s%-15s%10s%10s%10s\n'%('Module','Stud ID','Name','CW1 mark','Test mark','CW2 mark')))
            self.editArea0.insert(tk.INSERT,'='*65+'\n')     
        
def main(argv):
    root = tk.Tk()
    GUIgrade(root,argv[1])
    root.mainloop()

if __name__ == '__main__':
    main(sys.argv)


