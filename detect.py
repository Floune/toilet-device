import face_recognition
import cv2
import numpy
import os
import glob

face_locations = []
face_encodings = []
face_names = []
process_this_frame = True
faces_encodings = []
faces_names = []
path = os.path.join(os.getcwd(), 'data/faces/')
list_of_files = [f for f in glob.glob(path+'*.jpg')]
number_files = len(list_of_files)
names = list_of_files.copy()
  
def start():
	train()
	return detect()


def train():
	for i in range(number_files):
		globals()['image_{}'.format(i)] = face_recognition.load_image_file(list_of_files[i])
		globals()['image_encoding_{}'.format(i)] = face_recognition.face_encodings(globals()['image_{}'.format(i)])[0]
		faces_encodings.append(globals()['image_encoding_{}'.format(i)])
		names[i] = names[i].replace(os.getcwd(), "")  
		faces_names.append(names[i])


def detect():   
	video_capture = cv2.VideoCapture(0)
	while True:
		ret, frame = video_capture.read()
		small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)    
		rgb_small_frame = small_frame[:, :, ::-1]    

		face_locations = face_recognition.face_locations( rgb_small_frame)
		face_encodings = face_recognition.face_encodings( rgb_small_frame, face_locations)
		face_names = []

		for face_encoding in face_encodings:
			matches = face_recognition.compare_faces(faces_encodings, face_encoding)
			face_distances = face_recognition.face_distance( faces_encodings, face_encoding)
			best_match_index = numpy.argmin(face_distances)
			if matches[best_match_index]: #trouvé
				raw = faces_names[best_match_index]
				return os.path.basename(os.path.normpath(raw))[:-4] 
