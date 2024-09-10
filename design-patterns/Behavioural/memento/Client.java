package memento;

public class Client {
    public static void main(String[] args) {
        CareTaker careTaker = new CareTaker();
        Originator originator = new Originator(5, 10);

        Memento snapshot1 = originator.createMemento();
        careTaker.addMemento(snapshot1);

        Memento snapshot2 = originator.createMemento();
        careTaker.addMemento(snapshot2);
        snapshot2.setHeight(15);
        snapshot2.setWidth(16);

        Memento restored = careTaker.undo();
        originator.restoreMemento(restored);

        System.out.println("Height + " + originator.height + " width " + originator.width);
        System.out.println("Height + " + restored.height + " width " + restored.width);
    }
}
