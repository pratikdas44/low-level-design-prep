package LeaveApplication;

public class ProjectLeader extends LeaveHandler{
    @Override
    public String applyLeave(Leave leave){
        if(leave.getDays() <= 14){
            if(leave.getLevel() <= 3){
                return "Leave Approved by ProjectLeader";
            }
            else{
                return "Request my manager";
            }
        }
        else{
            return leaveHandler.applyLeave(leave);
        }
    }
}