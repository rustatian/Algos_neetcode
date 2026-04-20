class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []
        for i in range(len(tokens)):
            match tokens[i]:
                case "+":
                    v1 = int(st.pop())
                    v2 = int(st.pop())
                    st.append(str(v1+v2))
                case "-":
                    v1 = int(st.pop())
                    v2 = int(st.pop())
                    st.append(str(v2-v1))
                case "*":
                    v1 = int(st.pop())
                    v2 = int(st.pop())
                    st.append(str(v1*v2))
                case "/":
                    v1 = int(st.pop())
                    v2 = int(st.pop())
                    res = int(v2/v1)
                    st.append(str(res))
                case _:
                    st.append(tokens[i])

        return int(st.pop())