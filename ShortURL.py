import requests as rq

def shorten_link(full_link, link_name):
    API_KEY = '177c065a69937ddac9e313cc73a89051198e5'
    BASE_URL = 'https://cutt.ly/api/api.php'

    payload = {'key': API_KEY, 'short': full_link, 'name': link_name}
    request = rq.get(BASE_URL, params=payload)
    data = request.json()

    print('')

    try:
        title = data['url']['title']
        short_link = data['url']['shortLink']

        print('Title', title)
        print('Link', short_link)
    except:
        status = data['url']['status']
        print('Error Status:', status)

link = input('Enter a link: >>')
name = input ('Give your link name: >>')

shorten_link(link, name)