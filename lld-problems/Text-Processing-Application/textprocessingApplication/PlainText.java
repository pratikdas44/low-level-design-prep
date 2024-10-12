package textprocessingApplication;

public class PlainText implements Text{
    private String text;

    public PlainText(String text){
        this.text = text;
    }

    @Override
    public String addtext(){
        return this.text;
    }
}
