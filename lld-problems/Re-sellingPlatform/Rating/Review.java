package Rating;

public class Review implements ReviewComponent{
    private String text;
    private int rating;

    public Review(String text, int rating){
        this.text = text;
        this.rating = rating;
    }

    @Override
    public void add(ReviewComponent reviewComponent){

    }

    @Override
    public void remove(ReviewComponent reviewComponent){

    }

    @Override
    public void display(){
        System.out.println("Rating: " + rating + " Review " + text);
    }
}
