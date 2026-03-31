def print_file_info(file_name):
    '''

    :param file_name:即将读取的文件
    :return:
    '''
    f=None
    try:
        f = open(file_name,'r',encoding="UTF_8")
        content=f.read()
        print("文件内容如下：")
        print(content)
    except Exception as e:
        print(f"文件异常{e}")
    finally:
        if f:
            f.close()
def append_to_file(file_name,data):
    with open(file_name,'a',encoding="UTF_8") as f:
        f.write(data)
        f.write("\n")
        f.close()


if __name__ == '__main__':
    append_to_file("C:/Users/许明鉴/Desktop/x.txt.bak","我是帅哥")
    # print_file_info("C:/Users/许明鉴/Desktop/x.txt.bakss")
