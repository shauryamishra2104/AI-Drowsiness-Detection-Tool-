import numpy as np

MOUTH_INDICES = [78, 308, 13, 14]

class calculation:
    def calculate_ear(eye_points):
        a = np.linalg.norm(eye_points[1] - eye_points[5])
        b = np.linalg.norm(eye_points[2] - eye_points[4])
        c = np.linalg.norm(eye_points[0] - eye_points[3])
        return (a + b) / (2.0 * c)
    
    def calculate_mar(mouth_points):
        vertical_dist = np.linalg.norm(mouth_points[13] - mouth_points[14])
        horizontal_dist = np.linalg.norm(mouth_points[78] - mouth_points[308])
        return vertical_dist / (horizontal_dist + 1e-6)


    
