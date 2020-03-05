#---防sql注入处理——#
import re
def res(sql,list2):
    """ 
    :param sql: 
    :param list2: 
    :return sql字段: 
 """
    if list2 !=[]:
        for i in list2:
            j=str(i)

            if i==None:
                 print(j);
                 j="null"
            if j.find(" ")<=0:
                if type(i)==type("ds"):
                    ##该判断作用是免去后面判断字段类型的麻烦
                  sql = re.sub("#", "'"+j+"'", sql, 1)
                else:
                    sql = re.sub("#",j, sql, 1)
    print(sql)
    if len(open("sqllog.txt", "r").readlines()) > 90:
        print("你的SQL语句已经使用到了"+str(len(open("sqllog.txt", "r").readlines()))+"条，需要请去记录，200条被删除，在sqllog")
    if len(open("sqllog.txt","r").readlines())>120:
        open("sqllog.txt", "w").write(sql + "\n")
    else:
        open("sqllog.txt", "a").write(sql + "\n")
    return sql
