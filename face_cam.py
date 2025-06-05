import cv2
import mediapipe as mp
import datetime

mp_pose = mp.solutions.pose
mp_drawing = mp.solutions.drawing_utils

cap = cv2.VideoCapture("afogamento1.mp4")

def detect_risk_pose(landmarks):
    nose = landmarks[mp_pose.PoseLandmark.NOSE.value]
    left_eye = landmarks[mp_pose.PoseLandmark.LEFT_EYE.value]
    right_eye = landmarks[mp_pose.PoseLandmark.RIGHT_EYE.value]
    left_shoulder = landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value]
    right_shoulder = landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value]
    left_hip = landmarks[mp_pose.PoseLandmark.LEFT_HIP.value]
    right_hip = landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value]
    left_knee = landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value]
    left_wrist = landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value]
    right_wrist = landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value]

    # Simulação: altura da água está no nível do joelho
    agua_nivel = left_knee.y

    # Altura média dos ombros e quadris
    quadril_medio_y = (left_hip.y + right_hip.y) / 2

    # 2. Postura de risco (nariz abaixo do quadril)
    if nose.y > quadril_medio_y:
        return "risco_postura"

    # 3. Pessoa submersa com quadril abaixo e água baixa
    elif agua_nivel < 0.5 and quadril_medio_y > 0.7:
        return "submerso"

    # 4. Braços erguidos (pedindo ajuda)
    elif (left_wrist.y < left_shoulder.y) and (right_wrist.y < right_shoulder.y):
        return "pedido_ajuda"

    return None


with mp_pose.Pose() as pose:
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
            continue

        #frame = cv2.resize(frame, (500, 500))
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = pose.process(image)
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        if results.pose_landmarks:
            landmarks = results.pose_landmarks.landmark
            mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)

            estado = detect_risk_pose(landmarks)
            if estado:
                cv2.putText(image, f"Alerta: {estado}", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

                ts = datetime.datetime.now().strftime("%Y%m%d_%H%M%S_%f")
                cv2.imwrite(f"alerta_{ts}.jpg", image)

        cv2.imshow("FloodPose", image)
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()
