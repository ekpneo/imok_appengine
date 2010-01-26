from google.appengine.ext import db


class ImokUser(db.Model):
  account = db.UserProperty()


class Post(db.Model):
	user 		= db.UserProperty()
	datetime	= db.DateTimeProperty(auto_now_add=True)

	# this could maybe be a GeoPtProperty() - i don't know if it matters.
	lat			= db.FloatProperty()
	lon			= db.FloatProperty()
	message 	= db.StringProperty()

