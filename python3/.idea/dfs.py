import sys
try:
    while True:
        m,n=list(map(int,raw_input().split(',')))
        mat=[]
        for i in range(m):
            mat.append(map(int,raw_input().split(',')))
        def search(i,j):
            if i<0 or j<0 or i>=m or j>=n or mat[i][j]!=1:
                return 0
            temp=mat[i][j]
            mat[i][j]=-1
            manCount=temp+search(i-1,j)+search(i+1,j)+search(i,j-1)+search(i,j+1)+search(i-1,j-1)+search(i+1,j+1)+search(i-1,j+1)+search(i+1,j-1)
            return manCount
        blockNum=0
        maxNum=0
        for i in range(m):
            for j in range(n):
                maxNum=search(i,j)
                if maxNum>0:
                    blockNum+=1
                    if manNum>maxNum:
                        maxNum=manNum
            print (str(blockNum)+','+str(maxNum))
except Exception:
    pass

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

    result=merge(value_list_all)

