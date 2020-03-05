from init import  __init as p
def cut(sql):
   db=p.conntion()
   cur=db.cursor()
   cur.execute(sql)
   b=cur.fetchall()
   db.commit()
   return b
   cur.close()
def findall(sql):
    db = p.conntion()
    cur = db.cursor()
    cur.execute(sql)
    listfile = cur.fetchall()
    cur.close()
    return listfile
def findaones(sql):
    db = p.conntion()
    cur = db.cursor()
    cur.execute(sql)
    c=cur.fetchone()
    cur.close()
    return c