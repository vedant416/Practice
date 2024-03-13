class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
            elder_count = [0] * numCourses
            for elder in prerequisites:
                elder_count[elder[1]] += 1

            # Initialize a queue for topological sorting
            queue = []
            for i in range(numCourses):
                if elder_count[i] == 0:
                    queue.append(i)

            # Perform topological sorting
            visited_count = 0
            while queue:
                current = queue.pop(0)
                visited_count += 1
                for elder in prerequisites:
                    if elder[0] == current:
                        elder_count[elder[1]] -= 1
                        if elder_count[elder[1]] == 0:
                            queue.append(elder[1])

            # If all houses are visited, return 'YES'; otherwise, return 'NO'
            return visited_count == numCourses
        