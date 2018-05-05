import cv2
import numpy as np
from keras.models import model_from_json
import base64
import face.CNN_MODEL as cnn



def predict_emotion(face_image_gray,sess):
	resized_img = cv2.resize(face_image_gray, (48,48), interpolation = cv2.INTER_AREA)
	pixel = np.zeros((48,48))
	for i in range(48):
		for j in range(48):
			pixel[i][j] = resized_img[i][j]
	list = cnn.Predict(pixel,sess)
	
	return list[0]

def get_emotion(str,faceCascade,sess):
	data =base64.b64decode(str)
	dataStr =  np.fromstring(data, np.uint8)
	frame = cv2.imdecode(dataStr,cv2.IMREAD_COLOR)
	img_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	faces = faceCascade.detectMultiScale(
		img_gray,
		scaleFactor=1.1,
		minNeighbors=5,
		minSize=(30, 30),
		flags= cv2.CASCADE_SCALE_IMAGE
	)
	ret = []
	for (x, y, w, h) in faces:
		face_image_gray = img_gray[y:y+h, x:x+w]
		cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
		list= predict_emotion(face_image_gray,sess)
		# list = ["angry","disgust","fear","happy","sad","surprise","neutral"]
		ret += [(int)(list[3]+list[5]-list[0]-list[1]-list[2]-list[4])]
	return ret