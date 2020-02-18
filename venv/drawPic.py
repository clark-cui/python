#要求：展示一个图画
#**
#*****
#**
#*****
#**

a=[2,5,2,5,2]

# 方法一（python中可以用num*字符串表示多个字符串）
for item in a:
    print(item*'*')

#方法二（常规方法）
for item in a:
    z=''
    for base in range(item):
       z+='*'
    print(z)

#封装从0开始的range方法
def my_range(num):
    n=0
    arr=[]
    while n<num:
        arr.append(n)
        n+=1

    print(arr)

my_range(3)
