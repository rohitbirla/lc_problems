def romanToInt(s):
        d = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        sol =0
        
        for i in range(len(s)):
            if i+1 != len(s) and d[s[i]]<d[s[i+1]]:
                sol= sol-d[s[i]]
                
                
            else:
                sol=sol+d[s[i]]
        return sol
    