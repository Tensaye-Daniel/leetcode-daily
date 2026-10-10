class solution : 
    def removeouterParenthesses(self,s):
        list,stack = [],[]
        for i in s:
            if i == ")":
                stack,pop()
            elif stack:
                list.append(i)
            else i == "(":
                stack.append(i)
        return "".join(list)