
#coding=utf-8
import sys

def merge(list):
    for item in list:

        first=item[0]
        last=item[1]
        # for i in range(a,b):
        for item in list[1:]:
            print("------------------")
            print(item)
            # if item[0] in range(first,last):
            #     if item[1] in range(first,last):
            #         pass
            #     elif item[1] not in range
            if first<=item[0]<=last & item[1]>=last:
                first=first
                last=item[1]
            elif first>item[0] & item[1]<last:
                first=item[0]
                last=last
            elif first>item[0] & item[1]>last>item[0]:
                first=item[0]
                last=item[1]
            else:
                first=first
                last=last
        return (first,last)





        # for i in range(1,11):
        #
        #     print (i)


if __name__ == "__main__":
    # 读取第一行的n
    n = int(sys.stdin.readline().strip())

    # ans = 0
    value_list_all = []
    for i in range(n):
        # 读取每一行
        line = sys.stdin.readline().strip()
        print(line)
        # 把每一行的数字分隔后转化成int列表
        line_values=line.split(';')
        print(line_values)

        for i in line_values:

            v=map(int,i.split(','))
            value_list = []
            for item in v:

                value_list.append(item)
            print(value_list)
            value_list_all.append(value_list)
    # print (value_list_all)
    # b=[[1, 10], [32, 45], [78, 94], [5, 16], [80, 100], [200, 220], [16, 32]]
    result=merge(value_list_all)


            # values=int(line.split(','))
            # print(values)
            # for v in values:
            #     print(v)
        # values = map(int, line.split(';'))
        # for v in values:
        #     ans += v
    # print (ans)