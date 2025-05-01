from collections import deque

class Solution(object):
    def maxTaskAssign(self, tasks, workers, pills, strength):
        tasks.sort()
        workers.sort()

        def can_finish(mid, pills):
            n = len(workers)
            i = 0
            queue = deque()

            for j in range(n - mid, n):  # pick the 'mid' strongest workers
                w = workers[j]

                # Push all tasks the current worker (with pill) can possibly do
                while i < mid and tasks[i] <= w + strength:
                    queue.append(tasks[i])
                    i += 1

                if not queue:
                    return False

                # If worker can do task without pill
                if queue[0] <= w:
                    queue.popleft()
                else:
                    # Otherwise, use a pill if available
                    if pills == 0:
                        return False
                    pills -= 1
                    queue.pop()  # use pill for hardest task in queue

            return True

        left = 0
        right = min(len(tasks), len(workers))

        while left < right:
            mid = (left + right + 1) // 2  # binary search midpoint

            if can_finish(mid, pills):
                left = mid
            else:
                right = mid - 1

        return left
