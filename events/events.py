import enum
import cv2
import pytesseract as ocr


class EventType(enum.Enum):
    KILL = 1
    ASSIST = 2
    DEATH = 3


class Severity(enum.Enum):
    YELLOW = 1
    ORANGE = 2
    RED = 3
    DEFCON_FUCKZONE = 4


class Event:

    def __init__(self, **kwargs):
        self._type = kwargs.pop('event_type', None)
        self._log = kwargs.pop('log', None)
        self._severity = kwargs.pop('severity', None)
