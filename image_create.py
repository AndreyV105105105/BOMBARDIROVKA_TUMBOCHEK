import numpy as np
from PIL import Image, ImageDraw
from requests import get

img = Image.new('RGB', (256, 256), 'red')
img.save('main.jpg')
img = Image.open('main.jpg')

img2 = Image.new('RGB', (256, 256), 'red')
img2.save('modul.jpg')
img2 = Image.open('modul.jpg')


ans = []
while len(ans) < 16:
    response = get("https://olimp.miet.ru/ppo_it/api?status=jury")
    a = response.json()['message']['data']
    if a not in ans:
        ans.append(a)

response_coords = get("https://olimp.miet.ru/ppo_it/api/coords")
a = response_coords.json()['message']
sender = a['sender']
listener = a['listener']
price = a['price']

ans = np.array(ans)

ans = ans.reshape((4, 4, 64, 64))
with Image.open('main.jpg') as img:
    draw = ImageDraw.Draw(img)
    for u in range(4):
        for e in range(4):
            for i in range(len(ans[u][e])):
                for j in range(len(ans[u][e])):
                    draw.rectangle(((j + 64 * e, i + 64 * u), (j + 64 * e * 2, i + 64 * u * 2)), fill=(ans[u][e][i][j], ans[u][e][i][j], ans[u][e][i][j]), width=1)
    img.save('main.jpg')


with Image.open('main.jpg') as img:
    draw = ImageDraw.Draw(img)
    draw.ellipse(((sender[1] - 3, sender[0] - 3), (sender[1] + 3, sender[0] + 3)), fill='green', width=1)
    draw.ellipse(((listener[1] - 3, listener[0] - 3), (listener[1] + 3, listener[0] + 3)), fill='red', width=1)
    img.save('main.jpg')

img.show()
print(sender, listener)