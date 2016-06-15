from views import db
from models import Task
from datetime import date

db.create_all()

#db.session.add(Task("Finish this tutortial", date(2015, 3, 13), 10, 1))
#db.session.add(Task("Finish this Real Python", date(2015, 3, 13), 10, 1))

db.session.commit()
