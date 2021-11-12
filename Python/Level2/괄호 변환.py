def sepUV(p):
    new_u = ''
    new_v = ''

    if p == '':
        return ''
    else:
        cur = 0
        for i in range(len(p)):
            if p[i] == '(':
                cur -= 1
            else:
                cur += 1

            if cur == 0:
                new_u = p[:i + 1]
                new_v = p[i + 1:]
                break

    if new_u[0] == '(':
        new_v = sepUV(new_v)
        return new_u + new_v

    else:
        new_v = '(' + sepUV(new_v) + ')'
        temp = ''
        for i in range(1, len(new_u) - 1):
            if new_u[i] == '(':
                temp += ')'
            else:
                temp += '('
        new_v += temp
        return new_v


def solution(p):
    answer = sepUV(p)

    return answer

# def solution(p):
#     counter = 0
#     inner_counter = 0
#     if not p:
#         return ''
#     u = ''
#     v = ''
#     for current_p in p:
#         if current_p == '(':
#             counter += 1
#             u += current_p
#         else:
#             counter -= 1
#             u += current_p
#         if counter == 0:
#             v = p[len(u):]
#             u_is_right = True
#             for inner_p in u:
#                 if inner_p == '(':
#                     inner_counter += 1
#                 else:
#                     inner_counter -= 1
#                 if inner_counter < 0:
#                     u_is_right = False
#             if u_is_right:
#                 return u + solution(v)
#             else:
#                 new_u = ''
#                 for i in u[1:-1]:
#                     if i == '(':
#                         new_u += ')'
#                     else:
#                         new_u += '('
#                 answer = '(' + solution(v) + ')' + new_u
#                 return answer