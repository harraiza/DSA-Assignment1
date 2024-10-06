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
        
        raise NotImplementedError
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
        
        raise NotImplementedError
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
        
        raise NotImplementedError
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

        raise NotImplementedError
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
        
        raise NotImplementedError
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

        raise NotImplementedError
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
        
        raise NotImplementedError
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
        
        raise NotImplementedError
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
             
        raise NotImplementedError
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
           
        raise NotImplementedError
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
        
        raise NotImplementedError
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
        
        raise NotImplementedError
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
    # sheet.CreateSheet(5,5)
    #
    # while True:
    #     sheet.Goto(2,2)
    #     sheet.insert(4)
    #     sheet.Print()
    

if __name__ == '__main__':
    main()
    
#======================


