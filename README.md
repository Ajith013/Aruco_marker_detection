# Aruco_marker_detection
Detection of Aruco markers on live camera feed

Includes code for capturing calibration images,camera calibration, generation of Aruco marker and aruco marker identification on live camera feed

Things to remember : <br />
1. Aruco marker size is defined in pixels during generation(Eg: 300 ). It should be scaled during distance measurment (pixel to cm) <br />
2. The checkerboard square size is multiplied to object points in the calibration point ( Eg: 28.83)
3. Checkerboard pattern can be created using [this](https://docs.opencv.org/4.x/da/d0d/tutorial_camera_calibration_pattern.html)


