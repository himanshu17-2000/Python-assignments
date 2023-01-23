class Loan:
    
    def __init__(s , name, age , salary ):
        s.name = name
        s.age = age 
        s.salary =salary  
    
    def give_loan(self):
        try:
            if(self.salary < 10000):
               
                raise Exception()
        except:
            print(self.name + "Loan not approved as salary is less  :'( ")
        else:
            print(self.name + " Your loan has been approved")


a = Loan("Himanshu" , 32 , 2500)

a.give_loan() 
print()


b = Loan("Avni" , 23 , 250000)

b.give_loan()