#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import cv2 as cv2

#charger le classificateur en cascade pré-entrainés

face_cascade = cv.CascadeClassifier('haarcascade_frontface_default.xml')

#charger les images
img = cv.imread('talibe.jpeg')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

#execution de la détection de visage
face = face_cascade.detectMultiScale(gray, 1.1, 8)

#affichage des visages
i = 0
for face in faces:
    x, y, w, h = face
    
    # dessiner le rectangle sur l'image principale
    cv.rectangle(img, (x,y), (x + w, y + h), (0, 255, 0), 2)

    # extraire les visages sur l'image principale
    # OpenCV & Numpy: y <-> row et x <-> col
    face = img[y:y+h, x:x+w]

    # afficher face0, face1, face2, etc...
    cv.imshow('face{}'.format(i), face)
    i += 1
cv.imshow('image principale', img)
cv.waitKey(0)
cv.destroyAllWindows()