import web
import model
import demjson

urls = (
	'/', 'UserCollection',
	'/users', 'UserCollection',
	'/users/', 'UserCollection',
	'/users/(\d+)', 'User',
	'/users/(\d+)/', 'User',
	'/users/(\d+)/events', 'EventCollection',
	'/users/(\d+)/events/', 'EventCollection',
	'/users/(\d+)/events/(\d+)', 'Event',
	'/users/(\d+)/events/(\d+)/', 'Event'
)

class UserCollection:
	
	def GET(self):
		"""Get users list"""
		users = model.get_users()
		return demjson.encode(users)

	def POST(self):
		"""New a user"""
		data = web.data()
		data = demjson.decode(data)
		id = model.new_user(data['email'], data['password'])
		return demjson.encode({"userid":id})
		 
class User:
	
	def GET(self, id):
		"""Get user"""
		user = model.get_user(id)
		return demjson.encode(user)

	def PUT(self, id):
		"""Update a user"""
		data = web.data()
		data = demjson.decode(data)
		model.update_user(id, data['email'], data['password'])
		return demjson.encode(model.get_user(id))

	def DELETE(self, id):
		"""Delete a user"""
		if model.del_user(id) == 1 :
			return demjson.encode({"status":"success"})
		else:
			return demjson.encode({"status":"fail"})

class EventCollection:
	
	def GET(self, userid):
		"""Get events list"""
		events = model.get_events(userid)
		return demjson.encode(events)

	def POST(self, userid):
		"""New a event"""
		data = web.data()
		data = demjson.decode(data)
		id = model.new_event(userid, data['title'], data.get('starttime'), data.get('endtime'), data.get('place'), data.get('description'))#data['title'], data['description'])
		return demjson.encode({"eventid":id})

class Event:
	
	def GET(self, userid, eventid):
		"""Get event"""
		event = model.get_event(userid, eventid)
		return demjson.encode(event)

	def PUT(self, userid, eventid):
		"""Update a event"""
		data = web.data()
		data = demjson.decode(data)
		model.update_event(userid, eventid, data['starttime'], data['endtime'], data['place'], data['title'], data['description'])
		return demjson.encode(model.get_event(userid, eventid))

	def DELETE(self, userid, eventid):
		"""Delete a event"""
		if model.del_event(userid, eventid) == 1 :
			return demjson.encode({"status":"success"})
		else:
			return demjson.encode({"status":"fail"})


app = web.application(urls, globals())

if __name__ == '__main__':
    app.run()		

