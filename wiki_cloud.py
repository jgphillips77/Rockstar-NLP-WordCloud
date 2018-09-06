import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

import wikipedia
import sys
import os
from os import path
from PIL import Image
from wordcloud import WordCloud, STOPWORDS

# Make path to script's directory
currdir = path.dirname(__file__) if "__file__" in locals() else os.getcwd()

def get_wiki(query):
	# get best matching title for given query
	title = wikipedia.search(query)[0]

	# get wikipedia page for selected title
	page = wikipedia.page(title)
	return page.content


def create_wordcloud(text):
	# create numpy array for wordcloud mask image
	mask = np.array(Image.open(path.join(currdir, "cloud.png")))

	# create set of stopwords	
	stopwords = set(STOPWORDS)

	# create wordcloud object
	wc = WordCloud(background_color="black",
					max_words=200, 
					mask=mask,
	               	stopwords=stopwords, max_font_size=40)
	
	# generate wordcloud
	wc.generate(text)

	# Save wordcloud as wc.png, Do not need to save right now.
	#wc.to_file(path.join(currdir, "wc.png"))
    
	plt.figure(figsize=(13,13))
	plt.imshow(wc, interpolation='bilinear')
	plt.axis("off")