from  init import __init as ge


def cls():
    all = ge.getfile()
    sql = "select * from "
    insersql = "insert into"
    for i in all:

      str = """class """+i["tablename"]+"():"+"""
     def __init__(self,"""

      for j in range(0,len(i["file"])):
         if j==len(i["file"])-1:
           str+=i["file"][j][0]+"=None):"
         else:
           str += i["file"][j][0] + "=None,"
      for j in range(0, len(i["file"])):
         str+="""
         self."""+i["file"][j][0]+"="+i["file"][j][0]

      open(i["tablename"]+"class" + ".py", "w").write(str)









