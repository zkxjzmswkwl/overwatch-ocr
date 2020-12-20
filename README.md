# Overwatch Optical Character Recognition
Overwatch OCR is a bit annoying. You have to train Tesseract with the Koverwatch font, and even then it's really not that accurate... Unless you interpolate with OpenCv's `INTER_CUBIC` and blur with OpenCv's `medianBlur` with the intensity set to `3`. This is what I've been able to get the best results with so far.

# What's in the repo
The repo contains images I was testing with. They were all taken from the Odyssey vs. DarkMode NA loser's final gaunlet match from December 2020.

Furthermore, this repository contains the training data that I've made to train Tesseract to properly recognize the
Overwatch font. Put this in your `/tesseract/tessdata/` folder.

Make sure to install the `Koverwatch` font included in the `fonts` directory on your local machine. 

# Extra info
Generally, on `1920x1080`, the coordinates for each player on the spectator ui are as follows:
```
x1 = 40
x2 = x1 + 90

// loop over image
// cut image. e.g: img[y_start:y_end, x_start:x_end]
// Read string from image 

x1 = x1 + 106
x2 = x1 + 90
```
The delta between each player-block in the spectator UI is ~100. However I've found that `106` gives the best ocr
results.