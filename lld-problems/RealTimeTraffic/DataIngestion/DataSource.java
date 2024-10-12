package DataIngestion;

import java.util.ArrayList;
import java.util.List;

public class DataSource {
    private List<Obserer> obsererList = new ArrayList<>();
    public void add(Obserer obserer){
        this.obsererList.add(obserer);
    }

    public void remove(Obserer obserer){
        this.obsererList.remove(obserer);
    }

    public void notifyAll(String data){
        for(Obserer obserer1:obsererList){
            obserer1.update(data);
        }
    }
}
