def str_reverse(s):
    '''
    将字符串反转
    :param s: 将被反转的字符串
    :return:反转之后的字符串
    '''
    return s[::-1]

def substr(s,x,y):
    '''

    :param s:即将被切片的字符串
    :param x:切片开始的下标
    :param y:切片结束的下标
    :return:切片完成之后的字符串
    '''
    return s[x:y]


if __name__ == '__main__':
    print(str_reverse('abcdefg'))
    print(substr('abcdefg',2,4))