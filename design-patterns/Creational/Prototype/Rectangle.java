package Prototype;

public class Rectangle extends Shape{
    public Rectangle(int w, int h){
        super(w, h);
    }

    @Override
    public void draw(){
        System.out.println("Rectangle");
    }

    @Override
    public Shape clone(){
        return new Rectangle(width,height);
    }
}
