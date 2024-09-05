from Student import Student

class Student122(Student):
    '''
    Student122 class to represent each 122COM student object
    '''
    numStudent = 0 # class variable to record number of student
    
    CW1weight = 0.25 # class variable for weights for the coursework 1
    CW2weight = 0.25 # class variable for weights for the coursework 2 
    CW3weight = 0.5 # class variable for weights for the coursework 3
    
    CWweight = 1.0 # class variable for weights for the coursework 

       
    def __init__(self,studentData):
        '''
        constructor method
        
        Parameters:
        - studentData with following data feilds
            - studID: student ID
            - name: name of student
            - test: test mark
            - iAsgn: individual assignment mark
            - gAsgn: group assignment mark
        '''
        
        pass