class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        p = defaultdict(list)
        for course, prereq in prerequisites:
            p[course].append(prereq)
        
        # tracks courses we have already visited
        visited = set()
        def dfs(course):
            # cycle detected
            if course in visited: 
                return False

            # course has no prereqs
            if p[course] == []:
                return True
            
            visited.add(course)
            for crs in p[course]:
                if not dfs(crs):
                    return False
            visited.discard(course)
            p[course] = []
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True
        