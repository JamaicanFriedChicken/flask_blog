from flask import Flask, render_template, url_for
app = Flask(__name__)

posts = [
    {
        'author': 'Jirapat Kleepbua',
        'title': 'Blog Post 1',
        'content': 'I love Michael Lue and His FAT, too bad he isnt like Nick Young',
        'date_posted': 'June 22, 2019'
    },
    {
        'author': 'Ngimanita',
        'title': 'Blog Post 2',
        'content': 'I love P Toon!! and Fern my Side Chick',
        'date_posted': 'June 23,2019'
    },
    {
        'author': 'Moness',
        'title': 'Blog Post 3',
        'content': 'Michaeeeeeeeeel! Nine wants to go Hasong and Korean BBQ',
        'date_posted': 'June 25, 2019'
    }
]

@app.route("/")
def hello():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html', title='About')

if __name__ == '__main__':
    app.run(debug=True)
