package textprocessingApplication;

public class FontAdd extends TextProcessor{
    private String font;
    public FontAdd(Text text, String font){
        super(text);
        this.font = font;
    }

    @Override
    public String addtext(){
        return this.font + super.addtext();
    }
}
