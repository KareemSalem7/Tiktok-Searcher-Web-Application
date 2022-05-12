from TikTokApi import TikTokApi
import pywebio
from pywebio.input import input
from pywebio.output import put_text, put_buttons
import webbrowser


def btn_click(btn_val):
    webbrowser.open(btn_val)


def app():
    api = TikTokApi(proxy="http://52.60.169.78:3128")
    num_videos = 100
    links = []

    username = input('Enter your username: ')
    user = api.user(username)
    search_keyword = input('Enter search keyword: ')
    liked_videos = user.liked(num_videos)

    for tiktok in liked_videos:
        search_values = [tiktok['desc'], tiktok['author']['uniqueId'], tiktok['author']['nickname'],
                         tiktok['music']['title'], tiktok['music']['authorName']]
        search_values = [string.lower() for string in search_values]

        for search_value in search_values:
            if search_keyword in search_value:
                url = 'https://www.tiktok.com/@' + tiktok['author']['uniqueId'] + '/video/' + tiktok['id']
                links.append(url)
                break

    put_text(f'Tiktok videos liked by {username}, relating to {search_keyword}:')
    count = 1
    for url in links:
        slice_one = url[23:]
        index_end = slice_one.index("/")
        slice_two = slice_one[:index_end]
        put_text(f"{count}. Creator: {slice_two}")
        put_buttons([url], onclick=btn_click)
        count += 1


if __name__ == '__main__':
    pywebio.start_server(app, port=80)
