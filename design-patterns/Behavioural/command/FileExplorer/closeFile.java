package command.FileExplorer;

public class closeFile implements Command{
    private FileReceiver fileReceiver;
    public closeFile(FileReceiver fileReceiver){
        this.fileReceiver = fileReceiver;
    }
    
    @Override
    public void execute(){
        this.fileReceiver.closeFile();
    }
}
