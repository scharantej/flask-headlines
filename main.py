 
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    articles = [
        {
            'title': 'The First Article',
            'content': 'This is the content of the first article.'
        },
        {
            'title': 'The Second Article',
            'content': 'This is the content of the second article.'
        },
        {
            'title': 'The Third Article',
            'content': 'This is the content of the third article.'
        }
    ]
    return render_template('index.html', articles=articles)

@app.route('/article/<article_id>')
def article(article_id):
    article = {
        'title': 'The First Article',
        'content': 'This is the content of the first article.'
    }
    return render_template('article.html', article=article)

@app.route('/search')
def search():
    keyword = request.args.get('keyword')
    articles = [
        {
            'title': 'The First Article',
            'content': 'This is the content of the first article.'
        },
        {
            'title': 'The Second Article',
            'content': 'This is the content of the second article.'
        },
        {
            'title': 'The Third Article',
            'content': 'This is the content of the third article.'
        }
    ]
    return render_template('search.html', articles=articles, keyword=keyword)

if __name__ == '__main__':
    app.run()


html code for index.html

html
<!DOCTYPE html>
<html>
<head>
    <title>News App</title>
</head>
<body>
    <h1>News App</h1>
    <ul>
        {% for article in articles %}
            <li><a href="/article/{{ article.id }}">{{ article.title }}</a></li>
        {% endfor %}
    </ul>
</body>
</html>


html code for article.html

html
<!DOCTYPE html>
<html>
<head>
    <title>News App</title>
</head>
<body>
    <h1>{{ article.title }}</h1>
    <p>{{ article.content }}</p>
</body>
</html>


html code for search.html

html
<!DOCTYPE html>
<html>
<head>
    <title>News App</title>
</head>
<body>
    <h1>Search Results</h1>
    <ul>
        {% for article in articles %}
            <li><a href="/article/{{ article.id }}">{{ article.title }}</a></li>
        {% endfor %}
    </ul>
</body>
</html>
