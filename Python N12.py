#15-20 minutes
class Solution:
    def intToRoman(self, num: int) -> str:
        string = ""
        while num != 0:
            if num >= 1000:
                string = string + "M"
                num = num - 1000
            elif num >= 900:
                string = string + "CM"
                num = num - 900
            elif num >= 500:
                string = string + "D"
                num = num - 500
            elif num >= 400:
                string = string + "CD"
                num = num - 400
            elif num >= 100:
                string = string + "C"
                num = num - 100
            elif num >= 90:
                string = string + "XC"
                num = num - 90
            elif num >= 50:
                string = string + "L"
                num = num - 50
            elif num >= 40:
                string = string + "XL"
                num = num - 40
            elif num >= 10:
                string = string + "X"
                num = num - 10
            elif num >= 9:
                string = string + "IX"
                num = num - 9
            elif num >= 5:
                string = string + "V"
                num = num - 5
            elif num >= 4:
                string = string + "IV"
                num = num - 4
            elif num >= 1:
                string = string + "I"
                num = num - 1
        return string