package Rating;

import java.util.ArrayList;
import java.util.List;

public class ReviewCollection implements ReviewComponent{
    private List<ReviewComponent> reviews = new ArrayList<>();

    @Override
    public void add(ReviewComponent reviewComponent){
        reviews.add(reviewComponent);
    }

    @Override
    public void remove(ReviewComponent reviewComponent){
        reviews.remove(reviewComponent);
    }

    @Override
    public void display(){
        for(ReviewComponent reviewComponent : reviews){
            reviewComponent.display();
        }
    }
}
