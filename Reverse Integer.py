def reverse( x: int) -> int:
    xString = str(x)
    if xString[0] == '-':
        xString = xString[1:len(xString)][::-1]
        xString = '-' + xString
        if (x < 0 and int (xString) > 0) or int(xString) < pow(2,31)*-1:
            return 0
        else:
            return int(xString)
    else:
        xString = xString[::-1]
        if (x > 0 and int(xString) < 0) or int(xString) > pow(2,31)-1:
            return 0
        else:
            return int(xString)

print(reverse(1534236469))
# print(type(reverse(-123)))
