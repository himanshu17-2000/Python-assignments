class Voter:
    candidates = ['Trump' , 'gandhi' , 'Modi' , 'Putin']

    def __init__(s , name, age , number ):
        s.name = name
        s.age = age 
        s.number =number  
    
    def give_vote(self):
        try:
            if(self.age < 18):
               
                raise Exception()
        except:
            print(self.name + " You Are below Age limit ")
        else:
            print()
            print(self.name + " Here are your candidates ", Voter.candidates ," press index of your candidate to cast your vote")
            print()
            n = int(input("Enter the index ->  "))
            print(f"{self.name} you casted your vote to " , Voter.candidates[n] ," See your next time")
            

     


a = Voter('Himanshu' , 14 , '548795847')

a.give_vote()


b = Voter('Sherliy' , 22 , "8787545421")
b.give_vote()

