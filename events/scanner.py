import cv2
from numpy.core.fromnumeric import resize
import pytesseract as oc
import numpy as np
from time import sleep


class Vision:

    def open_video(self, vod_path):
        vod = cv2.VideoCapture(vod_path)
        fps = int(vod.get(cv2.CAP_PROP_FPS))
        
        if vod.isOpened() == False:
            print(f'{vod_path} does not exist. Try again fucko.')
        
        while vod.isOpened():
            ret, frame = vod.read()

            if ret == True:
                frame = cv2.resize(frame, None, fx=2.5, fy=2.5, interpolation=cv2.INTER_CUBIC)
                print(f'Chex currently has {self.check_blinks(frame)} blinks.')
                # sleep(1/fps) 

                cv2.imshow('Anton', frame)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
            else:
                break

    def _preprocess(snapshot, dilate=True, erode=True, otsu=True):
        kernel = np.ones((1, 1), np.uint8)

        snapshot = cv2.resize(snapshot, None, fx=2.6, fy=2.6, interpolation=cv2.INTER_CUBIC) 
        snapshot = cv2.cvtColor(snapshot, cv2.COLOR_BGR2GRAY)
        snapshot = cv2.dilate(snapshot, kernel, iterations=1)
        snapshot = cv2.erode(snapshot, kernel, iterations=1)
        if otsu:
            snapshot = cv2.threshold(cv2.medianBlur(
                snapshot, 3), 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
        return snapshot
    
    @staticmethod
    def _save(snapshot):
        pass

    @staticmethod
    def _rotate(img, x, y, offset=15):
        M = cv2.getRotationMatrix2D((y, x), offset, 1)
        return cv2.warpAffine(img, M, (img.shape[1], img.shape[0]))
    
    @staticmethod
    def _resize_blur(img, resize_fl, blur):
        img = cv2.resize(img, None, fx=resize_fl, fy=resize_fl, interpolation=cv2.INTER_CUBIC)
        img = cv2.GaussianBlur(img, (5, blur), 0)
        return img

    def check_blinks(self, frame):
        frame = Vision._preprocess(frame)

        blink_indicator = frame[893:913, 1608:1632]
        # blink_indicator = cv2.resize(blink_indicator, None, fx=6.6, fy=6.6, interpolation=cv2.INTER_CUBIC)
        blink_indicator = cv2.GaussianBlur(blink_indicator, (5, 25), 0)


        rotated_indicator = Vision._rotate(blink_indicator, 50, 20, offset=10)
        cv2.imshow('rota', rotated_indicator)
        cv2.waitKey(0)
        txt = oc.image_to_string(rotated_indicator, config='--psm 13')
        print(txt, len(txt))

        if '3' in txt:
           return 3
        if '2' in txt:
            return 2
        if '1' in txt:
            return 1
        if '0' in txt:
            return 0
        
        # second pass
        # Tesseract reliably recognizes preprocessed Koverwatch 0's to be I.
        # Potential TODO to focus in on numeric training? But for this purpose, it's fine.
        blink_indicator = Vision._resize_blur(frame[875:920, 1602:1640], 5.6, 25)
        rotated_indicator = Vision._rotate(blink_indicator, 50, 50, offset=15)

        txt = oc.image_to_string(rotated_indicator, lang="eng", config='--psm 10')

        if 'I' in txt:
            return 0

        


chex = Vision()
chex.open_video('C:\\Users\\Carter\\Videos\\chex-1080p.mp4')
        