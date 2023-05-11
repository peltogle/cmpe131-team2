import locale
from supabase import create_client, Client
# IMPROVE: remove unnecessary imports
from flask import Flask, render_template, flash, redirect, url_for, request, session, make_response

SUPABASE_URL = "https://yxvtigsplpdppgwlktpn.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Inl4dnRpZ3NwbHBkcHBnd2xrdHBuIiwicm9sZSI6ImFub24iLCJpYXQiOjE2NzkyMDUwNzMsImV4cCI6MTk5NDc4MTA3M30.S_V8wk3u2hKG5p2XL5TlQfYGwYxzNh488Y7vzz-UTXY"
SALAD_URL = "https://yxvtigsplpdppgwlktpn.supabase.co/storage/v1/object/public/website_assets/website_images/green_salad.png"
VERSION = "0.3.1"

# Set locale for float to dollar conversion
locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')

# Create Flask app instance
app = Flask(__name__, static_url_path='', static_folder='static/')
app.secret_key = SUPABASE_KEY

# Create Supabase app instance
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

# -------------------------------------------------------------------------------------------------
# TODO: handle bad input of forms (length, repeat user, wrong password, wrong email, etc)
# TODO: add a banner that confirms user interaction or error (addition, can't add more, order etc)
# TODO: order page (technically optional)


@app.route('/orders')
def orders():
    if fetch_state():
        userCart = Cart()
        pageDescription = "Here are all the orders."
        return render_template('orders.html',
                               activePage="orders",
                               pageTitle="All Orders",
                               pageDescription=pageDescription,
                               activeSession=fetch_state(),
                               itemCount=userCart.itemCount)
    else:
        return redirect(url_for('index'))


# -------------------------------------------------------------------------------------------------

# Inject global variable into each pag


@app.context_processor
def inject_globals():
    return {'green_salad_url': SALAD_URL, 'version': VERSION}

# Check for user session based on uid


def fetch_state():
    if 'uid' in session:
        # Logged in
        session['logged_in'] = True
        fetch_and_calc_session(session['uid'])
    else:
        # Logged out
        session.clear()
        session['logged_in'] = False
        session['items_count'] = 0

# Grab data from database and calculate data based database output
# IMPROVE: make more lean, can be split into fetch and calc


def fetch_and_calc_session(uid):
    # Database var
    supaResponse = supabase.table('carts').select(
        '*').eq('created_by', uid).limit(1).execute()

    # Check database for user cart, if it does not exist, make one and refresh the supaResponse variable
    if len(dict(supaResponse)["data"]) == 0:
        supabase.table('carts').insert(
            {'created_by': uid, 'items': {}}).execute()
        supaResponse = supabase.table('carts').select(
            '*').eq('created_by', uid).limit(1).execute()
        session['shipping_cost'] = False
        session['total_cost'] = None
        session['formatted_total_cost'] = None
        session['local_items_dic'] = {}
        session['items_count'] = 0
        return redirect(url_for('index'))
    else:
        # Init keys and temp vars for users with a cart already
        totalWeight: float = 0
        totalCost: float = 0
        session['local_items_dic'] = dict(
            supaResponse)["data"][0]["items"]
        session['items_count'] = len(session['local_items_dic'])

        # Calc total weight and total cost without shipping
        for key in session['local_items_dic']:
            supabaseItemInfo = dict(supabase.table('catalog').select(
                '*').eq('item_id', key).limit(1).execute())["data"][0]
            totalWeight += float(supabaseItemInfo.get("weight")) * \
                float(session['local_items_dic'].get(key))
            totalCost += float(supabaseItemInfo.get("price")) * \
                float(session['local_items_dic'].get(key))

        # Calc shipping cost and add to total cost
        if totalWeight > 20:
            session['shipping_cost'] = True
            session['total_cost'] = totalCost + 5
        else:
            session['shipping_cost'] = False
            session['total_cost'] = totalCost

        # Convert into formatted USD currency
        session['formatted_total_cost'] = locale.currency(
            session['total_cost'], grouping=True)


"""
# start addItem
#
[-] Check if item already is in cart, if so add the additional quantity to the cart, if not add to cart normally
[-] If the quantity in the cart exceeds stock, trim down to the highest amount that can be ordered and issue error
[-] Recalculate data
#
# end addItem
"""


def addItem(item_id, quantity):
    if item_id in session['local_items_dic']:
        potItemCount = int(session['local_items_dic'][item_id]) + int(quantity)
        totalStock = dict(supabase.table('catalog').select('*').eq('item_id', item_id).limit(1).execute())["data"][0].get("stock")
        if potItemCount > totalStock:
            session['local_items_dic'][item_id] = totalStock
        else:
            session['local_items_dic'][item_id] = int(session['local_items_dic'][item_id]) + int(quantity)
    else:
        session['local_items_dic'][item_id] = quantity
    supabase.table('carts').update({"items": session['local_items_dic']}).eq(
        'created_by', session['uid']).execute()
    fetch_and_calc_session(session['uid'])


"""
# start removeItem
#
[-] Remove the item (check if item in list)
[-] Recalculate data
#
# end removeItem
"""


def removeItem(item_id):
    if item_id not in session['local_items_dic']:
        flash('item not in list!')
    else:
        session['local_items_dic'].pop(item_id)
    supabase.table('carts').update({"items": session['local_items_dic']}).eq(
        'created_by', session['uid']).execute()
    fetch_and_calc_session(session['uid'])


@app.route('/')
def index():
    fetch_state()
    pageTitle = "Home"
    activePage = "home"
    return render_template('index.html',
                           activePage=activePage,
                           pageTitle=pageTitle,
                           activeSession=session['logged_in'],
                           itemCount=session['items_count'])


@app.route('/catalog/<category>', methods=('GET', 'POST'))
def catalog(category):
    # List of available categories
    categories = ['fruits', 'vegetables', 'meats', 'beverages']

    # Check which category it is and reject non-existent ones
    if category not in categories:
        # Handle unknown categories
        return "Invalid category"
    else:
        fetch_state()
        if category == 'fruits':
            pageDescription = "Explore a vibrant assortment of fresh and juicy fruits to add a burst of flavor and nutrition to your meals."
        elif category == 'vegetables':
            pageDescription = "Discover a colorful selection of farm-fresh vegetables packed with vitamins and minerals for wholesome cooking and healthy eating."
        elif category == 'meats':
            pageDescription = "Indulge in a variety of high-quality meats, including tender cuts and flavorful options, to create savory dishes that satisfy every palate."
        elif category == 'beverages':
            pageDescription = "Quench your thirst with a wide range of refreshing beverages, from revitalizing juices to energizing drinks, perfect for any occasion."

        # Handle adding item to cart
        if request.method == 'POST':
            quantityNeeded = request.form['quantityNeeded']
            itemNeeded = request.form['itemNeeded']
            if not quantityNeeded:
                flash('Quantity is required!')
            elif not itemNeeded:
                flash('Item is required!')
            else:
                addItem(itemNeeded, quantityNeeded)
                # TODO: add a banner that says item added

        # Pull catalog from database
        supaResponse = supabase.table('catalog').select(
            '*').eq('type', f'{category}').execute()
        return render_template('catalog.html',
                               activePage=category,
                               pageTitle=category.capitalize(),
                               pageDescription=pageDescription,
                               response=supaResponse,
                               activeSession=session['logged_in'],
                               itemCount=session['items_count'])


@app.route('/auth/<type>', methods=('GET', 'POST'))
def auth(type):
    # List of available types
    types = ['signin', 'signup', 'signout']

    # Check which category it is and reject non-existent ones
    if type not in types:
        # Handle unknown types
        return "Invalid authentication method"
    elif type == 'signout' and session['logged_in']:
        session.pop('uid')
        fetch_state()
        return redirect(url_for('index'))
    elif not session['logged_in']:
        fetch_state()
        if type == 'signin':
            pageTitle = "Sign In"
            pageDescription = "Welcome! Please fill in the information below to sign in."
        elif type == 'signup':
            pageTitle = "Sign Up"
            pageDescription = "Welcome! Please fill in the information below to sign up."
        
        # Handle form request
        if request.method == 'POST':
            userEmail = request.form['userEmailInput']
            userPassword = request.form['userPasswordInput']
            if not userEmail:
                flash('Email is required!')
            elif not userPassword:
                flash('Password is required!')
            elif type == 'signup':
                supabase.auth.sign_up(
                    {"email": userEmail, "password": userPassword})
                session['uid'] = supabase.auth.get_session().user.id
                fetch_state()
                supabase.auth.sign_out()
                return redirect(url_for('index'))
            elif type == 'signin':
                supabase.auth.sign_in_with_password(
                    {"email": userEmail, "password": userPassword})
                session['uid'] = supabase.auth.get_session().user.id
                fetch_state()
                supabase.auth.sign_out()
                return redirect(url_for('index'))

        # Return page for those not logged in
        return render_template('auth.html',
                               activePage=type,
                               pageTitle=pageTitle,
                               pageDescription=pageDescription,
                               activeSession=session['logged_in'])
    else:
        return redirect(url_for('index'))

# A class to help display items in the cart on the cart page


class FoodItem:
    # Init variables
    itemName = None
    itemPrice = itemWeight = itemQuantity = itemId = 0

    # Constructor
    def __init__(self, itemName, itemPrice, itemWeight, itemQuantity, itemId):
        self.itemName = itemName
        self.itemPrice = locale.currency(itemPrice, grouping=True)
        self.itemWeight = itemWeight
        self.itemQuantity = itemQuantity
        self.itemId = itemId


@app.route('/cart', methods=('GET', 'POST'))
def cart():
    if session['logged_in']:
        pageDescription = "Here is your cart."
        userItems = []
        for key in session['local_items_dic']:
            catalogInfo = dict(supabase.table('catalog').select(
                '*').eq('item_id', key).limit(1).execute())["data"][0]
            userItems.append(FoodItem(catalogInfo.get("name"), catalogInfo.get(
                "price"), catalogInfo.get("weight"), session['local_items_dic'].get(key), catalogInfo.get("item_id")))

        # Handle remove or checkout
        if request.method == 'POST':
            """ 
            # start placeOrder
            #
            [ ] TODO: Update stock (both ends) 
            [-] Place order
            [-] Move order to orders catalog so that user can create a new order
            [-] Redirect to orders page
            #
            # end placeOrder
            """
            if 'make_order' in request.form:
                addressInput = request.form['addressInput']
                countryInput = request.form['countryInput']
                stateInput = request.form['stateInput']
                zipInput = request.form['zipInput']
                nameInput = request.form['nameInput']
                ccNumberInput = request.form['ccNumberInput']
                ccExpirationInput = request.form['ccExpirationInput']
                ccCvvInput = request.form['ccCvvInput']
                if not addressInput:
                    flash("Address is required!")
                elif not countryInput:
                    flash("Country is required!")
                elif not stateInput:
                    flash("State is required!")
                elif not zipInput:
                    flash("ZIP code is required!")
                elif not nameInput:
                    flash("Name on card is required!")
                elif not ccNumberInput:
                    flash("Credit card number is required!")
                elif not ccExpirationInput:
                    flash("Credit card expiration is required!")
                elif not ccCvvInput:
                    flash("CVV is required!")
                else:
                    for key in session['local_items_dic']:
                        catalogInfo = dict(supabase.table('catalog').select('*').eq('item_id', key).limit(1).execute())["data"][0]
                        if catalogInfo.get("stock") < int(session['local_items_dic'].get(key)):
                            session['local_items_dic'][key] = catalogInfo.get("stock")
                        newStockAmount = catalogInfo.get("stock") - int(session['local_items_dic'][key])
                        supabase.table("catalog").update({"stock": newStockAmount}).eq('item_id', key).execute()
                    supabase.table('carts').update({"items": session['local_items_dic']}).eq('created_by', session['uid']).execute()
                    fetch_and_calc_session(session['uid'])
                    addressInfo = {'address': addressInput, 'country': countryInput, 'state': stateInput, 'zip': zipInput}
                    ccInfo = {'name': nameInput, 'ccNumber': ccNumberInput, 'ccExpiration': ccExpirationInput, 'ccCvv': ccCvvInput}
                    supabase.table('orders').insert({'user': session['uid'], 'items': session['local_items_dic'], 'total': session['total_cost'], 'shipping': session['shipping_cost'], 'address': addressInfo, 'cc info': ccInfo}).execute()
                    supabase.table("carts").delete().eq("created_by", session['uid']).execute()
                    return redirect(url_for('orders'))
            else:
                itemId = request.form['itemId']
                if not itemId:
                    flash('Id is required!')
                else:
                    for item in userItems:
                        if item.itemId == itemId:
                            userItems.remove(item)
                    removeItem(itemId)
                    return redirect(url_for('cart'))
        return render_template('cart.html',
                               activePage="cart",
                               pageTitle="Cart",
                               pageDescription=pageDescription,
                               activeSession=session['logged_in'],
                               itemCount=session['items_count'],
                               totalCost=session['formatted_total_cost'],
                               shippingCost=session['shipping_cost'],
                               userItems=userItems)
    else:
        return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(host="127.0.0.1", port=5000, debug=True)
    # IMPROVE: remove debug in production if it doesn't do it already
