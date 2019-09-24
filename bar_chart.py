"""
Output a list of the words from multiple cells in a CSV, in order of the most
frequent. Prints them to a bar chart using the Bokeh library.

"""

import sys
import collections
import requests
import pandas
import nltk
from nltk.corpus import stopwords
import string

# from nltk.tokenize import word_tokenize - This looks to be a significantly
# easier implementation of tokenizing words vs the string punctuation solution.

# nltk.download('stopwords')
# nltk.download('punkt')

with open('/content/sample_data/media_data2.csv', newline = '', encoding = 'mac_roman') as csvfile:
    dataFrame = pandas.read_csv(csvfile)

# #Have a look at the data.
# print(dataFrame.Outlet)
# print()
# print(dataFrame.Title)
# print()
# print(f"type(dataFrame.Body) = {type(dataFrame.Body)}")
# print(f"len(dataFrame.Body) = {len(dataFrame.Body)}")
# print()

punctuation = string.punctuation + "\u201C\u201D"   #double quotes “ ”
paragraphs = dataFrame.body
strippedWords = [word.strip(punctuation) for word in " ".join(paragraphs).split()]
lowerWords = [word.lower() for word in strippedWords if word]

# Clean list to make sure stop words are not counted
stop_words = set(stopwords.words('english'))   #"i", "me", "my", "myself", "we", etc.
cleanListOfWords = [word for word in lowerWords if word not in stop_words]

#Counter is like a dict.  Keys are words, values are counts.
counter = collections.Counter(cleanListOfWords)
listOfTuples = counter.most_common()

# for word, i in listOfTuples[:10]:
#     print(f"{i:2} {word}")

high_freq_words = [word[0] for word in listOfTuples[:10]]
freq = [int[1] for int in listOfTuples[:10] ]
# for word, i in listOfTuples[:10]: # take top 10 values and put them into plotting lists
#     word = high_freq_words.append(word)
#     i = freq.append(i)


from bokeh.io import show, output_notebook
from bokeh.plotting import figure

output_notebook()
print(freq)
# Set the x_range to the list of categories above
p = figure(x_range=high_freq_words, plot_height=250, title="Most Popular Words in Dataset")

# Categorical values can also be used as coordinates
p.vbar(x=high_freq_words, top=freq, width=0.9)

# Set some properties to make the plot look better
p.xgrid.grid_line_color = None
p.y_range.start = 0

show(p)
