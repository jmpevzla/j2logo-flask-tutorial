from flask import Flask, render_template
app = Flask(__name__)

# @app.route('/')
# def hello_world():
#     return 'Hello, World!'

posts = []

@app.route('/')
def index():
    #return "{} posts".format(len(posts))
    return render_template('index.j2', num_posts=len(posts))

@app.route('/p/<string:slug>/')
def show_post(slug):
    #return "Mostrando el post {}".format(slug)
    return render_template('post_view.j2', slug_title=slug)

@app.route("/admin/post/")
@app.route("/admin/post/<int:post_id>/")
def post_form(post_id=None):
    #return "post_form {}".format(post_id)
    return render_template('admin/post_form.j2', post_id=post_id)
