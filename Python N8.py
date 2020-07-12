#~1 hour
#Probably an easier way to do this
class Solution:
    def myAtoi(self, str: str) -> int:
        x = 0
        n = 0
        while x == 0:
            if n >= len(str):
                x = 3
                ans = 0
            elif str[n] == "1" or str[n] == "2" or str[n] == "3" or str[n] == "4" or str[n] == "5" or str[n] == "6" or str[n] == "7" or str[n] == "8" or str[n] == "9" or str[n] == "0" or str[n] == "+" or str[n] == "-":
                if str[n] == "-":
                    ans = -1
                    str = str[n + 1:len(str)]
                elif str[n] == "+":
                    ans = 1
                    str = str[n + 1:len(str)]
                else:
                    ans = 1
                    str = str[n:len(str)]
                x = 1
                n = 0
            elif str[n] == " ":
                n = n + 1
            else:
                x = 3
                ans = 0
        while x == 1:
            if str == "":
                x = 3
                ans = 0
            elif str[n] != "1" and str[n] != "2" and str[n] != "3" and str[n] != "4" and str[n] != "5" and str[n] != "6" and str[n] != "7" and str[n] != "8" and str[n] != "9" and str[n] != "0":
                x = 3
                ans = 0
            else:
                x = 2
        while x == 2:
            if n >= len(str):
                x = 3
                if str == '':
                    ans = 0
                else:
                    ans = ans * int(str)
            elif str[n] == "1" or str[n] == "2" or str[n] == "3" or str[n] == "4" or str[n] == "5" or str[n] == "6" or str[n] == "7" or str[n] == "8" or str[n] == "9" or str[n] == "0":
                n = n + 1 
            else:
                str = str[0:n]
                ans = ans * int(str)
                x = 3
        return max(min(ans, 2 ** 31 - 1),-2 ** 31)