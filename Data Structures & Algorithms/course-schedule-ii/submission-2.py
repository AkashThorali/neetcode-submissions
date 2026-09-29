class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        pre_map = defaultdict(list)
        for course, pre in prerequisites: 
            pre_map[course].append(pre)

        res = []
        visited, cycle = set(), set()

        def dfs(course):
            if course in cycle: 
                return False
            if course in visited: 
                return True
            
            cycle.add(course)
            for pre in pre_map[course]:
                if dfs(pre) == False:
                    return False
            cycle.remove(course)
            visited.add(course)
            res.append(course)
            return True
        
        for i in range(numCourses):
            if dfs(i) == False: 
                return []
        return res
        