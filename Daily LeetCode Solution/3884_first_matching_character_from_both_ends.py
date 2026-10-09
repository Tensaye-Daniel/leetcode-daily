class solultion (object):
    def firstMachingindex(self,s):
        left=0
        right= len(s)-1
        while left <= right:
            if s[left] == s[right) or left == right:
                return left
            else :
                left +=1
                right -=1
        return -1