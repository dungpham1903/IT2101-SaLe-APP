from sqlalchemy import Column, Integer, String, Float, ForeignKey
from APP import db, app
from sqlalchemy.orm import relationship

class Category(db.Model):
    __tablename__ = 'category'

    id  = Column(Integer, primary_key= True, autoincrement= True)
    name = Column(String(50), nullable= True)

products = relationship('Product', backref='category', lazy= True)
class Product(db.Model):
    __tablename__ = 'product'

    id  = Column(Integer, primary_key= True, autoincrement= True)
    name = Column(String(50), nullable= True)
    price = Column(Float)
    image = Column(String(100), default='https://i1-vnexpress.vnecdn.net/2023/02/01/327930130-1584629158642723-553-6981-4746-1675237738.jpg')
    category_id= Column(Integer, ForeignKey(Category.id))

if __name__ == '__main__':
    with app.app_context():
        # c1 = Category(name='Mobile')
        # c2 = Category(name='Tablet')
        # c3 = Category(name='Desktop')
        # db.session.add(c1)
        # db.session.add(c2)
        # db.session.add(c3)
        # db.session.commit()

       db.create_all()