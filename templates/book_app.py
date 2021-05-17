from flask import Flask, render_template, request
import pandas as pd
import numpy as np
import pickle

app = Flask(__name__)

popular_list = pd.read_csv(r'popular_list.csv')

print(popular_list.iloc[0,0])
books_stats = [{'title': popular_list.iloc[i, 1],
		'isbn': popular_list.iloc[i, 2],
		'author': popular_list.iloc[i, 3],
		'img': popular_list.iloc[i, -2],
		'date_published':popular_list.iloc[i, 4]} for i in np.arange(3)]


@app.route('/')
@app.route('/home')
def home():
	#return (popular_list.iloc[0][0])
	return render_template('home.html', books_stats=books_stats)
	#return


# def display_popular_books():
# 	return

@app.route("/about")
def about():
    return render_template('about.html', title='About',books_stats=books_stats)

if __name__ == '__main__':
	app.run(debug=True)