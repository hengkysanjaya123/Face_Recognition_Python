# import sys
import face_recognition
import cv2
import os
import datetime

def writeData(data):
    data = data.split('-')

    f = open('temporarydata.txt', 'a')
    now = datetime.datetime.now()
    f.write("\n"+str(data[0]) +"#" + data[1] + "#" + str(now.date())+ "#" + str(now.strftime("%H:%M:%S")))
    f.close()


def main():
    video_capture = cv2.VideoCapture(0)
    # Create arrays of known face encodings and their names
    dictKnownFace = {}

    listKnownFace = []
    listNameKnownFace = []

    listOfFiles = os.listdir("static\\attendance\\dataset")
    for l in listOfFiles:
        listImage = os.listdir("static\\attendance\\dataset\\" + str(l))

        dictKnownFace.setdefault(l,[])
        listNameKnownFace.append(l)

        for j in listImage:
            person_image = face_recognition.load_image_file("static\\attendance\\dataset\\" + str(l) + "\\"+j)
            face_locations = face_recognition.face_locations(person_image)
            person_face_encoding = face_recognition.face_encodings(person_image, face_locations)[0]

            dictKnownFace[l].append(person_face_encoding)
            listKnownFace.append(person_face_encoding)

    # Initialize some variables
    process_this_frame = True


    while True:
        # Grab a single frame of video
        ret, frame = video_capture.read()

        # Resize frame of video to 1/4 size for faster face recognition processing
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

        # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
        rgb_small_frame = small_frame[:, :, ::-1]


        # Only process every other frame of video to save time
        if process_this_frame:
            # Find all the faces and face encodings in the current frame of video
            face_locations = face_recognition.face_locations(rgb_small_frame)
            face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

            face_names = []
            for face_encoding in face_encodings:
                # See if the face is a match for the known face(s)
                matches = face_recognition.compare_faces(listKnownFace, face_encoding, tolerance=0.50)

                name = "Unknown"

                print(matches)

                # If a match was found in known_face_encodings, just use the first one.
                if True in matches:
                    first_match_index = matches.index(True)

                    name = listNameKnownFace[first_match_index]
                    writeData(name)

                    print(name)
                    face_names.append(name)
                    break

        process_this_frame = not process_this_frame


        # Hit 'q' on the keyboard to quit!
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release handle to the webcam
    video_capture.release()
    cv2.destroyAllWindows()

main()


# From : https://github.com/ageitgey/face_recognition