## Jinja2 template engine

'''
{{  }} expression to print output in html
{%....%} conditions, for loops
{#...#} for comments
'''

from flask import Flask, render_template, request, redirect, url_for

app=Flask(__name__)

@app.route('/',methods =['GET'])
def home():
    return render_template('index.html')

@app.route('/form',methods = ['GET','POST'])
def form():
    if request.method == 'POST':
        name = request.form['name']
        return f"Welcome! {name}!!!"
    return render_template('form.html')

# @app.route('/submit',methods = ['POST'])
# def submit():
#     name = request.form['name']
#     return f"Welcome! {name}!!!"

@app.route('/about')
def about():
    return render_template('about.html')

## variable rule
@app.route('/success/<int:score>') ## score also works
def success(score):
    res=""
    if score>=50:
        res="PASS"
    else:
        res="FAIL"

    return render_template('result.html',results=res)


## variable rule
@app.route('/successres/<int:score>') ## score also works
def successres(score):
    res=""
    if score>=50:
        res="PASS"
    else:
        res="FAIL"

    exp={'score':score,"res":res}

    return render_template('result1.html',results=exp)

## if condition
@app.route('/successif/<int:score>') ## score also works
def successres1(score):
    return render_template('result2.html',results=score)

## variable rule
@app.route('/fail/<int:score>') ## score also works
def fail(score):

    return render_template('result.html',results=score)

@app.route("/submit",methods=['POST','GET'])
def submit():
    total_score = 0
    if request.method=='POST':
        science = float(request.form['science'])
        maths = float(request.form['maths'])
        c = float(request.form['c'])
        data_science = float(request.form['datascience'])

        total_score=(science+maths+c+data_science)/4

    else:
        return render_template('getresult.html')
    return redirect(url_for('successres',score = total_score))
    
if __name__ == "__main__":
    app.run(debug=True)