import statistics
class Arithmetics :
    def __init__(self, nums):
        self.nums = nums 
    # ================== Mean  =======================
    def mean(self):
       
        return sum(self.nums)/len(self.nums)
    # ================== Median  =======================
    def median(self):
        arr = self.nums 
        arr.sort() 
        if(len(arr)%2 != 0):
            return arr[len(arr)//2]
        else:
            n = arr[len(arr)//2]
            m = arr[len(arr)//2-1]
            return (n+m)/2
    #================== mode =======================
    def mode(self):
        m = dict()
        for i in self.nums:
            if( i not in m):
                m[i] = 1 
            else:
                m[i] += 1 
        ans = [(value, key) for key, value in m.items()]
        return (max(ans)[1])
    #================== standard_deviation  ==========
    def standard_deviation(self):
        return statistics.stdev(self.nums)


 

        
a = Arithmetics([1,1,1,2,2,3,4,5,66,78,100])

    
print("Mean is :- " + str(a.mean())) 

print("median is :- " + str(a.median())) 

print("mode is :- " + str(a.mode())) 

print("standard deviation is :- " + str(a.standard_deviation())) 