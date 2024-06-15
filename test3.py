
import cv2

import numpy as np

import mediapipe as mp
import pandas as pd


    
def create_mask(image):
    mp_face_mesh = mp.solutions.face_mesh
    face_mesh = mp_face_mesh.FaceMesh(static_image_mode=True, max_num_faces=10)

    results = face_mesh.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    if not results.multi_face_landmarks:
        raise Exception("No face landmarks detected")

    mask = np.zeros((image.shape[0], image.shape[1]), dtype=np.uint8)
    face_oval = mp_face_mesh.FACEMESH_FACE_OVAL
    df = pd.DataFrame(list(face_oval), columns=["p1", "p2"])

    for landmarks in results.multi_face_landmarks:
        routes_idx = []

        p1 = df.iloc[0]["p1"]
        p2 = df.iloc[0]["p2"]

        for i in range(df.shape[0]):
            obj = df[df["p1"] == p2]
            p1 = obj["p1"].values[0]
            p2 = obj["p2"].values[0]

            route_idx = [p1, p2]
            routes_idx.append(route_idx)

        routes = []

        for source_idx, target_idx in routes_idx:
            source = landmarks.landmark[source_idx]
            target = landmarks.landmark[target_idx]

            relative_source = (int(image.shape[1] * source.x), int(image.shape[0] * source.y))
            relative_target = (int(image.shape[1] * target.x), int(image.shape[0] * target.y))

            routes.append(relative_source)
            routes.append(relative_target)

        cv2.fillPoly(mask, [np.array(routes)], 255)

    return mask  # Inverting the mask

image = cv2.imread("happy_family.png")
mask = create_mask(image)
cv2.imwrite("masddddk.png", mask)
