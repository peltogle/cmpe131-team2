from flask import Flask, render_template, request, url_for, flash, redirect
from supabase import create_client, Client

app = Flask(__name__, static_url_path='', static_folder='static/')
supabase: Client = create_client("https://yxvtigsplpdppgwlktpn.supabase.co", "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Inl4dnRpZ3NwbHBkcHBnd2xrdHBuIiwicm9sZSI6ImFub24iLCJpYXQiOjE2NzkyMDUwNzMsImV4cCI6MTk5NDc4MTA3M30.S_V8wk3u2hKG5p2XL5TlQfYGwYxzNh488Y7vzz-UTXY")
activeSession = supabase.auth.get_session()

# Global vars
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
    return render_template('index.html', activePage = "home", pageTitle = "Home", activeSession = returnActiveSession())


@app.route('/fruits')
def catalogF():
    pageTitle= "Fruits"
    activePage = "fruits"
    pageDescription = "Lorem"
    supaResponse = supabase.table('catalog').select('*').eq('type', 'fruits').execute()
    return render_template('catalog.html', activePage = activePage, pageTitle = pageTitle, pageDescription = pageDescription, response = supaResponse, activeSession = returnActiveSession())


@app.route('/vegetables')
def catalogV():
    pageTitle= "Vegetables"
    activePage = "vegetables"
    pageDescription = "Lorem"
    supaResponse = supabase.table('catalog').select('*').eq('type', 'vegetables').execute()
    return render_template('catalog.html', activePage = activePage, pageTitle = pageTitle, pageDescription = pageDescription, response = supaResponse, activeSession = returnActiveSession())


@app.route('/meats')
def catalogM():
    pageTitle= "Meats"
    activePage = "meats"
    pageDescription = "Lorem"
    supaResponse = supabase.table('catalog').select('*').eq('type', 'meats').execute()
    return render_template('catalog.html', activePage = activePage, pageTitle = pageTitle, pageDescription = pageDescription, response = supaResponse, activeSession = returnActiveSession())


@app.route('/beverages')
def catalogB():
    pageTitle= "Beverages"
    activePage = "beverages"
    pageDescription = "Lorem"
    supaResponse = supabase.table('catalog').select('*').eq('type', 'beverages').execute()
    return render_template('catalog.html', activePage = activePage, pageTitle = pageTitle, pageDescription = pageDescription, response = supaResponse, activeSession = returnActiveSession())


# TODO: fix validation (password length)
@app.route('/signup', methods=('GET', 'POST'))
def signUp():
    if request.method == 'POST':
        userEmail = request.form['userEmailInput']
        userPassword = request.form['userPasswordInput']
        if not userEmail:
            flash('Email is required!')
        elif not userPassword:
            flash('Password is required!')
        else:
            supabase.auth.sign_up({"email": userEmail, "password": userPassword})
            # Disable email verify
            return redirect(url_for('index'))
    pageDescription = "Welcome! Please fill in the information below to sign up."
    return render_template('signup.html', activePage = "signup", pageTitle = "Sign Up", pageDescription = pageDescription, activeSession = returnActiveSession())


@app.route('/signin', methods=('GET', 'POST'))
def signIn():
    if request.method == 'POST':
        userEmail = request.form['userEmailInput']
        userPassword = request.form['userPasswordInput']
        if not userEmail:
            flash('Email is required!')
        elif not userPassword:
            flash('Password is required!')
        else:    
            supabase.auth.sign_in_with_password({"email": userEmail, "password": userPassword})
            return redirect(url_for('index'))
    pageDescription = "Welcome! Please fill in the information below to sign in."
    return render_template('signin.html', activePage = "signin", pageTitle = "Sign In", pageDescription = pageDescription, activeSession = returnActiveSession())


@app.route('/signout')
def signOut():
    supabase.auth.sign_out()
    return redirect(url_for('index'))


# TODO: fix being able to go to these links when not signed in
@app.route('/orders')
def orders():
    if returnActiveSession:
        pageDescription = "Here are all the orders."
        return render_template('orders.html', activePage = "orders", pageTitle = "All Orders", pageDescription = pageDescription, activeSession = returnActiveSession())
    else:
        return redirect(url_for('index'))


@app.route('/cart')
def cart():
    print(returnActiveSession)
    if returnActiveSession:
        pageDescription = "Here is your cart."
        return render_template('cart.html', activePage = "cart", pageTitle = "Cart", pageDescription = pageDescription, activeSession = returnActiveSession())
    else:
        return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(host="127.0.0.1", port=5000, debug=True)