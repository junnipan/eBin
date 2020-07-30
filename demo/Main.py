import Analytics
import Motor
import Camera

print("Start")


def to_analyze(image_path):
    garbage_type = Analytics.analyze(image_path)
    dispose(garbage_type)
    

def dispose(garbage_type):
    print("Dispose: " + garbage_type)


to_analyze("data/ppp.jpeg")
