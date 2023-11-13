from sqlalchemy import Column, Integer, String, Float, ForeignKey
from APP import db, app
from sqlalchemy.orm import relationship

class User(db.Model):
    id = Column(Integer, primary_key=True, autoincrement= True)
    name = Column(String(50), nullable=False)
    username = Column(String(50), nullable=False, unique=True)
    password = Column(String(50), nullable=False)
    avatar = Column(String(100), default= 'https://cdn-icons-png.flaticon.com/512/6596/6596121.png')
    def __str__(self):
        return self.name

class Category(db.Model):
    __tablename__ = 'category'

    id  = Column(Integer, primary_key= True, autoincrement= True)
    name = Column(String(50), nullable= True)
    products = relationship('Product', backref='category', lazy= True)

    def __str__(self):
        return self.name

class Product(db.Model):
    __tablename__ = 'product'

    id  = Column(Integer, primary_key= True, autoincrement= True)
    name = Column(String(50), nullable= True)
    price = Column(Float)
    image = Column(String(100))
    category_id= Column(Integer, ForeignKey(Category.id))

    def __str__(self):
        return self.name

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        import hashlib
        u = User(name= 'admin', username= 'admin', password= str(hashlib.md5('Admin123'.encode('utf-8')).hexdigest()))
        db.session.add(u)
        db.session.commit()
        # c1 = Category(name='Mobile')
        # c2 = Category(name='Tablet')
        # c3 = Category(name='Desktop')
        # db.session.add(c1)
        # db.session.add(c2)
        # db.session.add(c3)
        # db.session.commit()

