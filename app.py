
from flask import Flask,render_template, url_for;


app = Flask(__name__)

posts = [
    {
        'author':'JV',
        'title':'Blog Post 1',
        'content':'First Post content',
        'date_posted': 'April 20,2019',
    },
    {
        'author':'MJV',
        'title':'Blog Post 2',
        'content':'Second Post content',
        'date_posted': 'April 21,2019',
    },

    {
        'author':'CR7',
        'title':'Blog Post 3',
        'content':'Third Post content',
        'date_posted': 'April 22,2019',
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", posts=posts, title='Home')

@app.route("/about")
def about():
    return render_template("about.html",title='About')

if __name__=="__main__":
    app.run(debug=True)
