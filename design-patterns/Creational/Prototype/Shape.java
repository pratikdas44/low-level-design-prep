package Prototype;

public abstract class Shape {
    protected int width;
    protected int height;

    public Shape(int width, int height){
        this.height = height;
        this.width = width;
    }

    public abstract void draw();
    public abstract Shape clone();
}
