import web
import os
import model
import simplejson
### Templates

web.config.debug = True

urls =(
        "/", "Index",
        "/test","test",
        "/like","action",
)

app = web.application(urls,globals())

render = web.template.render('templates',base='base')

class test:
    def GET(self):
        receive = web.input();
        if receive:
            user = model.get_user(receive.p)
            data = simplejson.dumps(user.list())
            print len(user)
            return data
        else:
            return "error request"
class Index:
    """Show page"""
    def GET(self):
        print web.ctx.method
        users = model.get_users()
        return render.index(users)
class action:
    def GET(self):
        print web.ctx.method
        id = web.input().id
        print id
        model.update_user(id)
        o = dict(r = 0) 
        return simplejson.dumps(o)

    def DELETE(self):
        print web.ctx.method
        id = web.data().id
        print id
        model.delete_user(id)
        o = dict(r = 0)
        return simplejson.dumps(o)

#application = web.application(urls, globals()).wsgifunc()
#curdir = os.path.dirname(__file__) #session =
#web.session.Session(app,web.session.DiskStore(os.path.join(curdir,'sessions')),)
#application = app.wsgifunc()
#
if __name__ == '__main__':
    app.run()
