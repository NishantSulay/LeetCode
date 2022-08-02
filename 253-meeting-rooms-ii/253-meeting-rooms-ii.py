class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        
        '''
        1.sort meeting by start time and end time 
        
        startTime = [0,5,15]
        endTime = [10,20,30]
 
        requiresMeetingRoom = 2
        currentMeeting = 3
        
        O(nlog(n))
        
        '''

        startTime = []
        endTime = [] 

        endTimeIdx = 0
        requiresMeetingRoom = 0 
        currentMeetingRoom = 0
        
        for i in range(len(intervals)):
            startTime += [intervals[i][0]]
            endTime += [intervals[i][1]]
            
            
        startTime.sort()
        endTime.sort()
        
        print(startTime)
        print(endTime)
        
        for i in range(len(startTime)):
            currentMeetingRoom += 1
            
            while(startTime[i] >= endTime[endTimeIdx]):              
                currentMeetingRoom -= 1 
                endTimeIdx += 1
            
    
            requiresMeetingRoom = max(requiresMeetingRoom, currentMeetingRoom)
            
        return requiresMeetingRoom
                
            