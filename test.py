import web, datetime, demjson

db = web.database(dbn = 'mysql', db = 'pythonDB', user = 'python', pw = 'python')
def get_users():
	data = db.select('user', order='id DESC')
	json = demjson.encode(data)
	print json

def get_dusers():
	data = db.select('user', order='id DESC')
	json = demjson.encode(data)
	print demjson.decode(json)[0]['name']

def new_user(name, age):
	print db.insert('user', name=name, age=age)

def del_user(id):
    	if db.delete('user', where="id=$id", vars=locals()) == 1 :
		print "success"
	else:
		print "fail"

def update_user(id, name, age):
  	print db.update('user', where="id=$id", vars=locals(), name=name, age=age)

#get_users()
#get_dusers()
#new_user("hello")
update_user(4, "cat", "40")
#del_user(4)



