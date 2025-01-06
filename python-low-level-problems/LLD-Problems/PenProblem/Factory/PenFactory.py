# Factory/PenFactory.py
from Factory.PenType import PenType
from Factory.Pen import Pen
from Factory.Writer import Writer

class PenFactory:
    @staticmethod
    def create_pen(pen_type: PenType) -> Writer:
        if pen_type == PenType.PEN:
            return Pen()
        if pen_type == PenType.PENCIL:
            return Pencil()
        if pen_type == PenType.MARKER:
            return Marker()
        if pen_type == PenType.DIGITAL_PEN:
            return DigitalPen()
        return None
