package textprocessingApplication;

public class ColorAdd extends TextProcessor{
    private String font;
    public ColorAdd(Text text, String font){
        super(text);
        this.font = font;
    }

    @Override
    public String addtext(){
        return this.font + super.addtext();
    }
}
