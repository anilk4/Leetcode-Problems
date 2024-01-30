class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token == "+":
                x = stack.pop() + stack.pop()
                stack.append(x)
            elif token == "-":
                a = stack.pop()
                b = stack.pop()
                x = b - a
                stack.append(x)

            elif token == "*":
                x = stack.pop() * stack.pop()
                stack.append(x)

            elif token == "/":
                a = stack.pop()
                b = stack.pop()
                x = int(b / a) if b * a >= 0 else int(b / a) + 0
                stack.append(x)

            else:
                stack.append(int(token))
        
        
        return stack.pop()
