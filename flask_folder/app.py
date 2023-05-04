import json, datetime
from flask import Flask, render_template
from supabase import create_client, Client

app = Flask(__name__, static_url_path='', static_folder='static/')
supabase: Client = create_client("https://yxvtigsplpdppgwlktpn.supabase.co", "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Inl4dnRpZ3NwbHBkcHBnd2xrdHBuIiwicm9sZSI6ImFub24iLCJpYXQiOjE2NzkyMDUwNzMsImV4cCI6MTk5NDc4MTA3M30.S_V8wk3u2hKG5p2XL5TlQfYGwYxzNh488Y7vzz-UTXY")


# Global vars
@app.context_processor
def inject_globals():
    return {'green_salad_url': 'https://yxvtigsplpdppgwlktpn.supabase.co/storage/v1/object/public/website_assets/website_images/green_salad.png'}


@app.route('/')
def index():
    return render_template('index.html', activePage = "home", pageTitle = "Home")


@app.route('/fruits')
def catalogF():
    pageTitle= "Fruits"
    activePage = "fruits"
    pageDescription = "Lorem"
    supaResponse = supabase.table('catalog').select('*').eq('type', 'fruits').execute()
    return render_template('catalog.html', activePage = activePage, pageTitle = pageTitle, pageDescription = pageDescription, response = supaResponse)


@app.route('/vegetables')
def catalogV():
    pageTitle= "Vegetables"
    activePage = "vegetables"
    pageDescription = "Lorem"
    supaResponse = supabase.table('catalog').select('*').eq('type', 'vegetables').execute()
    return render_template('catalog.html', activePage = activePage, pageTitle = pageTitle, pageDescription = pageDescription, response = supaResponse)


@app.route('/meats')
def catalogM():
    pageTitle= "Meats"
    activePage = "meats"
    pageDescription = "Lorem"
    supaResponse = supabase.table('catalog').select('*').eq('type', 'meats').execute()
    return render_template('catalog.html', activePage = activePage, pageTitle = pageTitle, pageDescription = pageDescription, response = supaResponse)


@app.route('/beverages')
def catalogB():
    pageTitle= "Beverages"
    activePage = "beverages"
    pageDescription = "Lorem"
    supaResponse = supabase.table('catalog').select('*').eq('type', 'beverages').execute()
    return render_template('catalog.html', activePage = activePage, pageTitle = pageTitle, pageDescription = pageDescription, response = supaResponse)

@app.route('/checkout')
def checkout():
    return render_template('checkout.html', activePage = "checkout", pageTitle = "Checkout")

@app.route('/signup')
def signUp():
    pageDescription = "Welcome! Please fill in the information below to sign up."
    return render_template('signup.html', activePage = "signup", pageTitle = "Sign Up", pageDescription = pageDescription)

if __name__ == '__main__':
    app.run(host="127.0.0.1", port=5000, debug=True)