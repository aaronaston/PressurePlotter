# Read barometer data, print to the screen
from objc_util import ObjCInstance, ObjCClass, ObjCBlock, c_void_p
from datetime import datetime

logfile = open("homelog", "a")

def handler(_cmd, _data, _error):
		obj = ObjCInstance(_data)
		print(obj)
		logfile.write(str(datetime.now())+'\t'+str(obj)+'\n')

handler_block = ObjCBlock(handler, restype=None, argtypes=[c_void_p, c_void_p, c_void_p])

def main():
    CMAltimeter = ObjCClass('CMAltimeter')
    NSOperationQueue = ObjCClass('NSOperationQueue')
    if not CMAltimeter.isRelativeAltitudeAvailable():
        print('This device has no barometer.')
        return
    altimeter = CMAltimeter.new()
    main_q = NSOperationQueue.mainQueue()
    altimeter.startRelativeAltitudeUpdatesToQueue_withHandler_(main_q, handler_block)
    print('Started altitude updates.')
    
    try:
        while True:
            pass
    finally:
        altimeter.stopRelativeAltitudeUpdates()
        print('Updates stopped.')
        logfile.close()

if __name__ == '__main__':
    main()

