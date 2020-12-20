import cv2
import pytesseract
import numpy as np
from pytesseract import Output

# Keeping everything in one file so it's easy to consume, as this is an example not something I'm pushing to production.

HEROES = [
    'Tracer', 'Ashe', 'Wrecking Ball',
    'Sigma', 'Mercy', 'Zenyatta',
    'Baptiste', 'Echo', 'Brigitte'
]

def match_image(img, sub):
    sub_img = cv2.imread(f'images/heroes/{sub}.png')

    # Preprocess both player spectator widget and hero template
    sub_img = preprocess(sub_img)
    img = preprocess(img)

    w, h = sub_img.shape[:-1]

    res = cv2.matchTemplate(img, sub_img, cv2.TM_CCOEFF_NORMED)
    threshold = .69
    loc = np.where(res >= threshold)

    for pt in zip(*loc[::-1]):
        cv2.rectangle(img, pt, (pt[0] + 5 + w, pt[1] + h), (255, 255, 0), 2)
        return True

def get_hero(img):
    for hero in HEROES:
        i = match_image(img, hero)
        if i:
            return hero

def preprocess(to_process):
    to_process = cv2.resize(to_process, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)
    to_process = cv2.cvtColor(to_process, cv2.COLOR_BGR2RGB)
    to_process = cv2.medianBlur(to_process, 3)
    return to_process

def parse_team(img, team, find_hero=False):
    x1 = x2 = None
    team_result = {}

    if team.lower() == 'blue':
        x1 = 50
        x2 = x1 + 90
    elif team.lower() == 'red':
        x1 = 1250
        x2 = x1 + 90

    for i in range(6):
        ready_img = preprocess(img[112:130, x1:x2])
        result = pytesseract.image_to_string(ready_img, lang='eng').rstrip()

        if find_hero:
            team_result[f'{team}_{str(i)}'] = {'player_name': result, 'hero': get_hero(img[70:106, x1:x2])}
        else:
            team_result[f'{team}_{str(i)}'] = {'player_name': result}

        x1 = x1 + 106
        x2 = x1 + 90
    return team_result


base_img = cv2.imread('images/bh_vs_at.png')
blue = parse_team(base_img, 'blue', find_hero=True)
red = parse_team(base_img, 'red', find_hero=True)

print('\nOn the blue team we have..')
print('****************************\n')
for i in blue.values():
    print(f'{i.get("player_name")} playing {i.get("hero")}.')

print('\nAnd on the red team we have..')
print('****************************\n')
for i in red.values():
    print(f'{i.get("player_name")} playing {i.get("hero")}.')

