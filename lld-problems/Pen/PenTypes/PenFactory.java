package PenTypes;

public class PenFactory {
    public static Writer createPen(PenType penType){
        if(penType == PenType.PEN){
            return new Pen();
        }
        if (penType == PenType.PENCIL) {
            return new Pencil();
        }
        if (penType == PenType.MARKER) {
            return new Marker();
        }
        if (penType == PenType.DIGITAL_PEN) {
            return new DigitalPen();
        }
        return null;
    }
}
