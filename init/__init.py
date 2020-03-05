from init import  Openprofile as op
import pymysql
def conntion():
     #返回连接
     """
     
     返回连接
     
     """
     list=op.openfile("profile")
     db = pymysql.Connect(host=list[0], port=int(list[2]), user=list[5], password=list[3], db=list[1],
                          charset=list[4])
     return db

def getcur():
     """
     该办法返回的是一你绑定数据的表
     :return: 
     """
     list = op.openfile("profile")
     db=conntion()
     cur=db.cursor()
     cur.execute("select table_name from information_schema.tables where table_schema='" + list[1] + "'")
     tablename=cur.fetchall()
     return tablename
def getfile():
     """
     
     :return 字段: 
     """
     list2=[]
     list = op.openfile("profile")
     tablename=getcur()
     db = conntion()
     cur = db.cursor()
     for i in range(0, len(tablename)):
          list = op.openfile("profile")
          sql="select column_name,column_comment,data_type  "
          sql+="from information_schema.columns  "
          sql+="where table_name='"+tablename[i][0]+"' and table_schema='"+list[1]+"'"
          cur.execute(sql)
          filename = cur.fetchall()
          dit={
              "tablename":tablename[i][0],"file":filename
          }
          list2.append(dit)
     return list2



# print(tablename[i][0])
#           cur.execute("select column_name  from information_schema.columns where "
#                       "table_name='" + tablename[i][0] + "'")
#           filename=cur.fetchall()
#           print(filename)
#           sql="select * from "+tablename[i][0]
#           print(sql)

#      #使用sql语句来查询
#      usesql="""
# import pymysql
# import init
# def selectall(sql):
#    db=init.conntion()
#    cur=db.cursor()
#    cur.execute(sql)
#    listfile=cur.fetchall()
#    cur.close()
#    return  list(listfile)
# def insert(dmlsql):
#    #使用于增删查
#    db=init.conntion()
#    cur=db.cursor()
#    cur.execute(dmlsql)
#    cur.db.commit()
#    cur.close()
#    """
#      open("usesql.py","w").write(usesql)
#      #tablename表名
#      for i in range(0, len(tablename)):
#           print(tablename[i][0])
#           cur.execute("select column_name  from information_schema.columns where "
#                       "table_name='" + tablename[i][0] + "'")
#           filename=cur.fetchall()
#           print(filename)
#           sql="select * from "+tablename[i][0]
#           print(sql)
#           pyfile="""import pymysql
# import init
# def selectall():
#    db=init.conntion()
#    cur=db.cursor()
#    cur.execute("""+'"'+sql+'")'+"""
#    listfile=cur.fetchall()
#    cur.close()
#    return  list(listfile)"""
#           for j in range(0,len(filename)):
#                update=upate="update " + tablename[i][0]+' set '+filename[j][0]+' = "+'+"'"+filename[j][0]+"'"+'+"where '+ filename[0][0]+'="+str(uid)'
#                sqlby="select * from "+tablename[i][0] +' where "+' +"str("+filename[j][0]+")"+'+"='+filename[j][0]
#                pyfile+="""
# def selectby"""+filename[j][0]+"("+filename[j][0]+"):"+"""
#    db=init.conntion()
#    cur=db.cursor()
#    cur.execute("""+'"'+sqlby+'")'+"""
#    listfile=cur.fetchone()
#    cur.close()
#    return  list(listfile)
# def update"""+filename[j][0]+"("+filename[j][0]+",uid):"+"""
#    db=init.conntion()
#    cur=db.cursor()
#    cur.execute("""+'"'+update+')'"""
#    cur.db.commit()
#    cur.close()
# """
#
#
#           open(tablename[i][0]+".py","w").write(pyfile)
#








