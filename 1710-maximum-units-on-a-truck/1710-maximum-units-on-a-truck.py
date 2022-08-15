class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        
        
        '''
        [[5,10],[2,5],[4,7],[3,9]]
        size = 10
        
        
        [[5,10],[3,9],[4,7],[2,5]]
        5*10 + 3*9 + 2*7 = 50 + 27 + 14 = 91
        
        1. sort by ascending units O(nlogn)
        2. iterate and subtract from total allowed boxes O(n)

        '''
        total = 0
        boxTypes.sort(key=lambda x:x[1], reverse=True)
        
        for boxType in boxTypes:      
            for box in range(boxType[0]):
                if truckSize == 0:
                     break
                truckSize -= 1
                total += boxType[1]
        
        return total 