package Prototype;

public class Square extends Shape{
    public Square(int w, int h){
        super(w, h);
    }

    @Override
    public void draw(){
        System.out.println("Rectangle");
    }

    @Override
    public Shape clone(){
        return new Square(width,height);
    }
}
