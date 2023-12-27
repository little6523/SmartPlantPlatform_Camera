#remove.bg 배경제거 api

import requests

def rm_bg(file_name, i) :
    response = requests.post(
        'https://api.remove.bg/v1.0/removebg',
        files={'image_file': open(file_name, 'rb')},
        data={'size': 'auto'},
        headers={'X-Api-Key': 'GJ6Jc5idYdUWJL2eWvJKBeoW'},
    )

    file_name = 'rem_test' + str(i) + '.png'
    print("file_name = ", file_name)

    if response.status_code == requests.codes.ok:
        with open(file_name, 'wb') as out:
            out.write(response.content)
    else:
        print("Error:", response.status_code, response.text)