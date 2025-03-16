from requests import get

def otsort(s1="https://olimp.miet.ru/ppo_it/api", s2="https://olimp.miet.ru/ppo_it/api/coords"):
    ans = []
    while len(ans) < 16:
        response = get(s1)
        a = response.json()['message']['data']
        if a not in ans:
            ans.append(a)
    response_coords = get(s2)
    a = response_coords.json()['message']
    sender = a['sender']
    listener = a['listener']
    price = a['price']
    sl = {'u': [], 'd': [], 'l': [], 'r': [], 'n': [], 'lua': [], 'rua': [], 'lda': [], 'rda': []}
    for i in range(len(ans)):
        if ans[i][0] == [255] * 64:
            fr = 1
            fl = 1
            for j in range(len(ans[i])):
                if ans[i][j][0] != 255:
                    fl = 0
                if ans[i][j][-1] != 255:
                    fr = 0
            if fr == 1 and fl == 0:
                sl['rua'].append(ans[i])
            elif fr == 0 and fl == 1:
                sl['lua'].append(ans[i])
            elif fr == 0 and fl == 0:
                sl['u'].append(ans[i])
        elif ans[i][-1] == [255] * 64:
            fr = 1
            fl = 1
            for j in range(len(ans[i])):
                if ans[i][j][0] != 255:
                    fl = 0
                if ans[i][j][-1] != 255:
                    fr = 0
            if fr == 1 and fl == 0:
                sl['rda'].append(ans[i])
            elif fr == 0 and fl == 1:
                sl['lda'].append(ans[i])
            else:
                sl['d'].append(ans[i])
        else:
            fr = 1
            fl = 1
            for j in range(len(ans[i])):
                if ans[i][j][0] != 255:
                    fl = 0
                if ans[i][j][-1] != 255:
                    fr = 0
            if fr == 1 and fl == 0:
                sl['r'].append(ans[i])
            elif fr == 0 and fl == 1:
                sl['l'].append(ans[i])
            else:
                sl['n'].append(ans[i])
    return sl
sl = otsort()
ans1 = 0
mxr = 255
e1 = sl['l'][0]
e2 = sl['l'][1]
while mxr > 0:
    for i in range(64):
        if abs(sl['lua'][0][-1][i] - e1[0][i]) > mxr:
            ans1 = mxr + 1
            mxr = -1
            break
    mxr -= 1
mxr = 255
while mxr > 0:
    for i in range(64):
        if abs(sl['lua'][0][-1][i] - e2[0][i]) > mxr:
            ans2 = mxr + 1
            mxr = -1
            break
    mxr -= 1
ans = min(ans1, ans2)
answer1 = []
answer2 = []
answer3 = []
answer4 = []
for e in sl:
    if e == 'u':
        itu = []
        f = 1
        for i in range(64):
            if abs(sl['lua'][0][i][-1] - sl[e][0][i][0]) > mxr:
                itu.append(sl[e][0])
                itu.append(sl[e][1])
                f = 0
                break
        if f:
            itu.append(sl[e][1])
            itu.append(sl[e][0])
        answer1.append([sl['lua'][0], *itu, sl['rua'][0]])
    if e == 'd':
        itu = []
        f = 1
        for i in range(64):
            if abs(sl['lda'][0][i][-1] - sl[e][0][i][0]) > mxr:
                itu.append(sl[e][0])
                itu.append(sl[e][1])
                f = 0
                break
        if f:
            itu.append(sl[e][1])
            itu.append(sl[e][0])
        answer4.append([sl['lda'][0], *itu, sl['rda'][0]])
    if e == 'l':
        itu1 = []
        itu2 = []
        f = 1
        for i in range(64):
            if abs(sl['lua'][0][-1][i] - sl[e][0][0][i]) > mxr:
                itu1.append(sl[e][0])
                itu2.append(sl[e][1])
                f = 0
                break
        if f:
            itu1.append(sl[e][1])
            itu2.append(sl[e][0])
        answer2.append([*itu1, [sl['n'][2]], [sl['n'][3]], *itu2])
    if e == 'r':
        itu1 = []
        itu2 = []
        f = 1
        for i in range(64):
            if abs(sl['rua'][0][-1][i] - sl[e][0][0][i]) > mxr:
                itu1.append(sl[e][0])
                itu2.append(sl[e][1])
                f = 0
                break
        if f:
            itu1.append(sl[e][1])
            itu2.append(sl[e][0])
        answer3.append([*itu1, [sl['n'][0]], [sl['n'][1]], *itu2])

for e in answer3[0]:
    print(e)
    print()