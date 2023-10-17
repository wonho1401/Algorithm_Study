def solution(s, skip, index):
    answer = list()
    for alphabet in s:
        tmp = 0
        n_alphabet = alphabet
        while True:    
            n_alphabet = chr(ord(n_alphabet) + 1)
            if ord(n_alphabet) == 123:
                n_alphabet = 'a'    
            if n_alphabet not in skip:
                tmp += 1
            if tmp == index:
                answer.append(n_alphabet)
                break
    return "".join(answer)