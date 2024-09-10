package LeaveApplication;

public abstract class LeaveHandler {
    protected LeaveHandler leaveHandler;

    public void setnextHandler(LeaveHandler leaveHandler){
        this.leaveHandler = leaveHandler;
    }

    public abstract String applyLeave(Leave leave);
}
