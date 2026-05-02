from flask import Flask, render_template

app=Flask(__name__)

@app.route('/')
def home():
    name="Kritika"
    age=20
    projects=["Weather App","Calculator","Shopping Cart"]
    return render_template ('index1.html',name=name,age=age,projects=projects)

if __name__=='__main__':
    app.run(debug=True)
