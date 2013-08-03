#coding:utf-8
from  mysns.models import sns
def save(name,content):
	n=sns()
	n.name=name
	n.content=content
	n.save()
def update_by_id(_id,name,content):
	n=sns.objects.get(id=_id)
	n.name=name
	n.content=content
	n.save()
def get_all():
	all= sns.objects.all()
	return all

def get_by_id(_id):
	return sns.objects.filter(id=_id)
	
def del_by_id(_id):
	_id=int(_id)
	n=sns.objects.get(id=_id)
	n.delete()
#del del_all():
#	db.metadata.create_all()
#get_all()
	
	
	
