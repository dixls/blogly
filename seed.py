from models import User, db, Post, Tag, PostTag
from app import app

db.drop_all()
db.create_all()

User.query.delete()

alan = User(first_name='Alan', last_name='Alda', img_url='https://www.hollywoodreporter.com/wp-content/uploads/2019/01/20181025_0023_f-h_2019_thr.jpg')

db.session.add(alan)
db.session.commit()

new_post = Post(title="My Article", 
                content="Being a professional funny man, I have a lot of very important opinions", 
                user_id=1)

db.session.add(new_post)
db.session.commit()

tag1 = Tag(name="commentary")
tag2 = Tag(name="thoughts")
tag3 = Tag(name="shitposting")

db.session.add_all([tag1, tag2, tag3])
db.session.commit()