from flask import Flask, render_template, request

app=Flask(__name__)

@app.route('/')
def home():
    name="Kritika"
    age=20
    projects=["Weather App","Calculator","Shopping Cart"]
    return render_template ('index1.html',name=name,age=age,projects=projects)

@app.route('/greet', methods=['POST'])
def greet():
    name = request.form['username']
    return f"Hello {name}!"

if __name__=='__main__':
    app.run(debug=True)
