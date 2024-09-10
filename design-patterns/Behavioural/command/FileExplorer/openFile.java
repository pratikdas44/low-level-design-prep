package command.FileExplorer;

import java.io.FileReader;

public class openFile implements Command{
    private FileReceiver fileReceiver;
    public openFile(FileReceiver fileReceiver){
        this.fileReceiver = fileReceiver;
    }
    
    @Override
    public void execute(){
        this.fileReceiver.openFile();
    }
}
