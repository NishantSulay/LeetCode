class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        
        #topological sort
        
        adjList = collections.defaultdict(list)
        inDegree = [0] * numCourses
        
        for child, parent in prerequisites:
            adjList[parent].append(child)
            inDegree[child] += 1 
            
        queue = deque()
        
        for course, count in enumerate(inDegree):
            if count == 0:
                queue.append(course)
                
        courseSeq = set()
        while queue:
            course = queue.popleft()
            courseSeq.add(course)
            for neighbour in adjList[course]:
                inDegree[neighbour] -= 1
                if inDegree[neighbour] == 0:
                    queue.append(neighbour)
                    
        return len(courseSeq) == numCourses
                
        