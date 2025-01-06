import PenTypes.PenFactory;
import PenTypes.PenType;
import PenTypes.Writer;
import WriteStrategy.Context;
import WriteStrategy.PencilStrategy;

public class Main {
    public static void main(String[] args) {
        Writer writer = PenFactory.createPen(PenType.MARKER);
        writer.write();

        Context context = new Context();
        context.setStrategy(new PencilStrategy());
        context.execute();
    }
}
