res=[]
def generateParenthesis(n):
    
    if n < 1 or n >= 8 :
        raise ValueError("Invalid Input : Valid Parenthesis is between 1 to 8")
    
    memo = {}

    def backtrack(s, left, right):
        
        if (s, left, right) in memo:
            return memo[(s, left, right)]

        if len(s) == 2 * n: 
            return [s]

        result = []
        if left < n:
            result += backtrack(s + '(', left + 1, right)
        if right < left:
            result += backtrack(s + ')', left, right + 1)

        memo[(s, left, right)] = result
        return result

    return backtrack('', 0, 0)

if __name__ == "__main__":
    try:
        n = int(input("Enter the number of pairs of parentheses: "))
        combinations = generateParenthesis(n)
        print("All Combinations of Parenthesis are : ")
        res.append(combinations)
        print(res)
    except Exception as e:
        print("Error: {}".format(str(e)))