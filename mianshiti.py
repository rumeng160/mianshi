def how_many_ways(digitarray):
    #如果数字是以“0”开头，将“0”去掉
    digitarray = digitarray.lstrip('0')
    length = len(digitarray)
    #当去掉“0”后，数字的长度等于0时，直接返回0，因为0在条件里无法转换为字母
    if length == 0:
        return 0
    #按照该数字的长度生成一个列表，用于后面进行计算
    li = list(range(length+1))
    li[0] = 1
    print(li)
    #循环去判断该数字的每一个值
    for i in range(length+1):
        #第一个数字不是0，肯定可以变换成一个字母
        if i == 0:
            continue
        #前面一个字符如果不是'0'则li[i]至少等于li[i-1]
        if digitarray[i-1] == '0':
            li[i] = 1
        else:
            li[i] = li[i-1]
        #判断当前字符跟前一个字符是否可以凑成一个字母所对应的值
        if (i>1 and int(digitarray[i-1])<=6 and int(digitarray[i-2])==2) or (i>1 and int(digitarray[i-2])==1):
            li[i] += li[i-2]
    print(li)
    return li[length]
