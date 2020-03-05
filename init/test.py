from  init import  crit
from  init import critclass
from init import  usesql
all=crit.findall()#页码为可选参数
slelectbyid=crit.findbyid(1)#单条件查询ces完成
crit.insert(critclass.crit(contet="232" ))#添加完成，需要指定前缀，没有的字段留空
selectad=crit.findand(critclass.crit(c_id=1,id=1))
like=selectlike=crit.findbycontetlike("%s%",)#模糊查询
likepage=selectlike=crit.findbycontetlike("%s%",0,4)#分页单值分页一样，页码，可以为可选参数
update=crit.update(critclass.crit(c_id=1,contet="ds"))#修改，主键列id，一定不能缺少
max=crit.max("id")#聚合函数
#使用你的sql，当初版本没注入事务，如果要使用事务，自己处理事务
#try expct 处理，，自己commit，查询不用，或者你直接使用库包
sql="select * from crit where id=#"
list1=[]
list1.append(1)
c=usesql.findall(sql,list1)
print(c)

