def reverse(x):

        r=0
        s=1
        if x<0:
            s=-1
            x=x*-1
        while(x>0):
            r=(r*10)+x%10
            x=x//10
        if not -2**31<r<2**31-1:
            return 0
        return s*r