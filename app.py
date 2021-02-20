# ---------------------------- Import libraries --------------------------------------#
# Flask
from flask import Flask
from flask import render_template, jsonify, request 
# Classify function
from inference import classify

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])

def classify_app():
    # Write the POST method to post the result
    if request.method=='POST' : 
        # Read article from textarea
        article =request.form.get('article')
        # Check if the article is not empty
        if article : 
            # Get prediction of the article
            user_prediction = classify(article)
            # Convert the prediction from english to arabic
            if user_prediction[0] == 'Culture':
                user_prediction = 'تم تصنيف مقالتك على انها:  مـقالـة ثـقـافـيـة'
            elif user_prediction[0] == 'Finance':
                user_prediction = 'تم تصنيف مقالتك على انها : مـقالـة إقـتـصـاديـة'
            elif user_prediction[0] == 'Medical':
                user_prediction = 'تم تصنيف مقالتك على انها : مـقالـة صـحـيـة'
            elif user_prediction[0] == 'Politics':
                user_prediction = 'تم تصنيف مقالتك على انها : مـقالـة سـيـاسـيـة'
            elif user_prediction[0] == 'Sports':
                user_prediction = 'تم تصنيف مقالتك على انها : مـقالـة ريـاضـيـة'
            elif user_prediction[0] == 'Tech':
                user_prediction = 'تم تصنيف مقالتك على انها : مـقالـة تـقـنـيـة'
            else:
                user_prediction = 'لا يـمـكـن تـحـديـده'
            # Return the result
            return jsonify(result=user_prediction)
        # If the article is empty
        else : 
            # Return the error message
            return jsonify(result='الرجاء إدخال نص الخبر ')
    # Render the index template
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
    