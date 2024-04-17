def solution(phone_book):
    dict = {}
    for phone in phone_book:
        dict[phone] = True
    for phone in phone_book:
        s = ""
        for p in phone:
            s += p
            if s in dict and s != phone:
                return False
    return True