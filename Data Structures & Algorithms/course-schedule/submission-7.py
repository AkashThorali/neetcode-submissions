class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # build a hashmap
        prereq = defaultdict(list)
        for i in prerequisites: 
            prereq[i[0]].append(i[1])

        visited = set()
        def dfs(course):
            if course in visited:
                return False
            if prereq[course] == []:
                return True
            
            visited.add(course)
            for i in prereq[course]:
                if not dfs(i):
                    return False
            visited.discard(course)
            prereq[course] = []
            return True
            
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True
        