import cv2
import pytesseract
from pytesseract import Output

# Keeping everything in one file so it's easy to consume, as this is an example not something I'm pushing to production.

img = cv2.imread('images/1920by1080.png')

def parse_team(team):
    x1 = x2 = None
    team_result = []

    if team.lower() == 'blue':
        x1 = 40
        x2 = x1 + 90
    elif team.lower() == 'red':
        x1 = 1250
        x2 = x1 + 90

    for i in range(6):
        team_result.append(img[112:130, x1:x2])
        x1 = x1 + 106
        x2 = x1 + 90
    return team_result

players = parse_team('blue')

for player in players:
    player = cv2.resize(player, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)
    player = cv2.cvtColor(player, cv2.COLOR_BGR2RGB)
    player = cv2.medianBlur(player, 3)
    player_str = pytesseract.image_to_string(player, lang='eng')
    cv2.imshow(player_str, player)
    cv2.waitKey(0)

