import redis
def main():
    r = redis.Redis(host='192.168.221.70', port=6379, password='SSShyu1104.')
    r.set('username1', 'shy')
    r.set('username2', '张辰熙')
    r.set('length','18')
    r.incr('length')
    r.hset('stu1','id','1001')
    r.hset('stu1', 'age', '50')
    r.hset('stu1', 'sex', 'male')
    r.rpush('list1',10,20,30,40,25)
    print(r.lrange('list1',0,-1))
    print(r.incr('length'))
    print(r.get('username2').decode('utf-8'))
    print(r.hgetall('stu1'))

if __name__ == '__main__':
    main()