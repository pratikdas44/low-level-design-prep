package CommunicationLayer;

public class ExternalDataConverter {
    private String internalData;

    public ExternalDataConverter(String internalData){
        this.internalData = internalData;
    }

    public String convertToExternalFormat(){
        return "External format of " + internalData;
    }
}
