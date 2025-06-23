class Solution(object):
    def kMirror(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: int
        """
        def is_pal_10(x):
            orig, rev = x, 0
            while x:
                rev = rev * 10 + x % 10
                x //= 10
            return rev == orig

        ans = 0
        found = 0
        length = 1

        while found < n:
            half = (length + 1) // 2
            start = 1 if half == 1 else k ** (half - 1)
            end = k ** half

            for prefix in range(start, end):
                # build the base-k palindrome from the prefix
                pal = prefix
                t = prefix // k if (length % 2) else prefix
                while t:
                    pal = pal * k + (t % k)
                    t //= k

                # if its decimal form is also a palindrome, include it
                if is_pal_10(pal):
                    ans += pal
                    found += 1
                    if found == n:
                        return ans

            length += 1

        return ans
        
        '''Approach
Generate base-k palindromes by length

For each target palindrome length L, split it into a “prefix” of ⌈L/2⌉ digits (in base k) and mirror those to form the full palindrome.
Convert each palindrome to decimal by repeatedly multiplying‐and‐adding digits in base k.

Test the decimal value for palindrome by reversing its decimal digits numerically (no string conversion).

Accumulate the sum of the first n that pass both checks and return it as soon as we hit n.'''