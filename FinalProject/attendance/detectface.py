import cv2
import os


def detect(id,name):
	# initialize
	cap = cv2.VideoCapture(0)


	cv2.startWindowThread()

	# Create the haar cascade
	faceCascade = cv2.CascadeClassifier("attendance/haarcascade_frontalface_default.xml")

	# declare value to determine the time and number of pictures
	n = 1

	takePicture = True
	while takePicture:
		# Capture frame-by-frame
		ret, frame = cap.read()

		# convert the frame to gray color
		gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

		# Detect faces in the image
		faces = faceCascade.detectMultiScale(
			gray,
			scaleFactor=1.1,
			minNeighbors=5,
			minSize=(100, 100), flags=cv2.CASCADE_SCALE_IMAGE
		)

		font = cv2.FONT_HERSHEY_DUPLEX

		# check if face not found then put message text
		if(len(faces) == 0):
			cv2.putText(frame, "Please put your face in camera", (50,250), font, 1.0, (255,255,255), 1)
		# if face founded
		else:
			cv2.putText(frame, "Press p to take a picture", (50, 50), font, 1.0, (255, 255, 255), 1)
			# Draw a rectangle around the faces
			for (x, y, w, h) in faces:
				cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

			if cv2.waitKey(1) & 0xFF == ord('p'):
				# save the frame to image file
				newPath = 'attendance/static/attendance/dataset/'+ id + '-' + name
				if not os.path.exists(newPath):
					os.makedirs(newPath)

				ret, frame = cap.read()
				cv2.imwrite(newPath + '/' + str(n) + ".jpg", frame)

				cv2.putText(frame, "Picture saved", (50, 250), font, 1.0, (255, 255, 255), 1)

				takePicture = False

		#Display the resulting frame
		cv2.imshow('frame', frame)

		#waiting for the 'q' keys
		if cv2.waitKey(1) & 0xFF == ord('q'):
			break

	# When everything done, release the capture
	cap.release()
	cv2.destroyWindow('frame')
	cv2.destroyAllWindows()

	return "Success"
