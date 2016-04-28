import cv2

# Initializing VideoCapture
capture = cv2.VideoCapture(0)

while(True):
	# Capture framey by frame
	retval, frame = capture.read()
	
	# Operations on per frame
	# gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	
	# Display on the resulting frame
	cv2.imshow('frame',frame)
	
	# Break
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break
    
# Release the capture
capture.release()
cv2.destroyAllWindow()		
	