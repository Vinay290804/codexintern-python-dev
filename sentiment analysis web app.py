from flask import Flask, render_template, request
from textblob import TextBlob

app = Flask(_name_)

@app.route('/', methods=['GET', 'POST'])
def sentiment_analysis():
    if request.method == 'POST':
        text = request.form['text']
        analysis = TextBlob(text)
        polarity = analysis.sentiment.polarity
        subjectivity = analysis.sentiment.subjectivity
        
        if polarity > 0.2:
            sentiment = "Positive"
        elif polarity < -0.2:
            sentiment = "Negative"
        else:
            sentiment = "Neutral"
            
        return render_template('result.html', 
                            text=text,
                            sentiment=sentiment,
                            polarity=f"{polarity:.2f}",
                            subjectivity=f"{subjectivity:.2f}")
    
    return render_template('index.html')

if _name_ == '_main_':
    app.run(debug=True)