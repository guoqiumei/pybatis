from init import __init
import  re

def contion():
    db=__init.conntion()
    cur=db.cursor()
    return cur
#分析sql
def analysisindex(sql):
    global sqlstr
    sqlstr=sql
    #查看sql使用情况
    db=__init.conntion()
    cur=db.cursor()
    sql="explain "+sql
    cur.execute(sql)
    reslut=cur.fetchall()
    return reslut
def analysistable():
    pat=re.compile(" from (.*?) where ")
    file=pat.findall(sqlstr)
    return file
#
# def analysissql():
#     pat=re.compile("select (.*?)from")
#     file=pat.findall(sqlstr)
#     return file
def analysissql2():
    pat=re.compile("where (.*?)=")
    file=pat.findall(sqlstr)
    return file
def analysissqland():
    pat=re.compile("and (.*?)=''")
    file=pat.findall(sqlstr)
    return file
def  main(sql):
 i=0
 while i==0:
        j=0
        j=++j
        reslut=analysisindex(sql)
        tablename = analysistable()
        andsql=analysissqland()
        if reslut[0][4] == "ALL":
            file = analysissql2()
            if andsql == []:
                if file != []:
                    cur = contion()
                    indexsql = "create index index_" + file[0] + " on " + tablename[0] + "(" + file[0] + ")"
                    try:
                        cur.execute(indexsql)
                    except:
                        i=2

            else:

                cur = contion()
                indexsql = "create index index_" + file[0] + " on " + tablename[0] + "(" + file[0] + " ," + andsql[
                    0] + ")"
                print(indexsql)
                cur.execute(indexsql)

        else:
            i = 2
        if j > 5:
            # 防止程序出现死循环，当检验5次都不能优化，就结束程序
            print("请检查你的sql语句，或者手工优化。")
            i = 2
 print("已经完成简单优化")



