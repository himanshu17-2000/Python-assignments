import sys 
import os 

class Bank:

    data = dict() 

    def read_file(self):
        file = open(os.path.join(sys.path[0],'data.csv') , mode='r' )
        f = file.readlines() 
        
        for i in f:
            temp = i.split(',')
            Bank.data[temp[0]] = int(temp[1][:len(temp[1]) -1 ])
        print(Bank.data)

    def write_file(self):
        print(Bank.data) 

    def open_account(self):
        # file = open(os.path.join(sys.path[0],'data.csv') , mode='w' )
        pass 

if __name__ == "__main__":
    
    option = 0 
    obj = Bank()
    obj.read_file()
    while(True):
        print("Welcome to Badhiya Bank Tell me your Requirement")
        print("press 1 to Open the Bank Account ")
        print("press 2 to deposite in the Bank Account ")
        print("press 3 to Withdraw from the Bank Account ")
        # print("press 4 to Transfer ammount from one to another ") 
        print("press 5 to terminate the transactions ")
        option = int(input())
        try:
            if(option == 1 ):
                continue
            elif(option == 2) :
                continue
            elif(option == 3) :
                continue
            elif(option == 5 ):
                print("Transaction Termination")
                break
            else:
                raise('Exception')
        except:
            print("Invalid Number Entered")
            continue


