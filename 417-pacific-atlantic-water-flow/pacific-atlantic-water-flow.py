class Solution:
    def pacificAtlantic(self, heights):
        if not heights or not heights[0]:
            return []

        m, n = len(heights), len(heights[0])

        pacific = set()
        atlantic = set()

        # Directions: up, down, left, right
        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        def dfs(r, c, visited):
            visited.add((r, c))

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                # Check bounds
                if 0 <= nr < m and 0 <= nc < n:
                    # Only flow to equal/higher cells (reverse logic)
                    if (nr, nc) not in visited and heights[nr][nc] >= heights[r][c]:
                        dfs(nr, nc, visited)

        # Start from Pacific Ocean (top row, left column)
        for c in range(n):
            dfs(0, c, pacific)
        for r in range(m):
            dfs(r, 0, pacific)

        # Start from Atlantic Ocean (bottom row, right column)
        for c in range(n):
            dfs(m - 1, c, atlantic)
        for r in range(m):
            dfs(r, n - 1, atlantic)

        # Cells reachable by both oceans
        result = list(pacific & atlantic)
        return [list(pair) for pair in result]
