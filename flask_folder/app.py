from flask import Flask, render_template, request, url_for, flash, redirect
from supabase import create_client, Client

app = Flask(__name__, static_url_path='', static_folder='static/')
supabase: Client = create_client("https://yxvtigsplpdppgwlktpn.supabase.co",
                                 "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Inl4dnRpZ3NwbHBkcHBnd2xrdHBuIiwicm9sZSI6ImFub24iLCJpYXQiOjE2NzkyMDUwNzMsImV4cCI6MTk5NDc4MTA3M30.S_V8wk3u2hKG5p2XL5TlQfYGwYxzNh488Y7vzz-UTXY")

@app.context_processor
def inject_globals():
    return {'green_salad_url': 'https://yxvtigsplpdppgwlktpn.supabase.co/storage/v1/object/public/website_assets/website_images/green_salad.png'}


def returnActiveSession():
    if supabase.auth.get_session() is not None:
        return True
    else:
        return False


@app.route('/')
def index():
    if returnActiveSession():
        userCart = Cart()
    else:
        userCart = FakeCart()
    return render_template('index.html',
                           activePage="home",
                           pageTitle="Home",
                           activeSession=returnActiveSession(),
                           itemCount=userCart.itemCount)


@app.route('/fruits', methods=('GET', 'POST'))
def catalogF():
    if returnActiveSession():
        userCart = Cart()
    else:
        userCart = FakeCart()
    if request.method == 'POST':
        # TODO: handle bad input
        quantityNeeded = request.form['quantityNeeded']
        itemNeeded = request.form['itemNeeded']
        if not quantityNeeded:
            flash('Quantity is required!')
        elif not itemNeeded:
            flash('Item is required!')
        else:
            userCart.addItem(itemNeeded, quantityNeeded)
            # TODO: add a banner that says item added
    pageTitle = "Fruits"
    activePage = "fruits"
    pageDescription = "Lorem"
    supaResponse = supabase.table('catalog').select('*').eq('type', 'fruits').execute()
    return render_template('catalog.html',
                           activePage=activePage,
                           pageTitle=pageTitle,
                           pageDescription=pageDescription,
                           response=supaResponse,
                           activeSession=returnActiveSession(),
                           itemCount=userCart.itemCount)


# TODO: add for all other items
@app.route('/vegetables')
def catalogV():
    if returnActiveSession():
        userCart = Cart()
    else:
        userCart = FakeCart()
    pageTitle = "Vegetables"
    activePage = "vegetables"
    pageDescription = "Lorem"
    supaResponse = supabase.table('catalog').select('*').eq('type', 'vegetables').execute()
    return render_template('catalog.html',
                           activePage=activePage,
                           pageTitle=pageTitle,
                           pageDescription=pageDescription,
                           response=supaResponse,
                           activeSession=returnActiveSession(),
                           itemCount=userCart.itemCount)


@app.route('/meats')
def catalogM():
    if returnActiveSession():
        userCart = Cart()
    else:
        userCart = FakeCart()
    pageTitle = "Meats"
    activePage = "meats"
    pageDescription = "Lorem"
    supaResponse = supabase.table('catalog').select('*').eq('type', 'meats').execute()
    return render_template('catalog.html',
                           activePage=activePage,
                           pageTitle=pageTitle,
                           pageDescription=pageDescription,
                           response=supaResponse,
                           activeSession=returnActiveSession(),
                           itemCount=userCart.itemCount)


@app.route('/beverages')
def catalogB():
    if returnActiveSession():
        userCart = Cart()
    else:
        userCart = FakeCart()
    pageTitle = "Beverages"
    activePage = "beverages"
    pageDescription = "Lorem"
    supaResponse = supabase.table('catalog').select('*').eq('type', 'beverages').execute()
    return render_template('catalog.html',
                           activePage=activePage,
                           pageTitle=pageTitle,
                           pageDescription=pageDescription,
                           response=supaResponse,
                           activeSession=returnActiveSession(),
                           itemCount=userCart.itemCount)


# TODO: fix validation (password length)
@app.route('/signup', methods=('GET', 'POST'))
def signUp():
    if returnActiveSession():
        userCart = Cart()
    else:
        userCart = FakeCart()
    if request.method == 'POST':
        userEmail = request.form['userEmailInput']
        userPassword = request.form['userPasswordInput']
        if not userEmail:
            flash('Email is required!')
        elif not userPassword:
            flash('Password is required!')
        else:
            supabase.auth.sign_up(
                {"email": userEmail, "password": userPassword})
            # TODO: Disable email verify
            return redirect(url_for('index'))
    pageDescription = "Welcome! Please fill in the information below to sign up."
    return render_template('signup.html',
                           activePage="signup",
                           pageTitle="Sign Up",
                           pageDescription=pageDescription,
                           activeSession=returnActiveSession(),
                           itemCount=userCart.itemCount)


@app.route('/signin', methods=('GET', 'POST'))
def signIn():
    if returnActiveSession():
        userCart = Cart()
    else:
        userCart = FakeCart()
    if request.method == 'POST':
        userEmail = request.form['userEmailInput']
        userPassword = request.form['userPasswordInput']
        if not userEmail:
            flash('Email is required!')
        elif not userPassword:
            flash('Password is required!')
        else:
            supabase.auth.sign_in_with_password(
                {"email": userEmail, "password": userPassword})
            return redirect(url_for('index'))
    pageDescription = "Welcome! Please fill in the information below to sign in."
    return render_template('signin.html',
                           activePage="signin",
                           pageTitle="Sign In",
                           pageDescription=pageDescription,
                           activeSession=returnActiveSession(),
                           itemCount=userCart.itemCount)


@app.route('/signout')
def signOut():
    supabase.auth.sign_out()
    return redirect(url_for('index'))


@app.route('/orders')
def orders():
    if returnActiveSession():
        userCart = Cart()
        pageDescription = "Here are all the orders."
        return render_template('orders.html',
                               activePage="orders",
                               pageTitle="All Orders",
                               pageDescription=pageDescription,
                               activeSession=returnActiveSession(),
                               itemCount=userCart.itemCount)
    else:
        return redirect(url_for('index'))


@app.route('/cart', methods=('GET', 'POST'))
def cart():
    if returnActiveSession():
        userCart = Cart()
        pageDescription = "Here is your cart."
        userItems = []
        for key in userCart.items:
            catalogInfo = dict(supabase.table('catalog').select('*').eq('item_id', key).limit(1).execute())["data"][0]
            userItems.append(FoodItem(catalogInfo.get("name"), catalogInfo.get(
                "price"), catalogInfo.get("weight"), userCart.items.get(key), catalogInfo.get("item_id")))
        if request.method == 'POST':
            itemId = request.form['itemId']
            if not itemId:
                flash('Id is required!')
            else:
                for item in userItems:
                    if item.itemId == itemId:
                        userItems.remove(item)
                userCart.removeItem(itemId)
                return redirect(url_for('cart'))
        return render_template('cart.html',
                               activePage="cart",
                               pageTitle="Cart",
                               pageDescription=pageDescription,
                               activeSession=returnActiveSession(),
                               itemCount=userCart.itemCount,
                               subTotal=userCart.subTotal,
                               totalCost=userCart.totalCost,
                               shippingCost=userCart.shippingCost,
                               userItems=userItems)
    # TODO: remove subtotal
    else:
        return redirect(url_for('index'))


class FoodItem:
    itemName = "Name"
    itemPrice = 0
    itemWeight = 0
    itemQuantity = 0
    itemId = 0

    def __init__(self, itemName, itemPrice, itemWeight, itemQuantity, itemId):
        self.itemName = itemName
        self.itemPrice = itemPrice
        self.itemWeight = itemWeight
        self.itemQuantity = itemQuantity
        self.itemId = itemId


class FakeCart:
    itemCount = 0


class Cart:
    # Class variables
    subTotal = 0
    itemCount = 0
    totalCost = 0
    shippingCost = False
    uuid = 0
    supaResponse = 0
    items = {}

    """ 
    # start Class constructor
    #
    [ ] TODO: Check if cart entry exists for user, if not, create one
    [-] If a cart entry exists run countItems, calcShipping, and calcTotal
    #
    # end Class constructor
    """

    def __init__(self):
        # Set instance variables
        self.uuid = supabase.auth.get_session().user.id
        self.supaResponse = supabase.table('carts').select('*').eq('created_by', self.uuid).limit(1).execute()
        # Check if a cart entry exists for the user already
        if False:  # self.supaResponse.count is None
            supabase.table('carts').insert(
                {'created_by': self.uuid, 'items': {}}).execute()
        self.items = dict(supabase.table('carts').select('items').eq('created_by', self.uuid).limit(1).execute())["data"][0]["items"]
        self.calcData()

    """ 
    # start calcData
    #
    [-] Calc total items
    [-] Check weights of all items in cart, it it exceeds 20lb add $5 shipping
    [-] Calculate total cost of all items in cart plus shipping
    #
    # end calcData
    """

    def calcData(self):
        # Calc total items
        self.itemCount = len(self.items)
        # Check item weights
        totalWeight = 0
        for key in self.items:
            catalogInfo = dict(supabase.table('catalog').select('*').eq('item_id', key).limit(1).execute())["data"][0]
            totalWeight += (catalogInfo.get("weight") * int(self.items.get(key)))
        if totalWeight >= 20:
            self.shippingCost = True
            self.totalCost += 5
        # Calc total cost plus shipping
        for key in self.items:
            catalogInfo = dict(supabase.table('catalog').select('*').eq('item_id', key).limit(1).execute())["data"][0]
            self.totalCost += (int(self.items.get(key)) * catalogInfo.get("price"))


    """ 
    # start addItem
    #
    [-] Check if item already is in cart, if so add the additional quantity to the cart, if not add to cart normally
    [ ] TODO: If the quantity in the cart exceeds stock, trim down to the highest amount that can be ordered and issue error
    [-] Recalculate data
    #
    # end addItem
    """

    def addItem(self, itemId, quantity):
        if itemId in self.items:
            self.items[itemId] += quantity
        else:
            self.items.update({itemId: quantity})
        supabase.table('carts').update({"items": self.items}).eq(
            'created_by', self.uuid).execute()
        self.calcData()

    """ 
    # start removeItem
    #
    [-] Remove the item (check if item in list)
    [-] Recalculate data
    #
    # end removeItem
    """
    def removeItem(self, itemId):
        if itemId not in self.items:
            flash('item not in list!')
        else:
            self.items.pop(itemId)
        supabase.table('carts').update({"items": self.items}).eq(
            'created_by', self.uuid).execute()  
        self.calcData()

    """ 
    # start placeOrder
    #
    [ ] TODO: Update stock then place order, send order to orders catalog so that user can create a new order, clear cart catalog entry
    [ ] TODO: Redirect to orders page
    #
    # end placeOrder
    """
    def placeOrder(self):
        pass


if __name__ == '__main__':
    app.run(host="127.0.0.1", port=5000, debug=True)
    # TODO: remove debug
