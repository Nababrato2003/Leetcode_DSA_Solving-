class Solution(object):
    def maxDistance(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        moves = defaultdict(int)
        res = 0

        for c in s:
            moves[c] += 1
            
            min_vertical = moves["S"] if moves["S"] < moves["N"] else moves["N"]
            min_horizontal = moves["E"] if moves["E"] < moves["W"] else moves["W"]
            
            max_vertical = moves["S"] if moves["S"] > moves["N"] else moves["N"]
            max_horizontal = moves["E"] if moves["E"] > moves["W"] else moves["W"]

            forward = max_vertical + max_horizontal
            backward = min_vertical + min_horizontal
            
            change_direction = min(backward, k)
            backward -= change_direction
            forward += change_direction

            res = max(res, forward-backward)

        return res
        