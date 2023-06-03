from flask import Flask,render_template,request,jsonify
app = Flask(__name__)
@app.route('/',methods=['GET','POST'])
def home_page():
   return render_template('index.html')
@app.route('/math',methods=['POST'])
def math_operation():
    if (request.method=='POST'):
       ops=request.form['operation']
       a= int(request.form['num1'])
       b= int(request.form['num2'])
       if(ops=='add'):
          r = a+b 
          res = 'Sum of the ' +str(a) + " and " + str(b)+' is '+str(r)

       if(ops=='subtract'):
          r = a-b 
          res = 'Subtract  of  the  '  +str(a) +  "  and  " + str(b)+'  is  '+str(r)
       if(ops=='multiply'):
          r = a*b 
          res = 'Multiply of  the  '  +str(a) +  "  and  " + str(b)+'  is  '+str(r)
       if(ops=='divide'):
          r = a/b 
          res = 'Divide  of  the  '  +str(a) +  "  and  " + str(b)+'  is  '+str(r)
      

       return render_template('result.html',result=res)
#api testing with postman 
@app.route('/post_man',methods=['POST'])
def math_operation1():
    if (request.method=='POST'):
       ops=request.json['operation']
       a= int(request.json['num1'])
       b= int(request.json['num2'])
       if(ops=='add'):
          r = a+b 
          result = 'Sum of the ' +str(a) + " and " + str(b)+' is '+str(r)

       if(ops=='subtract'):
          r = a-b 
          result = 'Subtract  of  the  '  +str(a) +  "  and  " + str(b)+'  is  '+str(r)
       if(ops=='multiply'):
          r = a*b 
          result = 'Multiply of  the  '  +str(a) +  "  and  " + str(b)+'  is  '+str(r)
       if(ops=='divide'):
          r = a/b 
          result = 'Divide  of  the  '  +str(a) +  "  and  " + str(b)+'  is  '+str(r)
      

       return  jsonify(result)

if __name__ =="__main__":
   app.run( host="0.0.0.0")
