import re
# 打开配置文件
#默认是txt文件
def openfile(profile):
    list=[]
    f=open(profile,"r").read()
    host=re.compile("host=(.*)").findall(f)[0]
    dbname = re.compile("dbname=(.*)").findall(f)[0]
    port= re.compile("port=(.*)").findall(f)[0]
    password= re.compile("password=(.*)").findall(f)[0]
    enconde= re.compile("encode=(.*)").findall(f)[0]
    username= re.compile("username=(.*)").findall(f)[0]
    list.append(host)
    list.append(dbname)
    list.append(port)
    list.append(password)
    list.append(enconde)
    list.append(username)
    return  list







