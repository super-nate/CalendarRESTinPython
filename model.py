#!/usr/bin/env python
import web, datetime
import time
import datetime

db = web.database(dbn = 'mysql', db = 'pythonDB', user = 'python', pw = 'python')
null =''
def get_users():
    return db.select('CalendarUser', order='id DESC')

def get_user(id):
    try:
        return db.select('CalendarUser', where='id=$id', vars=locals())[0]
    except IndexError:
        return None

def new_user(email, password):
    return db.insert('CalendarUser', email=email, password=password)

def del_user(id):
    return db.delete('CalendarUser', where="id=$id", vars=locals())

def update_user(id, email, password):
    return db.update('CalendarUser', where="id=$id", vars=locals(),
        email=email, password=password)

def get_events(userid):
    try:
    	return db.select('Event', where='userid=$userid', vars=locals())
    except IndexError:
        return None

def new_event(userid, title, starttime=null, endtime=null, place=null, description=null):
    #st = time.mktime(datetime.datetime.strptime(starttime, "%Y-%m-%d %H:%M:%S").timetuple())
    #et = time.mktime(datetime.datetime.strptime(endtime, "%Y-%m-%d %H:%M:%S").timetuple())
    return db.insert('Event', userid=userid, starttime=starttime, endtime=endtime, place=place, title=title, description=description)

def get_event(userid, eventid):
    try:
    	return db.select('Event', where='userid=$userid and id=$eventid', vars=locals())[0]
    except IndexError:
        return None

def update_event(userid, starttime, endtime, place, title, decription):
    st = time.mktime(datetime.datetime.strptime(starttime, "%Y-%m-%d %H:%M:%S").timetuple())
    et = description
    return db.insert('Event', where="userid=$userid and eventid=$eventid", vars=locals(), userid=userid, starttime=st, endtime=et, place=place, title=title, description=description)

def del_event(userid, eventid):
    return db.delete('Event', where="userid=$userid and eventid=$eventid", vars=locals())