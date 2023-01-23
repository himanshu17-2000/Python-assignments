import datetime 
def difference():
    print('Enter The first date time seperated by - ') 
    time1 = [int(i) for i in list(input().split('-'))] 
    print('Enter The second date time seperated by - ') 
    time2 = [int(i) for i in list(input().split('-'))] 
    a = datetime.datetime(time1[0],time1[1],time1[2] , time1[3],time1[4],time1[5])
    b = datetime.datetime(time2[0],time2[1],time2[2] , time2[3],time2[4],time2[5])
    print('diffrence = ' , b-a) 
    
difference() 
    
  

