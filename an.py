# Import packages
import datetime
from datetime import date
import matplotlib.pyplot as plt
import wikipedia
from wordcloud import WordCloud, STOPWORDS
import re
# Specify the title of the Wikipedia page
wiki = wikipedia.page('Web scraping')
# Extract the plain text content of the page
text = wiki.content
# Clean text
text = re.sub(r'==.*?==+', '', text)
text = text.replace('\n', '')
def plot_cloud(wordcloud):
    # Set figure size
    plt.figure(figsize=(40, 30))
    # Display image
    plt.imshow(wordcloud)
    # No axis details
    plt.axis("off");

    # Generate word cloud
wordcloud = WordCloud(width=3000, height=2000, random_state=1, background_color='black', margin=20, colormap='Pastel1',
                      collocations=False, stopwords=STOPWORDS).generate(text)
# Plot
plot_cloud(wordcloud)
wordcloud.to_file("wordcloud" + str(date.today())+".png")
