from  init import  __init as ge

def alls():
    all = ge.getfile()
    delsql="delete from  "
    sqland = "select * from  where"
    insersql="insert into"
    for i in all:
        sql = "select "
        for j in range(0, len(i["file"])):
            if j == len(i["file"]) - 1:
                sql += i["file"][j][0] + " from "
            else:
                sql += i["file"][j][0] + ","
        # 生成头部
        str="""from init import """+i["tablename"]+"dc"+"""
import pymysql
from until import  preteatment
from init import  publicfun
from  init import optimi
from until import  preteatment
def findall(page=None,line=None):
          if page!=None and line !=None:
             list2=[]
             list2.append(page)
             list2.append(line)
             sql=('"""+sql+i["tablename"]+" limit #,#')"+"""
             a=preteatment.res(sql,list2)
             rusels=publicfun.findall(a)
          else:
            rusels=publicfun.findall('"""+sql+i["tablename"]+"')"+"""
          return rusels
          """
        #cnunt
        str+="""
def conunt():
     sql='select  count(*)  from  """+i["tablename"]+"'"+"""
     rusels=publicfun.findall(sql)
     return rusels[0][0]
        """
        #max
        str += """
def max(a):
     sql='select  max('+a+')  from  """ + i["tablename"] + "'" + """
     rusels=publicfun.findall(sql)
     return rusels[0][0]
                """
        #min
        str += """
def min(a):
    sql='select  min('+a+')  from  """ + i["tablename"] + "'" + """
    rusels=publicfun.findall(sql)
    return rusels[0][0]
                        """
        str += """
def sum(a):
    sql='select  sum('+a+')  from  """ + i["tablename"] + "'" + """
    rusels=publicfun.findall(sql)
    return rusels[0][0]
                              """
        # 生成条件查询单值


        for j in range(0,len(i["file"])):

            str+="""
def findby"""+i["file"][j][0]+"("+i["file"][j][0]+",page=None,line=None"+"):"+"""
          list2=[]
          list2.append("""+i["file"][j][0]+")"+"""
          if page!=None and line !=None:
                   list2.append(page)
                   list2.append(line)
                   a=preteatment.res('""" + sql + i["tablename"] + " where " + i["file"][j][0] + " =# limit #,#',list2)" + """
          else:
            a=preteatment.res('"""+sql+i["tablename"]+" where "+i["file"][j][0]+ "=#',list2)"+"""
          optimi.main(a)
          rusels=publicfun.findaones(a)
          return rusels"""+""" 
          """

         # 生成条件查询like
        for j in range(0, len(i["file"])):
                str += """
def findby""" + i["file"][j][0] + "like" + "(" + i["file"][j][0] + ",page=None,line=None"+"):" + """
                list2=[]
                list2.append(""" + i["file"][j][0] + ")" + """
                if page!=None and line !=None:
                   list2.append(page)
                   list2.append(line)
                   a=preteatment.res('""" + sql + i["tablename"] + " where " + i["file"][j][0] + " like  # limit #,#',list2)" + """
                else:
                  a=preteatment.res('""" + sql + i["tablename"] + " where " + i["file"][j][0] + " like  #',list2)" + """
                rusels=publicfun.findall(a)
                return rusels""" + """ 
                      """

        # 生成条件查询and

        str+="""
def findand(a): 
      ret="""+i["tablename"]+"dc"+".dtion(a)"+"""
      f = preteatment.res(ret[0], ret[1])
      print(f)
      rusels = publicfun.findaones(f)
      return rusels
      """

      # 生成条件查询or

        str+="""
def findandor(a): 
      ret="""+i["tablename"]+"dc"+".dtionor(a)"+"""
      f = preteatment.res(ret[0], ret[1])
      optimi.main(a)
      rusels = publicfun.findaones(f)
      return rusels
      """

        # 生成删除单值
        for j in range(0, len(i["file"])):
            str += """
def delby""" + i["file"][j][0] + "(" + i["file"][j][0] + "):" + """
                  list2=[]
                  list2.append(""" + i["file"][j][0] + ")" + """
                  a=preteatment.res('""" + delsql + i["tablename"] + " where " + i["file"][j][0] + "=#',list2)" + """
                  rusels=publicfun.cut(a)
                  return rusels""" + """ 
                  """
        #add

        str+= """
def insert(a):
            list2 = []
            sql = "insert into """ + i["tablename"] + "("
        for j in range(0, len(i["file"])):
                if j == len(i["file"])-1:
                    str += i["file"][j][0] + ") values("
                else:
                    str += i["file"][j][0] + ","
        for j in range(0, len(i["file"])):
                 if j == len(i["file"]) - 1:
                    str+="#)"+'"'
                 else:
                    str += "#, "
        for j in range(0, len(i["file"])):
          str+="""
            list2.append(a."""+i["file"][j][0]+")"
        str+="""
            f = preteatment.res(sql, list2)
            rusels = publicfun.cut(f)
            return rusels 
        
        """

         #upadte
        str += """
def update(a): 
              ret=""" + i["tablename"] + "dc" + ".update(a)" + """
              f = preteatment.res(ret[0], ret[1])
              rusels = publicfun.cut(f)
              return rusels
              """


         #生成分页
        # 生成条件查询单值
        for j in range(0, len(i["file"])):
            str += """
def limitby""" + i["file"][j][0] + "(" + i["file"][j][0] +",page"+",line"+ "):" + """
                  list2=[]
                  list2.append(""" + i["file"][j][0] + ")" + """
                  list2.append(page)
                  list2.append(line)
                  a=preteatment.res('""" + sql + i["tablename"] + " where " + i["file"][j][0] + "=# limit #,#',list2)" + """
                  rusels=publicfun.findall(a)
                  return rusels""" + """ 
                  """

        open(i["tablename"] + ".py", "w").write(str)
    print("生成成功")





