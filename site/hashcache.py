import redis
import alert
import portopen
#
#
# To save some time and to make it statelass we add a cache to store the hash in.
# This will read from db and save the rsult into the redis cache server.
# Then we run the script we can easy test if we already have the result in the cache !
#
#
portopen.wait_net_service('redis',6379)
r = redis.StrictRedis(host='redis', port=6379, db=0)


def add_to_redis(id,hash):
	# Lets add some data into redis
	alert.print_message("Add to redis "+id+hash)
	r.set(id,hash)



def check_hash_redis(id):
	# Check if we have a working hash in redis
	from_cache = r.get(id)
	if from_cache == None:
		#We dont haveything in the cache :-( 
		alert.print_message("cache hit missed !")
		return False
	else:
		#O yess we have a hit in cache retrun the hit !
		return from_cache