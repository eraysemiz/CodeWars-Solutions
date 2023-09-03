def count(s):
    chars = {}
    if len(s) > 0:
        for char in s:
            if char not in chars:
                chars[char] = 1
            else:
                chars[char] += 1
        return chars
    return {}

