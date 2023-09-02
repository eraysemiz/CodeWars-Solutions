def solution(s):
    break_camel = ""
    for i in s:
        if i.isupper():
             break_camel += " " + i
        else:
            break_camel += i
    return break_camel

