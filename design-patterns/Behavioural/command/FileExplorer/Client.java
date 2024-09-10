package command.FileExplorer;

public class Client {
    public static void main(String[] args) {
        FileReceiver fileReceiver = new FileReceiver();
        FileInvoker fileInvoker = new FileInvoker();
        Command openFileCommand = new openFile(fileReceiver);
        fileInvoker.setCommand(openFileCommand);
        fileInvoker.clickFile();
    }
}
