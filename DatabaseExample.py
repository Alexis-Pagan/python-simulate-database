#==============================================================================
# simulate a database using advanced Python
# Made by: Alexis I. Garcia Pagan
# Day: Jan 2, 2018
# Place: Puerto Rico, Vega Alta
#==============================================================================
class DatabaseSimulation(object):
    
   #simulate database 
   databaseTable = []
   
   @staticmethod
   def options():
       """ menu to user """
       print('1. Insert data\n')
       print('2. Read data\n')
       print('3. Update data\n')
       print('4. Delete data\n')
       print('5. Close Database Management System\n')

       user = int(input('Select an option: \n'))
       
       return user
# =============================================================================
#        user selected option for menu
# =============================================================================
   @classmethod    
   def callOp(self, selected):
       while selected != 5:
           if selected == 1:
               self.insert()
               print('Calling.. function insert()')
               selected = 0
               self.callOp(self.options())
           elif selected == 2:
               self.read()
               print('Calling.. function read()')
               selected = 0
               self.callOp(self.options())
           elif selected == 3:
               self.update()
               print('Calling.. function update()')
               selected = 0
               self.callOp(self.options())
           elif selected == 4:
               self.delete()
               print('Calling.. function delete()')
               selected = 0
               self.callOp(self.options())
           elif selected == 5:
              print('Closing Database Management System...')
              break
# =============================================================================
#       insert data if it does not exist       
# =============================================================================
   @classmethod
   def insert(self):
       param = input('Enter data to insert: \n')
       if param in self.databaseTable:
           print('Data exist... exiting()')
       else:
           count = 0
           self.databaseTable.insert(count,str(param))
           count += 1
           print('Inserted data: \n' + str(self.databaseTable[0]))
# =============================================================================
#      delete data if it does exist      
# =============================================================================
   @classmethod     
   def delete(self):
       param = input('Enter data to delete: \n')
       if param in self.databaseTable:
           self.databaseTable.remove(param)
           print('Removed...' + str(param))
       else: 
           print('Can not be removed, because it does not exist')
# =============================================================================
#     update data if it does exist and prompt user to enter the new data       
# =============================================================================
   @classmethod
   def update(self):
       param = input('Enter data to be update: \n')
       if param in self.databaseTable:
           new_param = input('Enter new data: \n')
           self.databaseTable.append(new_param)
           
           """ remove after update """
           
           self.databaseTable.remove(param)
           
           print('Update successfull and remove as well')
       else:
           print('Could not update the parameter')
# =============================================================================
#      read the requested data from database      
# =============================================================================
   @classmethod
   def read(self):
       param = input('Enter data you want to read: \n')
       if param in self.databaseTable:
           for x in self.databaseTable:
               if x == param:
                   print('\nRequested data: \n' + str(param))
       else: 
           print('Could not read element, because it does not exist')
           
#==============================================================================
# user enter data
#==============================================================================

#display options to user:
userSelected = DatabaseSimulation.options()
#enter option selected:
DatabaseSimulation.callOp(userSelected)