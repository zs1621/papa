#!/usr/bin/env python
#-*-coding="utf-8"-*-
import MySQLdb
import httplib
import simplejson
import time
import MySQLdb.cursors
con = MySQLdb.connect(host='localhost',user='****',passwd='*****',db='pa',charset='utf8')
cursor = con.cursor(cursorclass=MySQLdb.cursors.DictCursor)
#cursor.execute("create table user(avatar varchar(80) ,id char(8) unique,follower int,following int, name varchar(20), createtime bigint,background varchar(80),signature varchar(100) )")
#5731 12256
def papa(url):
    i,j = 1,249
    for n in range(1,1000000):
        pa = httplib.HTTPConnection(url)
        pa.request('GET','/api/v1/timeline/recommend?count=50&cursor='+str(j)) 
        result = pa.getresponse()
        print result
        if not result:
            print 'fuck'
        content = simplejson.loads(result.read())
        response = content['response']
        startime = time.clock()
        if j == 249:
            last = response[len(response)-1]['post']['id']
            startime = time.clock()
            for m in range(0,len(response)): 
                for a in response[m]['post']['favors']:
                    signature = a['user']['signature']
                    print a['user']['name']
                    user =[a['user']['avatarLarge'][0:-7], a['user']['id'],a['user']['followerCount'],a['user']['followingCount'],a['user']['name'],a['user']['registerTime'],a['user']['background'][0:-7],signature]
                    cursor.execute("replace into user values(%s,%s,%s,%s,%s,%s,%s,%s)",user)
            endtime = time.clock()
            con.commit()
            print endtime-startime
        else:
            if last != response[len(response)-1]['post']['id']:
                #todo upsert into the first
                for a in response[0]['post']['favors']:
                    signature = a['user']['signature']
                    user =[a['user']['avatarLarge'][0:-7], a['user']['id'],a['user']['followerCount'],a['user']['followingCount'],a['user']['name'],a['user']['registerTime'],a['user']['background'][0:-7],signature]
                    cursor.execute("replace into user values(%s,%s,%s,%s,%s,%s,%s,%s)",user)
                last = response[len(response)-1]['post']['id']
                print j
        con.commit()
        time.sleep(1)
        j=j+1
if __name__ == "__main__":
    url = "api.papa.me"
    papa(url)
