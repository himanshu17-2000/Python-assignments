from datetime import date 
# ====================== Function ===================== 
def in_between_date(start , end , target):
    s = date(start[0] , start[1], start[2])
    e = date(end[0] , end[1], end[2])
    t = date(target[0] , target[1], target[2])

    print("yes in between") if (start < target < end) else print("Not in between")


    
# ======================== main =======================
print("Enter The start Date with yyyy/mm/dd seperated by space")

start = list(map(int , input().split()))

print("Enter The End Date with yyyy/mm/dd seperated by space")

end = list(map(int , input().split()))


print("Enter The Target Date with yyyy/mm/dd seperated by space")

target = list(map(int , input().split()))

in_between_date(start , end , target) 

