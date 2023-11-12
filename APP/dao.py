from APP.models import Category, Product
def get_categories():
    return Category.query.all()
def get_products(kw):
    products = Product.query
    if kw:
        products= products.filter(Product.name.contains(kw))
    return products.all()
    # products = [{
    #     "id" : 1,
    #     "name" : "Iphone 13",
    #     "price" : 20000000,
    #     "image" : "https://cdn2.cellphones.com.vn/insecure/rs:fill:358:358/q:80/plain/https://cellphones.com.vn/media/catalog/product/i/p/iphone-13_2_.png",
    #     "category_id" : 1
    # }, {
    #     "id" : 2,
    #     "name" : "Iphone 14",
    #     "price" : 25000000,
    #     "image" : "https://cdn2.cellphones.com.vn/insecure/rs:fill:358:358/q:80/plain/https://cellphones.com.vn/media/catalog/product/i/p/iphone-14_1.png",
    #     "category_id" : 1
    # }, {
    #     "id" : 3,
    #     "name" : "Iphone 15",
    #     "price" : 25000000,
    #     "image" : "https://cdn2.cellphones.com.vn/insecure/rs:fill:358:358/q:80/plain/https://cellphones.com.vn/media/catalog/product/i/p/iphone-15-plus_1__1.png",
    #     "category_id" : 1
    # }, {
    #     "id" : 4,
    #     "name" : "Iphone 12",
    #     "price" : 25000000,
    #     "image" : "https://cdn2.cellphones.com.vn/insecure/rs:fill:358:358/q:80/plain/https://cellphones.com.vn/media/catalog/product/i/p/iphone-12-128gb_2.png",
    #     "category_id" : 1
    # }, {
    #     "id" : 5,
    #     "name" : "Iphone 11",
    #     "price" : 25000000,
    #     "image" : "https://cdn2.cellphones.com.vn/358x/media/catalog/product/1/1/11._d_nn.jpg",
    #     "category_id" : 1
    #
    # }, {
    #     "id" : 6,
    #     "name" : "SSG S22",
    #     "price" : "25.000.000",
    #     "image" : "https://cdn2.cellphones.com.vn/insecure/rs:fill:358:358/q:80/plain/https://cellphones.com.vn/media/catalog/product/s/a/samsung-galaxy-s22-plus-256gb.png",
    #     "category_id" : 1
    # }, {
    #     "id" : 7,
    #     "name" : "SSG S23",
    #     "price" : 25000000,
    #     "image" : "https://cdn2.cellphones.com.vn/insecure/rs:fill:358:358/q:80/plain/https://cellphones.com.vn/media/catalog/product/s/a/samsung-galaxy-s23.png",
    #     "category_id" : 1
    # }]
    # if kw:
    #     products = [p for p in products if p['name'].find(kw) >= 0]
    # return products