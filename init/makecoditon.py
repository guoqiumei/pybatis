from  init import __init as ge


def decyion():
    """
    sql 多条件查询
    :return: 
    """
    all = ge.getfile()
    sql = "select * from "
    sqland = "select * from  where"
    insersql = "insert into"
    for i in all:
        str = """
def dtion(a):
     sql="select * from  """+i["tablename"]+" where "+'"'+"""
     list3=[]
     list4=[]
        """
        for j in range(0, len(i["file"])):
            str += """
     if a.""" + i["file"][j][0] + "!=None:" + """
         sql+='""" + i["file"][j][0] + "=" + " # " + "'"+"""
         list3.append(a."""+i["file"][j][0] +")"
            for h in range(j+1, len(i["file"])):
                str += """
         if a.""" + i["file"][h][0] + "!=None:" + """
            sql+='"""  + " and "+  i["file"][h][0]+"=" + " # " + "'"+"""
            list3.append(a."""+i["file"][h][0]+")"

            str+="""
         list4.append(sql)
         list4.append(list3)
         return list4
         """


        #make or
        str+= """
def dtionor(a):
     sql="select * from  """+i["tablename"]+" where "+'"'+"""
     list3=[]
     list4=[]
        """
        for j in range(0, len(i["file"])):
            str += """
     if a.""" + i["file"][j][0] + "!=None:" + """
         sql+='""" + i["file"][j][0] + "=" + " # " + "'"+"""
         list3.append(a."""+i["file"][j][0] +")"

            for h in range(j+1, len(i["file"])):

                   str += """
         if a.""" + i["file"][h][0] + "!=None:" + """
            sql+='"""  + " or "+  i["file"][h][0]+"=" + " # " + "'"+"""
            list3.append(a."""+i["file"][h][0]+")"

            str+="""
         list4.append(sql)
         list4.append(list3)
         return list4
         """

         #生成 修改
        str+="""
def update(a):
     sql="update """+i["tablename"]+' set  " '+"""
     list3=[]
     list4=[]
    """
        for j in range(0, len(i["file"])):
            if j!=len(i["file"])-1:
                str += """
     if a.""" + i["file"][j][0] + "!=None:" + """
                   sql+='"""+ i["file"][j][0] + "=" + " #, " + "'" + """
                   list3.append(a.""" + i["file"][j][0] + ")"
            else:
                str += """
     if a.""" + i["file"][j][0] + "!=None:" + """
                           sql+='"""  + i["file"][j][0] + "=" + " #" + "'" + """
                           list3.append(a.""" + i["file"][j][0] + ")"


        str += """
     sql+=' where """+i["file"][0][0]+"=#"+"'"+"""
     list4.append(sql)
     list3.append(a."""+i["file"][0][0]+")"+"""
     list4.append(list3)
     return list4
               """





        open(i["tablename"]+"dc" + ".py", "w").write(str)



