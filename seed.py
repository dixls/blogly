from models import User, db
from app import app

db.drop_all()
db.create_all()

User.query.delete()

alan = User(first_name='Alan', last_name='Alda', img_url='https://www.hollywoodreporter.com/wp-content/uploads/2019/01/20181025_0023_f-h_2019_thr.jpg')

db.session.add(alan)

db.session.commit()