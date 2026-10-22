class Solution(object):
    def interpret(self, command):
        list = []
        i = 0
        n = len(command)

        while i < n:
            if command[i] == "G":
                list.append("G")
                i += 1

            elif command[i:i+2] == "()":
                list.append("o")
                i += 2

            else:
                list.append("al")
                i += 4

        return "".join(list)