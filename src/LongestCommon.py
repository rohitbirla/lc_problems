def longestCommonPrefix(strs):


        new= sorted(strs, key=len)
        lcp = ""
        for i in range(len(new[0])):
            for s in new:
                 if i == len(s) or s[i] != new[0][i]:
                    return lcp
            lcp += new[0][i]
        return lcp