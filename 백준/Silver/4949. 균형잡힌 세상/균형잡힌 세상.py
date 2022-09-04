while True:
    a = input()

    if a == '.':
        break
    stack = []
    for i in range(len(a)):
        # print(stack, a[i])
        if a[i] == '(' or a[i] == '[':
            stack.append(a[i])
        elif a[i] == ')' or a[i] == ']':
            if stack:
                if (stack[-1] == '(' and a[i] == ')') or (stack[-1] == '[' and a[i] == ']'):
                    stack.pop()
                else:
                    print('no')
                    break
            else:
                print('no')
                break
    else:
        if stack:
            print('no')
        else:
            print('yes')