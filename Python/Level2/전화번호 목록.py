def solution(phone_book):
    phone_book.sort()

    for i in range(len(phone_book) - 1):
        if phone_book[i + 1].startswith(phone_book[i]):
            return False
    return True

# def solution(phone_book):
#     answer = True
#     phone_book.sort()

#     for x,y in zip(phone_book, phone_book[1:]):
#         if y.startswith(x):
#             answer = False
#             break
#     return answer