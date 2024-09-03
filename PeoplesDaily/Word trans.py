import pandas as pd

# Load the CSV file to check its contents
file_path = '/text/translated_PDS1.csv'
data = pd.read_csv(file_path)
data.head()

from wordcloud import WordCloud
import matplotlib.pyplot as plt


# Generate a word cloud image
word_freq = dict(zip(data['english_word'], data['freq']))
font_path = '/System/Library/Fonts/STHeiti Light.ttc'
wordcloud = WordCloud(font_path=font_path, width=800, height=400, background_color='white').generate_from_frequencies(word_freq)


# Display the generated image
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.savefig('/image/wordPDS1_e2.png') 
plt.show()
