from pymongo import MongoClient
import datetime
import hashcache
import alert
import portopen

#
# Used to connect to the db 
#
#


## Conenct to mongo and set collection



portopen.wait_net_service('mongo',27017)

client = MongoClient('mongo', 27017)
db=client.theknow


def add_file_db(url,id,hash,content,site):
	'''
	Adding the file to the db
	'''
	is_there_page = db.pages.find_one({"id":id})

	if is_there_page == None:
		#We dont have file with that id in the db lets add it !!
		page = {"url": url,
			"id": id,
        	"hash": hash,
         	"version": "latest",
         	"content": content,
         	"site": site,
         	"date": datetime.datetime.utcnow()}
		page_id = db.pages.insert_one(page).inserted_id
		alert.print_message("Added a new page "+str(page_id))
		#And add it to the cache so we dont need to ask here every time !
		hashcache.add_to_redis(id,hash)

		#Return false we did not have this file in db before
		return False

	else:
		#We already has that fil in the db so lets add it to the cache
		alert.print_message("we hade the value in db so add to redis as well")
		hashcache.add_to_redis(id,hash)

		#Return the hash from the db
		alert.print_message(is_there_page)
		return is_there_page["hash"]



def add_alert_db(url,content,site):
	'''
	Adidng an alert to the db
	'''
	page = {"url": url,
         	"version": "latest",
         	"content": content,
         	"site": site,
         	"date": datetime.datetime.utcnow()}
	page_id = db.alert.insert_one(page).inserted_id
	alert.print_message("Added new alert to db "+str(page_id))



def getUrl():
	'''
	Get all urls we have in the db
	'''
	back= db.pages.find({"version": "latest"})
	jsonReturn =[]
	for url in back:
		urlReturn = {
			"site": url.get("site"),
			"id": str(url.get('_id')),
			"url": url.get("url"),
			"date": url.get("date").strftime('%Y:%m:%d:%H:%M:%S')

		}
		jsonReturn.append(urlReturn)


	return jsonReturn


def getAlerts():
	'''
	Get all urls we have in the db
	'''
	back= db.alert.find({})
	jsonReturn =[]
	for url in back:
		urlReturn = {
			"site": url.get("site"),
			"id": str(url.get('_id')),
			"url": url.get("url"),
			"date": url.get("date").strftime('%Y:%m:%d:%H:%M:%S')

		}
		jsonReturn.append(urlReturn)


	return jsonReturn

