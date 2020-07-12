#40-50 minutes
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        combinations = [""]
        combinations = [""]
        inputs = []
        n = 0
        m = 0
        while len(digits) > 0:
            if digits[0] == "2":
                inputs = ["a","b","c"]
            elif digits[0] == "3":
                inputs = ["d","e","f"]
            elif digits[0] == "4":
                inputs = ["g","h","i"]
            elif digits[0] == "5":
                inputs = ["j","k","l"]
            elif digits[0] == "6":
                inputs = ["m","n","o"]
            elif digits[0] == "7":
                inputs = ["p","q","r","s"]
            elif digits[0] == "8":
                inputs = ["t","u","v"]
            elif digits[0] == "9":
                inputs = ["w","x","y","z"]
            else:
                inputs = [""]
            
            if inputs[0] == "":
                digits = digits[1:len(digits)]
            elif combinations[0] == "":
                combinations = inputs
                digits = digits[1:len(digits)]
            else:
                save = combinations
                combinations = []
                while n < len(save):
                    while m < len(inputs):
                        com = save[n] + inputs[m]
                        combinations.append(com)
                        m = m + 1
                    m = 0
                    n = n + 1
                digits = digits[1:len(digits)]
            m = 0
            n = 0
        if combinations[0] == "":
            return []
        else:
            return combinations