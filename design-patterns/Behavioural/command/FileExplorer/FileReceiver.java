package command.FileExplorer;

public class FileReceiver implements FileSystemReceiver {
    @Override
    public void openFile(){
        System.out.println("File opened");
    }

    @Override
    public void closeFile(){
        System.out.println("File closed");
    }
    
}
