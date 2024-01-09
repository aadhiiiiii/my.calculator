from flask import Flask, renter_template,reguest
app=Flask(__name__)
@app.route('/')
def hello():
    
    return renter_template('index.html')
@app.route("/result",method=['GET','POST'])
def hi():
    if request.method=='POST':
        num1=request.form['num1']
        num2=request.form['num2']
        radio=request.form['radio']

        output=cal(int(res))
    return renter_template('result.html',output=output)
def cal(radio):
    if radio==addition:
        res=num1+num2
        return res
    elif radio==subtraction:
        res=num1-num2
        return res
    elif radio==multipliction:
        res=num1*num2
        return res
    elif radio==division:
        res=num1/num2
        return res
if__name__=='__main__':
    app.run()

            
