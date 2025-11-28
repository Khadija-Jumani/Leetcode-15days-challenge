class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        from collections import defaultdict

        # Build adjacency list
        graph = defaultdict(list)
        for a, b in prerequisites:
            graph[b].append(a)

        # 0 = unvisited, 1 = visiting, 2 = visited
        visited = [0] * numCourses

        def dfs(course):
            if visited[course] == 1:   # currently in recursion stack → cycle
                return False
            if visited[course] == 2:   # already checked, no cycle
                return True

            visited[course] = 1  # mark as visiting

            for neighbor in graph[course]:
                if not dfs(neighbor):
                    return False

            visited[course] = 2  # mark as finished
            return True

        # check each course
        for c in range(numCourses):
            if not dfs(c):
                return False

        return True
