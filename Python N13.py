#10-15 minutes
#Probably an easier way to do this
class Solution:
    def romanToInt(self, s: str) -> int:
        x = 0
        while len(s) != 0:
            a = s[0:1]
            if a == "I":
                a = 1
            elif a == "V":
                a = 5
            elif a == "X":
                a = 10
            elif a == "L":
                a = 50
            elif a == "C":
                a = 100
            elif a == "D":
                a = 500
            elif a == "M":
                a = 1000
            else:
                a = 0
            if len(s) != 1:
                b = s[1:2]
            else:
                b = "Z"
            if b == "I":
                b = 1
            elif b == "V":
                b = 5
            elif b == "X":
                b = 10
            elif b == "L":
                b = 50
            elif b == "C":
                b = 100
            elif b == "D":
                b = 500
            elif b == "M":
                b = 1000
            else:
                b = 0
            if a - b < 0:
                x = x + b - a 
                s = s[2:len(s)]
            else:
                x = x + a
                s = s[1:len(s)]
        return x