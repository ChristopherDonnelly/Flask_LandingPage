'''
Create a flask project capable of handling the following routes.

localhost:5000/    
This route should serve a view file called index.html and display a greeting. This will be considered our 'root route'.

localhost:5000/ninjas    
This route should serve a view file called ninjas.html and display information about ninjas.

localhost:5000/dojos/new    
This route should serve a view file called dojos.html and have a form. Don't worry where the form should be sent to for now, you can simply set your action blank, like this:action=''.

Next Steps
Create a folder inside of your project labeled static. This static folder will be used to serve all of our static content, such as stylesheets, images, and javascript files! Now place a stylesheet in the static folder and reference it in our view files (templates).
'''

# Import Flask to allow us to create our app, and import
# render_template to allow us to render HTML Files.
from flask import Flask, render_template, request, redirect

app = Flask(__name__)                     # Global variable __name__ tells Flask whether or not we
                                          # are running the file directly or importing it as a module.

@app.route('/')                           # The "@" symbol designates a "decorator" which attaches the
                                          # following function to the '/' route. This means that
                                          # whenever we send a request to localhost:5000/ we will run
                                          # the following "hello_world" function.

def display_index():
  return render_template('index.html')    # Render the template and return it!

@app.route('/ninjas')

def display_ninja():
  return render_template('ninjas.html')    # Render the template and return it!

# @app.route('/dojos')

# def display_dojos():
#   return render_template('dojos.html')    # Render the template and return it!

@app.route('/dojos/new', methods=['GET', 'POST'])
def create_user():

    if request.method == 'POST':
        print "Got Post Info"
        # we'll talk about the following two lines after we learn a little more
        # about forms
        name = request.form['name']
        email = request.form['email']       # redirects back to the '/' route
        return redirect('/dojos/new')
    else:    
        return render_template('dojos.html')

app.run(debug=True)                       # Run the app in debug mode.