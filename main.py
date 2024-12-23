import cv2
import face_recognition


def recognize_faces(image_path):
    
    image = face_recognition.load_image_file(image_path)

    
    face_locations = face_recognition.face_locations(image)


    image_cv2 = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

    
    for (top, right, bottom, left) in face_locations:
        cv2.rectangle(image_cv2, (left, top), (right, bottom), (0, 255, 0), 2)

    
    cv2.imshow("Yüz Tanıma", image_cv2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


recognize_faces("resim.jpg")  
