# app.py
from flask import Flask, render_template, request
from transformers import pipeline

app = Flask(__name__)

summarizer = pipeline("summarization")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/summarize', methods=['POST'])
def summarize_text():
    if request.method == 'POST':
        text = request.form['text']
        summarized_text = summarizer(text, max_length=150, min_length=50, length_penalty=2.0, num_beams=4)[0]['summary_text']
        return render_template('result.html', text=text, summarized_text=summarized_text)

if __name__ == '__main__':
    app.run(debug=True)
