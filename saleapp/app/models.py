from sqlalchemy import Column, Integer, Float, String
from app import db, app


class Categories(db.Model):
    id = Column(Integer, primary_key=True, autoincrement= True)
    name = Column(String(50), unique=True)


#if __name__ == '__main__':
    #with app.app_context():
        #db.create_all()
        #c1 = Categories(name='Mobile')
        #c2 = Categories(name='Tablet')
        #c3 = Categories(name='laptop')

        #db.session.add_all([c1, c2, c3])
        #db.session.commit()
