# Pending

#TODO: Set column values to calculate a value based on other columns in the table
#TODO: Set row element to perform a function like sum
#TODO: Dynamically calculate various statistic values and show them with each update
#TODO: Export the table to a user desired format
#TODO: Import an exported table
#TODO: use python-prompt-toolkit to dynamically display the table in one side of the split screen and have a command window on the other
#TODO: Interchange columns
#TODO: Privatise methods that do not need to exposed to user

# Partially Completed



# Completed

#DONE: Exchange column element within column
#DONE: Update individual column element
#DONE: Insert a columnn in a table
#DONE: Insert a row and element to the table
#DONE: Add empty rows


from typing import OrderedDict
from tabulate import tabulate

bar = '\u0304'


class beau:

    data = OrderedDict()
    isUpdate = False
    nRow = 0
    nCol = 0
    m = 0

    def tab_print(self,fmt="fancy_grid"):
        """
        Displays Table and resets update flag

        :param fmt: Table format according to tabulate
        :returns: None
        :raises None
        """
        self.fmt = fmt
        print(tabulate(self.data, headers='keys',tablefmt=fmt,showindex=True))
        self.isUpdate = False  
    
    # Data Handling Functions

    def sanitize(self):
        """
        Clean up the table. Adds None elements and 
        """
        l = []
        for k in self.data.keys():
            l.append(len(self.data[k]))
        self.m = max(l)
        for k in self.data.keys():
            ln = len(self.data[k])
            if ln!=self.m:
                for r in range(0,self.m-ln):
                    self.data[k].append(None)
        # Update index
        # self.data["Index"]=list(range(0,self.m))

    
    """def ad_index(self,dicts):
        l = []
        self.dicts = dicts
        for k in self.dicts.keys():
            l.append(len(self.dicts[k]))
        self.m = max(l)
        k = []
        for i in range(0,self.m):
            k.append(i)
        self.data = {"Index":k}"""
    
    def dict_in(self,dic):
        """
        Use a dict as an input for beau

        :param dic: Dictionary with keys as column title and their values as data
        :returns: None
        :raises: None
        """
        self.dic = dic
        # self.ad_index(self.dic)
        self.data.update(self.dic)
        self.sanitize()
        self.isUpdate = True
    
    # Row and Column Operations

    def add_cl(self,label,dat=[]):
        """
        Add column to table

        :param label: Column title
        :param dat: Column data to be added
        :returns: 1 when operation successful, -1 if failed
        :raises None

        """
    
        if not self.data:
            # print("data empty")
            #self.ad_index({label:dat})
            pass
        if label in self.data:
            print("Label Exists")
            return -1
        self.data[label]=dat
        # print("here",self.data)
        self.nCol+=1
        self.sanitize()
        self.isUpdate=True
        return 1

    def add_rw_el(self,label,dat):
        """
        Add element to row

        :param label: Column title
        :param dat: element to be added
        :returns: None
        :raises None

        """
        self.data[label].append(dat)
        self.sanitize()
    
    def add_rw(self,dat):
        """
        Add a row to the table

        :param dat: List containing the elements to be added to each column
        :raises None
        :returns None

        """
        # self.dat = dat
        i = 0
        if type(dat)==list:
            for k in self.data.keys():
                if k=="Index":
                    continue
                self.data[k].append(dat[i])
                i+=1
        self.sanitize()
        self.isUpdate=True
    
    def add_emp_row(self,n=1):
        """
        Add empty row to table

        :param n: Number oe empty rows to add
        :raises None
        :returns None
        """
        self.n=n
        for i in range(0,self.n):
            self.add_rw([None]*self.nCol)
    
    def update_el(self,label,index,dat):
        """
        Update an element of a column

        :param label: Column header
        :param index: Element index
        :param dat: New Element data
        :raises None
        :returns None
        """

        self.data[label][index] = dat
        self.isUpdate=True
    
    def ex_cl_el(self,label,Sin,Din):
        """
        Exchange elements of a column

        :param label: Column name
        :param Sin: Source element index
        :param Din: Destination element index
        :raises None
        :returns None
        """

        self.data[label][Sin],self.data[label][Din] = self.data[label][Din],self.data[label][Sin]
    
    def ex_cl(self,Sl,Dl):
        """
        Exchange column of table

        :param Sl: Label of Source Column
        :param Dl: Label of Destination Column
        :raises None
        :returns None
        """
        i=0
        Si=0
        Di=0
        for k,i in self.data.keys(),list(range(0,len(self.data.keys()))):
            if Sl == k:
                Si = i
            elif Dl == k:
                Di = i
            else:
                i+=1
            print(i,Si,Di)




"""Test Code"""
b = beau()
ret = b.add_cl('x',[1,2,3,4])
#print("return",ret)
# b.add_cl('x',[3,4,5,6])
ret = b.add_cl("y",[3,4,5,6])
#print("return",ret)
# b.tab_print()
#print(b.data)
b.add_rw_el("x",5)
b.add_rw([5,4])
#b.tab_print()
b.add_rw([7,8])
b.add_emp_row(2)
b.ex_cl_el("x",2,4)
b.tab_print()
b.ex_cl("x","y")
