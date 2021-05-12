import sys
import numpy as np
import pandas as pd

datafile = 'clean_v1.csv'
data = pd.DataFrame(pd.read_csv(datafile), columns=['tweet', 'category', 'class'])

def num_of_cursewords(row):
    '''
    Computes the amount of curse words in a string
    Takes a string as input
    Returns an integer
    '''
    cursewords = { # predefined set of curse words
        "ass",
        "shit",
        "fuck",
        "bitch",
        "cunt",
        "nigga",
        "nigger",
        "damn",
        "hell",
        "kike",
        "piss",
        "dick",
        "asshole",
        "shithead",
        "motherfucker",
        "kike",
        "pussy",
        "cock",
        "tit",
        "tits",
        "bullshit",
        "shitfaced",
        "cocksucker",
        "douchebag",
        "dickhead",
        "dumbass",
        "fuckface",
        "shithead",
        "dipshit",
        "asshat",
        "fag",
        "faggot"
    }
    count = 0
    for w in row.split():
        if w in cursewords:
            count += 1
    return count

# This section counts the number of hate speech observations, offensive language observations, and neither observations in the dataset
hate_speech_tot = 0
offensive_tot = 0
neither_tot = 0
for _, row in data.iterrows():
    if row['category'] == 'neither':
        neither_tot += 1
    elif row['category'] == 'hate_speech':
        hate_speech_tot += 1
    elif row['category'] == 'offensive_lang':
        offensive_tot += 1
totals = pd.DataFrame([['hate_speech',hate_speech_tot],['offensive_lang', offensive_tot],['neither',neither_tot]], columns=['category', 'count'])
totals['count'] = totals['count'].astype(float)
# Create bar plot for showing amount of data in each class
totals.plot.bar(x="category", y="count", ylabel="Amount of data points", rot=0, title="Data distribution of labels")

# this section find the max number of curse words in any observation, and creates a dataframe for category,class,curse word word count
cursewords_list = list()
max_curses = 0
for i, row in data.iterrows():
    count = num_of_cursewords(row['tweet'])
    if count > max_curses:
        max_curses = count
    cursewords_list.append([row['category'], int(row['class']), count])
cursewords_df = pd.DataFrame(cursewords_list, columns=['category', 'class', 'cursecount'])

# This section counts the number of hate speech observations, offensive language observations, and neither observations in the dataset for each curse word count from 0 to the max amount of curse words in the observations
d = dict()
for i in range(max_curses + 1):
    hate_speech_tot = 0
    offensive_tot = 0
    neither_tot = 0
    for _, row in cursewords_df.iterrows():
        if row['category'] == 'neither' and row['cursecount'] == i:
            neither_tot += 1
        elif row['category'] == 'hate_speech' and row['cursecount'] == i:
            hate_speech_tot += 1
        elif row['category'] == 'offensive_lang' and row['cursecount'] == i:
            offensive_tot += 1
    d[i] = (hate_speech_tot, offensive_tot, neither_tot)

df = pd.DataFrame(d)
# plot the amount of curse words by category
df.plot.bar(stacked=True, rot=0, xlabel="category", ylabel="Amount of curse words", title="Amount of curse words by category")
df = df.T
df.columns=["neither", "offensive language", "hate speech"]
# plot the category by the amount of cursewords
df.plot.bar(stacked=True, rot=0, xlabel="amount of curse words", ylabel="Amount of data points", title="Category by the amount of cursewords")

plt.show()
