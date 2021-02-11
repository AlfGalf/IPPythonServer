import cv2 as cv

'''
img=cv.imread('snake.jpeg')

cv.imshow('Snake',img)
'''
def videoRecording():
    capture=cv.VideoCapture(0)
    counter=0
    frames=[]
    while True:
        counter=counter+1
        isTrue, frame=capture.read()
        print(counter)
        #cv.imshow('Video',frame)
        print(frame.shape)
        #if cv.waitKey(20) & 0xFF==ord('d'):
        frames.append(frame)
        if cv.waitKey(20) & counter>2:
            break
        
    return frames

def showFrames(frames):
    for i in frames:
        cv.imshow('Img',i)
        cv.waitKey(0)
    #capture.release()
    cv.destroyAllWindows()

#Example
newRecording=videoRecording()
showFrames(newRecording)
