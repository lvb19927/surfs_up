# 1. Import Flask
from flask import Flask

# 2. Create an app
pop = Flask(__name__)

# 3. Define index route
@pop.route("/")
def index():
    return "Hello World!"

# 4. Define the about route
@pop.route("/about")
def about():
    return "Laine"
# 5. Define the contact route
@pop.route("/contact")
def contact():
    return "email here"
# 6. Define main behavior
if __name__=="__main__":
    pop.run(debug=True)