from flask import Flask,render_template,request,redirect
import csv

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

def write_to_csv(data):
    with open('data.csv','a',newline='') as csvfile:
        email = data['email']
        username = data['name']
        message = data['message']
        
        writer = csv.writer(csvfile, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
        writer.writerow([email,username,message])

@app.route('/submit_form',methods=['POST' ,'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        write_to_csv(data)
        return redirect('/thank-you.html')
    else:
        return 'Wrong input.Try again!'