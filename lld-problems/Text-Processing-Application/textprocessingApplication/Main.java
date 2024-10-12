package textprocessingApplication;

public class Main {
    public static void main(String[] args) {
        Text text = new PlainText("My name is Pratik");
        TextProcessor textProcessor = new FontAdd(new ColorAdd(text,"red"),"roman");

        System.out.println(textProcessor.addtext());
    }
}
