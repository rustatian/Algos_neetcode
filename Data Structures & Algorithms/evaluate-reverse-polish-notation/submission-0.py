class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []
        res: int = 0
        for i in range(len(tokens)):
            match tokens[i]:
                case "+":
                    while len(st) > 0:
                        res += int(st.pop())
                case "-":
                    while len(st) > 0:
                        res -= int(st.pop())
                case "*":
                    while len(st) > 0:
                        res *= int(st.pop())
                case "/":
                    while len(st) > 0:
                        res = int(st.pop()) // res
                case _:
                    st.append(tokens[i])
        return res