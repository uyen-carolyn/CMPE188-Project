import sys
import numpy as np
import pandas as pd
#from textualheatmap import TextualHeatmap
#import seaborn as sns
import matplotlib.pyplot as plt

datafile = 'clean_v1.csv'
data = pd.DataFrame(pd.read_csv(datafile), columns=['tweet', 'category', 'class'])

def num_of_cursewords(row):
    cursewords = {
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
totals.plot.bar(x="category", y="count", ylabel="Amount of data points", rot=0, title="Data distribution of labels")

cursewords_list = list()
max_curses = 0
for i, row in data.iterrows():
    count = num_of_cursewords(row['tweet'])
    if count > max_curses:
        max_curses = count
    cursewords_list.append([row['category'], int(row['class']), count])
cursewords_df = pd.DataFrame(cursewords_list, columns=['category', 'class', 'cursecount'])

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
df.plot.bar(stacked=True, rot=0, xlabel="category", ylabel="Amount of curse words", title="Amount of curse words by category")
df = df.T
df.columns=["neither", "offensive language", "hate speech"]
df.plot.bar(stacked=True, rot=0, xlabel="amount of curse words", ylabel="Amount of data points", title="Category by the amount of cursewords")

plt.show()
