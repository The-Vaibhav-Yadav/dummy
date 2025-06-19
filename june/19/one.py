s="(){}}{"
stack = s[0]

for i in range(1, len(s)):
    if stack == "":
        stack = stack + s[i]
    else:

        if s[i] == ")" and stack[-1] == "(":
            stack = stack[:-1]
        
        elif s[i] == "]" and stack[-1] == "[":
            stack = stack[:-1]

        elif s[i] == "}" and stack[-1] == "{":
            stack = stack[:-1]

        else:
            stack = stack + s[i]

print(stack)