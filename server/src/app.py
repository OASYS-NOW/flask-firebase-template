from flask import Flask, render_template, make_response
import os
import time

app = Flask(__name__)

# app_data = {
#     "name":         "Peter's Starter Template for a Flask Web App",
#     "description":  "A basic Flask app using bootstrap for layout",
#     "author":       "Peter Simeth",
#     "html_title":   "Peter's Starter Template for a Flask Web App",
#     "project_name": "Starter Template",
#     "keywords":     "flask, webapp, template, basic"
# }
#
#
# @app.route('/')
# def index():
#     return render_template('home/index.html', app_data=app_data)
#
#
# @app.route('/about')
# def about():
#     return render_template('about.html', app_data=app_data)
#
#
# @app.route('/service')
# def service():
#     return render_template('service.html', app_data=app_data)
#
#
# @app.route('/contact')
# def contact():
#     return render_template('contact.html', app_data=app_data)

@app.route('/')
def index():
    # context = { 'server_time': format_server_time() }
    # 1
    template = render_template('home/index.html') #, context=context)
    # 2
    response = make_response(template)
    # 3
    response.headers['Cache-Control'] = 'public, max-age=300, s-maxage=600'
    return response

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=int(os.environ.get('PORT', 8080)))