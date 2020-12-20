import cv2
import pytesseract
from pytesseract import Output

img = cv2.imread('images/1920by1080.png')

players = {'red': [], 'blue': []}

x1 = 40
x2 = x1 + 90

for i in range(6):
    players.get('blue').append(img[112:130, x1:x2])
    x1 = x1 + 106
    x2 = x1 + 90

for player in players.get('blue'):
    player = cv2.resize(player, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)
    player = cv2.medianBlur(player, 3)
    player_str = pytesseract.image_to_string(player, lang='eng')
    cv2.imshow(player_str, player)
    cv2.waitKey(0)

