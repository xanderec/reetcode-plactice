class Solution1:
    """
    Intuition:
        We use a bottom-up tabulation approach.

        Our base case is the empty subsequence "" for which there is only
        1 way for form.

        At each char, we have the choice to either append it to our existing
        subsequences or to skip it. We can naively append it to every sub-
        sequences we have found so far, leading to double the number of
        distinct subsequences i.e. dp[i] = 2 * dp[i - 1]. However, in doing
        so we double count previous subsequences ending in the same char.
        To subtract those, we need to track the index of the last occurrence
        of the character and subtract the number of distinct subsequences at
        that index.

        Thus, the recurrence relation becomes:

            dp[i] = (2 * dp[i - 1]) - dp[last[s[i]]]

    Runtime:
        O(n) for the linear scan.

    Memory:
        O(n) for the tabulated cache.

        O(n) for the hashmap tracking last index for each char.

        Overall, O(n) memory.
    """

    def distinctSubseqII(self, s: str) -> int:
        # cache: how many distinct subseqs in s[:i]
        # base case: there is 1 way to choose nothing
        dp = [1]
        # track last pos of last occurence of each char
        last = {}

        for ix, char in enumerate(s):
            # append curr char to every existing subseq,
            # leading to dp[-1] new subseqs
            dp.append(dp[-1] * 2)
            # if there are previous subseqs that ended w
            # same char as curr char, then we have double
            # counted. remove by subtracting num of distinct
            # subseqs at last ix of curr char
            if char in last:
                dp[-1] -= dp[last[char]]
            # update last occurrence of curr char
            last[char] = ix

        # -1 because we exclude the empty subseq base case ""
        return (dp[-1] - 1) % (10**9 + 7)


class Solution2:
    """
    Intuition:
        Same intuition as Solution 1.

        Notice how in the recurrence relation, state i only depends on state i - 1
        and the number of distinct subseqs at the last occurrence of char c. Given
        this, we don't need to persist a linear cache and can use a single variable
        instead. The hashmap maps character to number of distinct subsequences at
        the last occurrence now instead of mapping to the last seen index.

        With these observations, we can optimize the execution of our code to be
        much more succinct.

    Runtime:
        O(n) for the linear scan.

    Memory:
        O(n) for the `last` hashmap.
    """

    def distinctSubseqII(self, s: str) -> int:
        MOD = 10**9 + 7
        curr = 1
        last = {}

        for c in s:
            next = (2 * curr - last.get(c, 0)) % MOD
            last[c] = curr
            curr = next

        return (curr - 1) % MOD
