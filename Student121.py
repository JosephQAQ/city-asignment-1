from Student import Student

'''
Student121 class 

Created on Feb 20, 2020

@author: dcywchan
'''
class Student121(Student):
    '''
    Student121 class to represent each 121COM student object
    '''
    numStudent = 0 # class variable to record number of student
    
    CW1weight = 0.2 # class variable of weights for the coursework 1
    CW2weight = 0.2 # class variable of weights for the coursework 2 
    CW3weight = 0.6 # class variable of weights for the coursework 3
    
    CWweight = 0.7 # class variable of weights for the coursework 
    EXweight = 0.3 # class variable of weights for the exam 
       
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
            - exam: exam mark
        '''
        studentRec = studentData.split('_')
        
        if len(studentRec) != 6:                                            
            raise ValueError('incorrect number of data in input line : ')
        elif studentRec[0] == '' or studentRec[1] == '':                    
            raise ValueError('Invalid Stude ID or Name :')
        elif float(studentRec[2]) < 0 or float(studentRec[2]) > 100 :      
            raise ValueError('Invalid Test mark :')
        elif float(studentRec[3]) < 0 or float(studentRec[3]) > 100 :      
            raise ValueError('Invalid CW1 mark :')
        elif float(studentRec[4]) < 0 or float(studentRec[4]) > 100 :      
            raise ValueError('Invalid CW2 mark :')
        elif float(studentRec[5]) < 0 or float(studentRec[5]) > 100 :      
            raise ValueError('Invalid Exam mark:')
        
        Student.__init__(self,studentRec[0],studentRec[1])
        
        Student121.numStudent += 1
        
        self.__test  = float(studentRec[2])
        self.__iAsgn = float(studentRec[3])
        self.__gAsgn = float(studentRec[4])
        self.__exam  = float(studentRec[5])
        
    def getTest(self):
        '''
        accessor method to get student test mark
        '''
        return self.__test
    
    def getIAsgmt(self):
        '''
        accessor method to get student nindividual assignment mark
        '''
        return self.__iAsgn
            
    def getGAsgmt(self):
        '''
        accessor method to get student group assignment mark
        '''
        return self.__gAsgn
    
    def getExam(self):
        '''
        accessor method to get student examination mark
        '''        
        return self.__exam  
    
    def getCoursework(self):
        '''
        accessor method to get student coursework mark
        '''              
        return Student121.CW1weight*self.getTest()+\
            Student121.CW2weight*self.getIAsgmt()+\
            Student121.CW3weight*self.getGAsgmt()
                   
    def overall(self):
        '''
        service method to calculate overall mark from the weighted sum of the coursework mark and the the exam mark
        '''
        return Student121.CWweight * self.getCoursework() + \
                Student121.EXweight * self.getExam()
           
    def __str__(self):
        '''
        String representation of student object
        '''
        return '%-10s%25s%10.2f%10.2f'%('121COM',Student.__str__(self),self.getCoursework(),self.getExam())
