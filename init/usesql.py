from init import  __init as p
from  until import  preteatment
def cut(sql,list2):
    #使用你的sql，站位符请使用#
   db=p.conntion()
   cur=db.cursor()
   newsql=preteatment.res(sql,list2)
   cur.execute(newsql)
   b=cur.fetchall()
   db.commit()
   cur.close()
   return b

def findall(sql,list2):
    db = p.conntion()
    cur = db.cursor()
    newsql = preteatment.res(sql, list2)
    cur.execute(newsql)
    listfile = cur.fetchall()
    cur.close()
    return listfile
def findaones(sql,list2):
    db = p.conntion()
    cur = db.cursor()
    newsql = preteatment.res(sql, list2)
    cur.execute(newsql)
    c=cur.fetchone()
    cur.close()
    return c