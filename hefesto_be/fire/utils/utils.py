"""Django utils utilities"""
import time

# OpenCV
import cv2
# PIL
from PIL import Image


def get_int_timestamp():
    return str(int(time.time()))


def get_frame(path) -> tuple:
    """Get first frame from file or camera.
        * @params path, file path or camera url.
        * @returns (img, height, width) tuple."""
    frame = None
    height = None
    width = None
    img = None
    if path is None:
        return None, {'msg': 'Path is null.'}

    if path.isdigit():
        try:
            path = int(path)
        except ValueError as ve:
            print(ve)
            path = path

    vc = cv2.VideoCapture(path)
    start = time.time()
    while True:
        print(f'Connecting to {path} ...')
        ret, frame = vc.read()
        if ret:
            print(f'Conected')
            (height, width) = frame.shape[:2]
            # Image opencv to PIL.
            # https://stackoverrun.com/es/q/3660906
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            img = Image.fromarray(frame)
            break

        # Wait 1 minute to that VideoCapture response one frame
        # if not response (ret True), break cycle to close the
        # already opened file or camera with release function.
        current = time.time()
        if (current - start) > 90.0:
            break

    # Close the already opened file or camera.
    vc.release()
    size = {
        'height': height,
        'width': width
    }
    return img, size
