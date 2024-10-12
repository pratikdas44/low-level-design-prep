package textprocessingApplication;

public abstract class TextProcessor implements Text{
    protected Text text;
    public TextProcessor(Text text){
        this.text = text;
    }

    @Override
    public String addtext(){
        return text.addtext();
    }
}
