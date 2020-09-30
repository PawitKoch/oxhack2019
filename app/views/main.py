from flask import render_template, jsonify, request
from app import app
from predictor_handler import predict
from plot_handler import create_plot
import os

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Home')

@app.route('/uploaded', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if request.files:
            f = request.files["image"]
            path = os.path.join(app.config['UPLOAD_FOLDER'], f.filename)
            # print(f.filename)
            predictions = predict(path) #from predictor_handler.py
    #return top three predictions
    predictions = {i: predictions[i] for i in list(predictions.keys())[:3]}
    plot, carbon = create_plot(predictions) #from plot_handler.py
    return render_template('uploaded.html', title='Success',
                            predictions=predictions, plot=plot,
                            carbon=carbon, user_image=f.filename)

@app.route('/about')
def about():
    return render_template('about.html', title='About')
