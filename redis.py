import redis
r = redis.Redis(host='localhost', port=6379, db=0)
r.set('session-id-123','user-id-456')