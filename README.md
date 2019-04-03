# captcha_break
Captcha breaker for very old government website in order to automate the data entry task

This Repo consists of the captcha generator for creation of labelled dataset, we tried to create captchas that were similar to the one available on the website.
Website had captchas with strikethrough text of variable length available in red using Times font.

Challenge was to identify:-
1. captchas text of strikethrough, so just using Pytesseract was not possible
2. captchas of variable length 5-9 and thus most of the repos/datasets available on github could not be used.

With the issues at hand the recogition task based on contours/ text boxes for different characters was not possible as the strikethrough meant that separate boxes for different chars was not possible.
Use of opencv seemed to be the  best way ahead, with opencv we trained on the generated captchas and it looked good as we removed the lines and tried to extend the same on our real captcha dataset but due to different morphological operations now tesseract was not able to identify these images and that transition was no longer smooth.

we did not wanted to use DL here as it was not needed/required and use of opencv seemed more sensible. So we used simple python code and since we knew our captchas really well, this is the steps that we followed:-
1. We removed the line through simple Python script, we generated the images without the line for our real captcha dataset.
2. We converted the image in greyscale(preprocess) for better OCR results via tesseract.
    gray1 = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray2 = cv2.threshold(gray1, 0, 255,
        cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
        
3. We used these preprocessed images to get output from the tesseract OCR
     text.append(pytesseract.image_to_string(gray1))
     #print(text)
     text.append(pytesseract.image_to_string(gray2))
     #print(text)
     
The cumulative results from these two almost gave all the outputs, but only issue seems to be associated with e as after line removal e is converted similar to c. But even with this we are getting good enough results.

Going ahead we will be adding more approach to this dataset, that will include 
CNN+CTC based approach.
Contour based approach which will start from the processed images that we feed to tesseract.

Code shared here are the captcha generator Google Colab notebook.
Colab notebook again for giving the captcha results for our scenario as well.
Also sharing the captchas that we have crawled from the target website. We have provided the labeled dataset of 500 captchas that were the most painful part of the process.
For experimentation you can always generate any number of captchas from the captcha generator colab notebook that we have shared.


