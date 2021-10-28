import os
import random
import sys

import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from pytwitterscraper import TwitterScraper
from wordcloud import WordCloud

twit_txt_array = []


def plot_cloud(wordcloud):
    # Set figure size
    plt.figure(figsize=(500, 600))
    # Display image
    plt.imshow(wordcloud)
    # No axis details
    # plt.axis('off')


def generate_wc(text_str, mask, username, image_path):
    top_text = 'Created for @' + username
    bottom_text = 'Created by @pgolod'
    wordcloud = WordCloud(width=5000, height=4000, random_state=2, background_color='#1DA1F2', margin=3,
                          colormap='Pastel2',
                          collocations=False, mask=mask, max_words=250).generate(text_str)
    plot_cloud(wordcloud)
    path = 'wordcloud_' + username + '_' + str(random.randint(0, 999)) + '.png'
    wordcloud.to_file(path)
    img = Image.open(path)
    draw = ImageDraw.Draw(img)
    draw1 = ImageDraw.Draw(img)
    font = ImageFont.truetype('data/ComicHelvetic_Light.otf', 12)
    # draw.text((x, y),'Sample Text',(r,g,b))
    #draw.text((306 - len(top_text) * 6, 0), top_text, (255, 255, 255), font=font)
    draw1.text((306 - len(top_text) * 4, 590), top_text, (255, 255, 255), font=font)
    img.save(image_path)
    rm_file(path)


def twit_data(username):

    tw = TwitterScraper()
    profile = tw.get_profile(name=username)
    user_id = profile.__dict__.get('id')
    tweets = tw.get_tweets(user_id, count=random.randint(300, 850)).__dict__
    return tweets


def twt_to_string(twt_data):
    twt_str = ''
    for twt_item in twt_data.get('contents'):
        twt_text = twt_item.get('text')
        twt_text = twt_text.split(' ')
        for items in twt_text:
            if 'RT' not in items \
                    and 'http' not in items and \
                    '@' not in items \
                    and len(items) > 1 \
                    and 'на' not in items \
                    and 'не' not in items:
                twt_str += items.replace(',', '') \
                               .replace('.', '') \
                               .replace('️', '') + ', '

    return twt_str


def rr(username=''):
    print(username)

    image_path = 'images/result_' + str(username) + '_' + str(random.randint(0, 999)) + '.png'
    print(image_path)
    mask = np.array(Image.open('data/twitter-logo.jpg'))
    twt_data = twit_data(username)

    twt_to_str = twt_to_string(twt_data)

    generate_wc(twt_to_str, mask, username, image_path)

    # os.remove(path=image_path)
    return image_path


def rm_file(image_path):
    path = os.path.dirname(sys.modules['__main__'].__file__)
    print(path + '\\' + image_path.replace('/', '\\'))
    os.remove(image_path)
