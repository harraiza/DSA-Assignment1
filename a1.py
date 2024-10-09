#===================================
#===================================
# Name   : Ahmed Hamza
# Roll no: 271047758
# Section: C
#===================================
#===================================

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
        selection_tuple=()
        for i in range(self.selction[0],self.selction[2]+1):
            for j in range(self.selction[1],self.selction[3]+1):
                selection_tuple+=(self.sheet[i][j])
        self.selected_vals=selection_tuple
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
    def Undo(self):
        '''
        Undoes the previous action by user.
 
        Parameters:
            None
        
        Return value:
            None 

        '''
        
        raise NotImplementedError

#----------------------

    def Redo(self):
        '''
        Redoes the previous action undone by user.
 
        Parameters:
            None
        
        Return value:
            None 

        '''
        
        raise NotImplementedError

#----------------------

    def Save(self, fileName):
        '''
        Saves the spreadsheet to a file with name given as Parameter
 
        Parameters:
            fileName
        
        Return value:
            None 

        '''
        
        raise NotImplementedError

#----------------------

    def Load(self, fileName):
        '''
        Loads the spreadsheet from a file with name given as Parameter
 
        Parameters:
            fileName
        
        Return value:
            None 

        '''
        
        raise NotImplementedError
                
#======================


#======================
#======================
#
#    DRIVER FUNCTION
#
#======================

def main():
    # -----------------------------
    # Implement your own logic here:
    # -----------------------------
    sheet = Spreadsheet()
    sheet.CreateSheet(7,7)
    #
    while True:
        sheet.Goto(0,0)
        sheet.Insert(4)
        sheet.Goto(1,1)
        sheet.Insert(5)
        sheet.Goto(2,6)
        sheet.Insert(6)
        sheet.PrintSheet()
        break
    
def display_ui():
    print("0 to Quit")
    print("1 to Go to New Cell")
    print("2 to Insert at Current Cell")
    print("3 to Delete Value of Current Cell")
    print("4 to Read Current Cell")
    print("5 to Create New Selection")
    print("6 to Read Current Selection")
if __name__ == '__main__':
    main()
    
#======================


