import os

# 查看文件执行路径
print(os.getcwd())

file = open('static/txt.txt','w')

file.write("hahaha")

file.close()

file = open('static/txt.txt','r')

print(file.read())

file.close()


#优化写法

# 写入文件
with open('static/txt.txt', 'w') as write_file:
    write_file.write('hahaha')

with open('static/txt.txt', 'r') as read_file:
    content = read_file.read()

print(content)

# with 语句用于简化资源管理，特别是那些需要显式关闭或释放的对象，如文件、数据库连接、锁等
