from flask import Flask,url_for,render_template,flash,redirect
from forms import RegistrationForm,LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'c0bee25330b97bae81e3139f136725c1'
                            
posts = [
    {
        'author':'Mahesh',
        'title':'First blog',
        'content':'This is the first blog...',
        'date':'april 2022'
    },
    {
        'author':'manmohan',
        'title':'second blog',
        'content':'This is the second blog...',
        'date':'march 2022'
    }
    ,{
        'author':'manmohan',
        'title':'second blog',
        'content':'This is the second blog...',
        'date':'march 2022'
    },{
        'author':'manmohan',
        'title':'second blog',
        'content':'This is the second blog...',
        'date':'march 2022'
    }
]

@app.route("/") 
@app.route("/home")
def home():
    return render_template('home.html',posts=posts)

@app.route("/about")
def about():
    return render_template('about.html',title='About')

@app.route("/register",methods=['GET', 'POST'])
def register():
    form=RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!','success')
        return redirect(url_for('home'))
    return render_template('register.html',title='Register',form=form)

@app.route("/login",methods=['GET','POST'])
def login():
    form=LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'mahesh@gmail.com' and form.password.data == 'Pass123':
            flash(f'You have been logged in!','success')
            return redirect(url_for('home'))
        else:
            flash(f'Login unsuccessful! Please check email and password')
    return render_template('login.html',title='Login',form=form)



if __name__=="__main__":
    app.run(debug=True)