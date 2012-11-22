import web
import simplejson

db = web.database(dbn='mysql',db='pa',user='root',passwd='1213')

def get_users():
    return db.select('user',order='follower DESC',limit=30)
def get_user(i):
    return db.select('user',order='follower DESC',limit=10,offset=i)
def update_user(id):
    var = dict(id=id)
    b = db.select('user',where="id=$id",vars=var)[0]
    love =  b.love + 1
    db.update('user',love=love,where="id=$id",vars=var)
    print db.select('user',what="love",where="id=$id",vars =var)[0].love
def delete_user(id):
    var = dict(id=id)
    b = db.select('user',where="id=$id",vars=var)[0]
    love = b.love - 1
    db.update('user',love=love,where='id=$id',vars=var)
