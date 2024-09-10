package design;
public class CommandExecutorImpl implements CommandExecutor {

	@Override
	public void runCommand(String cmd){
                //some heavy implementation
		System.out.println("'" + cmd + "' command executed.");
	}

}
