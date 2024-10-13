#===================================
#===================================
# Name   : Ahmed Hamza
# Roll no: 271047758
# Section: C
#===================================
#===================================
import pickle
import copy
class Spreadsheet:
    def __init__(self):
        '''
        Predefined member variables. 
        
        WARNING:DO NOT MODIFY THE FOLLOWING VARIABLES
        '''
        self.sheet = None   # 2D array of values
        self.rows = 0       
        self.cols = 0
        self.cursor=[0,0]   # cursor's current position
        self.selction = [None, None, None, None]
        
        #======================
        # Insert your Member
        #   variables here (if any):
        #----------------------
        self.undo_stack=[]
        self.redo_stack=[]
        self.selected_vals=[]
        #======================
        
#======================
    def CreateSheet(self, rows, cols):
        '''
        Creates a new 2 dimensional array assigned
          to the self.sheet member variable.
        Initialize the 2D array with 'None' type.
 
        Parameters:
            rows --> total number of rows in this spreadsheet
            cols --> total number of cols in this spreadsheet
        
        Return value:
            None
        '''
        rowlist=[]
        for i in range(rows):
            collist=[]
            for j in range(cols):
                collist.append(None)
            rowlist.append(collist)
        
        self.sheet=rowlist
        self.undo_stack_append()
        #raise NotImplementedError
#======================

#======================
    def Goto(self, row, col):
        '''
        Moves the cursor to the location indicated by the 
          row and col parameters
 
        Parameters:
            row --> row number to move to
            col --> column number to move to
        
        Return value:
            None
        '''
        try:
            if self.sheet!=None:
                self.cursor=[row,col]
            else:
                print("Sheet not created yet")
        except:
            print("Out of Bound error")
        
        #raise NotImplementedError
#======================

#======================        
    def Insert(self, val):
        '''
        Inserts value at the position indicated by the cursor.
 
        Parameters:
            val --> value to be inserted at the cursor location
        
        Return value:
            None
        '''
        if self.sheet!=None:
            self.undo_stack_append()
            self.sheet[self.cursor[0]][self.cursor[1]]=val
        else:
            print("Sheet not created")
        
        #raise NotImplementedError
#======================

#======================        
    def Delete(self):
        '''
        Deletes a value from the position indicated by the cursor.
 
        Parameters:
            None
        
        Return value:
            None
        '''
        self.undo_stack_append()
        self.sheet[self.cursor[0]][self.cursor[1]]=None
        
        #raise NotImplementedError
#======================

#======================    
    def ReadVal(self):
        '''
        Prints the value from the position indicated by the cursor.
 
        Parameters:
            None
        
        Return value:
            value stored at the cursor location 

        '''
        print(self.sheet[self.cursor[0]][self.cursor[1]])
        return self.sheet[self.cursor[0]][self.cursor[1]]
        #raise NotImplementedError
#======================

#======================    
    def Select(self,row, col):   
        '''
        Selects values between the position indicated in arguments with row and col and the position indicated by the cursor
 
        Parameters:
            row --> Row number to be selected 
            col --> Column number to be selected
        
        Return value:
            None
        '''
        self.selction[0]=self.cursor[0]
        self.selction[1]=self.cursor[1]
        self.selction[2]=row
        self.selction[3]=col
        selection_list=[]
        for i in range(self.selction[0],self.selction[2]+1):
            for j in range(self.selction[1],self.selction[3]+1):
                if self.sheet[i][j]!=None:
                    selection_list.append(self.sheet[i][j])
        self.selected_vals=selection_list
        #raise NotImplementedError
#======================

#======================        
    def GetSelection(self):
        '''
        Returns a tuple with current selecion cooridnates
        Parameters:
            None
        
        Return value:
            Returns a tuple with row and column of the selection:
                position 1 of the tuple indicates the stating row of the selection
                position 2 of the tuple indicates the stating col of the selection
                position 3 of the tuple indicates the ending row of the selection
                position 4 of the tuple indicates the ending col of the selection
            
            Example: (1,1,3,4)
        '''
        return tuple(self.selction)

        #raise NotImplementedError
#======================

#======================        
    def Sum(self,row,col):
        '''
        Stores the sum of the values in the current selection at the position indicated in arguments
        Parameters:
            row --> Row number to store the sum
            col --> Column number to store the sum
        
        Return value:
            None
        '''
        self.undo_stack_append()
        self.sheet[row][col]=sum(self.selected_vals)
        
        #raise NotImplementedError
#======================

#======================    
    def Mul(self,row,col):
        '''
        Stores the product of the values in the current selection at the position indicated in arguments
        Parameters:
            row --> Row number to store the product
            col --> Column number to store the product
        
        Return value:
            None
        '''   
        prod=1
        for i in self.selected_vals:
            prod=prod*i
        self.undo_stack_append()
        self.sheet[row][col]=prod    
        
        #raise NotImplementedError
#======================

#======================        
    def Avg(self,row,col):
        '''
        Stores the average of the values in the current selection at the position indicated in arguments
        Parameters:
            row --> Row number to store the average
            col --> Column number to store the average
        
        Return value:
            None
        '''
        self.undo_stack_append()
        self.sheet[row][col]=sum(self.selected_vals)/len(self.selected_vals)   
        
        #raise NotImplementedError
#======================

#======================
    def Max(self,row, col):
        '''
        Stores the maximum of the values in the current selection at the position indicated in arguments
        Parameters:
            row --> Row number to store the maximum
            col --> Column number to store the maximum
        
        Return value:
            None
        '''        
        
        self.undo_stack_append()
        self.sheet[row][col]=max(self.selected_vals)

        
        #raise NotImplementedError
#======================

#======================
    def PrintSheet(self):
        '''
        Prints the sheet in a human readable from
        Parameters:
            None
        Return value:
            None    

        Note: This is an example output your values will differ
        PrintSheet()
        row/col:    0   1   2   3   4
            0       
            1   
            2           10               
            3                   12
            4 
        '''
        for i in self.sheet: 
            for j in i:
                if j!=None:
                    print(j,end="\t")
                else:
                    print("_",end="\t")
            print()
       #raise NotImplementedError
#======================

            
#======================
#======================
#    BONUS
#======================
    def undo_stack_append(self):
        self.undo_stack.append(copy.deepcopy(self))

    def redo_stack_append(self):
        self.redo_stack.append(copy.deepcopy(self))

    def Undo(self):
        if len(self.undo_stack)<1:
            print("Stack empty")
        else:
            self.redo_stack_append()
            copystack=self.redo_stack
            self.__dict__=self.undo_stack.pop().__dict__
            self.redo_stack=copystack
            
        '''
        Undoes the previous action by user.
 
        Parameters:
            None
        
        Return value:
            None 

        '''
        
        #raise NotImplementedError

#----------------------


    def Redo(self):
        if len(self.redo_stack)<1:
            print("Stack empty")
        else:
            self.undo_stack_append()
            self.__dict__=self.redo_stack.pop().__dict__

        '''
        Redoes the previous action undone by user.
 
        Parameters:
            None
        
        Return value:
            None 

        '''
        
        #raise NotImplementedError

#----------------------

    def Save(self, fileName):
        '''
        Saves the spreadsheet to a file with name given as Parameter
 
        Parameters:
            fileName
        
        Return value:
            None 

        '''
        try: 
            with open (f"{fileName}.txt","wb") as file:
                self.redo_stack=[]
                self.undo_stack=[]
                pickle.dump(self,file)
        except:
            print("File not saved")
        #raise NotImplementedError

#----------------------

    def Load(self, fileName):
        '''
        Loads the spreadsheet from a file with name given as Parameter
 
        Parameters:
            fileName
        
        Return value:
            None 

        '''
        try: 
            with open (f"{fileName}.txt","rb") as file:
                self.__dict__=pickle.load(file).__dict__
        except:
            print("File not loaded")
        #raise NotImplementedError
                
#======================


#======================
#======================
#
#    DRIVER FUNCTION
#
#======================

def display_ui():
    print("0 to Quit")
    print("1 to Go to New Cell")
    print("2 to Insert at Current Cell")
    print("3 to Delete Value of Current Cell")
    print("4 to Read Current Cell")
    print("5 to Create New Selection")
    print("6 to Read Current Selection")
    print("7 to Add Sum of Current Selection to Current Cell")
    print("8 to Add Product of Current Selection to Current Cell")
    print("9 to Add Average of Current Selection to Current Cell")
    print("10 to Add Maximum of Current Selection to Current Cell")
    print("11 to Print Sheet")
    print("12 to Undo")
    print("13 to Redo")
    print("14 to Save File")
    print("15 to Load File")
    option=input("Enter option:")
    return option

def main():
    # -----------------------------
    # Implement your own logic here:
    # -----------------------------
    sheet = Spreadsheet()
    x=int(input("enter sheet width"))
    y=int(input("enter sheet height"))
    sheet.CreateSheet(x,y)
    #
    while True:
        option=display_ui()
        if option=="1":
            x=int(input("enter cell row: "))
            y=int(input("enter sheet column: "))
            sheet.Goto(x,y)
        elif option=="0":
            print("Quiting")
            break
        elif option=="2":
            val=int(input("enter value: "))
            sheet.Insert(val)
        elif option=="3":
            sheet.Delete()
        elif option=="4":
            sheet.ReadVal()
        elif option=="5":
            nx=int(input("enter cell row(should be greater than the current cell): "))
            ny=int(input("enter cell column(should be greater than the current cell): "))
            sheet.Select(nx,ny)
        elif option=="7":
            nx=int(input("enter cell row: "))
            ny=int(input("enter cell column: "))
            sheet.Sum(nx,ny)
        elif option=="6":
            print(sheet.GetSelection())
        elif option=="8":
            nx=int(input("enter cell row: "))
            ny=int(input("enter cell column: "))
            sheet.Mul(nx,ny)
        elif option=="9":
            nx=int(input("enter cell row: "))
            ny=int(input("enter cell column: "))
            sheet.Avg()
        elif option=="10":
            nx=int(input("enter cell row: "))
            ny=int(input("enter cell column: "))
            sheet.Max(nx,ny)
        elif option=="11":
            sheet.PrintSheet()
        elif option=="12":
            sheet.Undo()
        elif option=="13":
            sheet.Redo
        elif option=="14":
            file=input("enter file name: ")
            sheet.Save(file)
        elif option=="15":
            file=input("enter file name: ")
            sheet.Load(file)
        else:
            print("option invalid")
if __name__ == '__main__':
    main()
    
#======================


