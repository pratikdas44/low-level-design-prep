package command.FileExplorer;

public class FileInvoker {
    private Command command;

    public void setCommand(Command command){
        this.command = command;
    }

    public void clickFile(){
        this.command.execute();
    }
}
