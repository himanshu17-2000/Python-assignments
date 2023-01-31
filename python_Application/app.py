import sys
import os


class Bank:

    data = dict()

    def __init__(self):
        file = open(os.path.join(sys.path[0], 'data.csv'), mode='r')
        f = file.readlines()
        for i in f:
            temp = i.split(',')
            Bank.data[temp[0].lower()] = int(temp[1][:len(temp[1]) - 1])

    def read_file(self):
        
        print('\nreading file...............\n')
        
        file = open(os.path.join(sys.path[0], 'data.csv'), mode='r')
        f = file.readlines()
        for i in f:
            temp = i.split(',')
            Bank.data[temp[0].lower()] = int(temp[1][:len(temp[1]) - 1])
        print(Bank.data)
        
        print('\nFile read...............\n')
        

    def write_file(self):
        arr = []
        
        print('\nwriting file...............\n')
        for k, v in Bank.data.items():
            arr.append(str(k).lower()+','+str(v)+'\n')
        file = open(os.path.join(sys.path[0], 'data.csv'), mode='w')
        file.writelines(arr)
       
        print('\nfile written...............\n')
        

       

class Customer(Bank):
    def __init__(self):
        Bank.__init__(self)
        self.first_name = input("Enter Your first_name :- ")
        self.amount = 0
        self.bankobj = Bank() 

    def open_account(self):
        try:
            if self.first_name not in self.bankobj.data.keys() :
                
                print('\nopening account...............\n')
                
                self.bankobj.data[str(self.first_name).lower()] = int(self.amount)
                self.bankobj.write_file()
                print('\nOpened.................\n')
                
            else:
                 raise()
        except:
             
             print('\nCustomer , OpenAccount , User aleady Exists\n')
    def close_account(self):
        
                
                print('\nclosing account...............\n')
                
                del self.bankobj.data[str(self.first_name).lower()] 
                self.bankobj.write_file()
                
                print('\nclosed.................\n')
                
            
             
    def deposite(self):
        try:
            if(self.first_name in self.bankobj.data):
                self.amount = input("Enter Your amount:- ")
                
                print('\nDepositing ' + str(self.amount)+'....................\n' )
                
                self.bankobj.data[self.first_name] += int(self.amount)
                self.bankobj.write_file()
                
                print('\nDeposited ' + str(self.amount)+'....................\n' )
                
            else:
                raise()
        except:
            print('\nCustomer , deposite , User does not Exists\n')       
            
    def withdraw(self):
        
            try:
                if(self.first_name in self.bankobj.data):
                    self.amount = input("Enter Your amount:- ")
                    if(self.bankobj.data[self.first_name] >=  int(self.amount)):
                        print('\Withdrawning ' + str(self.amount)+'....................\n' )
                        
                        
                        self.bankobj.data[self.first_name] -= int(self.amount)
                        self.bankobj.write_file()
                        
                        print('\Withdrawn ' + str(self.amount)+'....................\n' )
                    else:
                        print("\nAmount is less in account , can not withdrawn\n")
                    
                else:   
                    raise()
            except:
                print('\nCustomer , withdraw , User does not Exists\n') 
    def transfer(self):
            try:
                transfer_to = input('Enter name to whom mony is transfered :- ')
                if(self.first_name in self.bankobj.data and transfer_to in self.bankobj.data):
                    self.amount = input("Enter Your amount:- ")
                    if(self.bankobj.data[self.first_name] >=  int(self.amount)):
                        print('\nTransferring ' + str(self.amount) + " to "+ transfer_to +'....................\n' )
                        
                        
                        self.bankobj.data[self.first_name] -= int(self.amount)
                        self.bankobj.data[transfer_to] += int(self.amount)
                        self.bankobj.write_file()
                        print('\nTransferred ' + str(self.amount) + " to "+ transfer_to +'....................\n' )
                    else:
                        print("\nAmount is less in account , can not Transfer \n")
                    
                else:   
                    raise()
            except:
                print('\nCustomer , withdraw , User does not Exists\n')


    def balance(self):
            try:
                if(self.first_name in self.bankobj.data):
                    
                    print('\nshowing balance...............\n')
                    
                    print(self.first_name , "->" , self.bankobj.data[self.first_name] )
                    
                    print('\n balance shown...............\n')
                    
                else:
                    raise()
            except:
                print('\nCustomer , balance , User does not Exists\n')         

if __name__ == "__main__":

    option = 0
    obj = Bank()
    while (True):
        
        print("\nWelcome to Badhiya Bank Tell me your Requirement\n")
        print("press 1 to Open the Bank Account ")
        print("press 2 to deposite in the Bank Account ")
        print("press 3 to Withdraw from the Bank Account ")
        print("press 4 to Balance from the Bank Account ")
        print("press 5 to Transfer money to the account ")
        print("press 6 to Delete the account ")
        print("press 0 to terminate the transactions ")  
        
        option = int(input("\nEnter what operation you want:- "))
        
        if (option == 1):
            p1 = Customer()
            try:

                p1.open_account()
            
            except:
                print('some expection in open account')
            continue

        elif (option == 2):
            p1 = Customer()
            try:
                p1.deposite()
            
            except:
                print('some expection in deposite')
            continue

        elif (option == 3):
            p1 = Customer()
            try:
                p1.withdraw()
            except:
                print('some expection in withdraw')
            continue
        elif(option == 4):
            p1 = Customer()
            try:
                p1.balance()
            except:
                print('some expection in balance')
            continue
        elif (option == 5):
            p1 = Customer()
            try:
                p1.transfer()
            
            except:
                print('some expection in transfer ')
            continue
        elif (option == 6):
            p1 = Customer()
            try:
                p1.close_account()
            except:
                print('some expection in close account ')
            continue

        elif(option == 0):
            print("\nTransaction Terminated\n")
            break
        else:
            continue
        
            
