class Binary:
    def __init__(self, array,target):
        self.array = array
        self.target = target
    def binary_search(self, start, end):
        if end-start<=1:
            if self.array[start] == self.target:
                return start
            elif self.array[end] == self.target:
                return end
            else:
                return -1
        middle = (start+end)//2
        if self.array[middle]>self.target:
            return self.binary_search(start,middle)
        return self.binary_search(middle,end)

array = [1,2,5,7,9,10,81]
target = 7
obj = Binary(array,target)
print(obj.binary_search(0,len(array)-1))