class Solution:
    def evalRPN(tokens: list[str]) -> int:
        stack = []
        for i in range(len(tokens)):
            if tokens[i].isdigit() or tokens[i].startswith("-") and tokens[i][1:].isdigit():
                stack.append(int(tokens[i]))
            else:
                x = stack.pop()
                y = stack.pop()
                sign = tokens[i]
                if sign == "+":
                    stack.append(x+y)
                elif sign == "-":
                    stack.append(y-x)
                elif sign == "*":
                    stack.append(x*y)
                else:
                    stack.append(int(y/x))
        return stack[0]
                    
        
tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
print(Solution.evalRPN(tokens))