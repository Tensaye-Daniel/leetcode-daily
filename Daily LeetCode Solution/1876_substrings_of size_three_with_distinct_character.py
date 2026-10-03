calss solution: 
   def countGoodsubString(self,s: str) -> int:
     valid=0
     n=len(s)
     for i in range (n-2):
        if s[i] != s[i+1] and \
           s[i] != s[i+2] and \
           s[i+1] != s[i+2]:
             valid += 1
    return valid
