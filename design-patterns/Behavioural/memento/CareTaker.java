package memento;

import java.util.ArrayList;
import java.util.List;

public class CareTaker {
    List<Memento> history = new ArrayList<>();
    public void addMemento(Memento memento){
        this.history.add(memento);
    }

    public Memento undo(){
        if(!history.isEmpty()){
            int lastIndex = history.size() - 1;
            Memento lastMemento = history.get(lastIndex);
            history.remove(lastIndex);
            return lastMemento;
        }
        return null;
    }
}
