def myAtoi( s: str) -> int:
    res = 0
    sign = 1
    for i in range(len(s)):
        if s[0].isalpha():
            return 0

        if s[i] == " ":
            pass
        elif '-' in s[i]:
            sign = -1
        else:
            if not s[i].isalpha():
                res = res * 10 + (ord(s[i]) - ord('0'))

    return res * sign

print(myAtoi("42 word"))