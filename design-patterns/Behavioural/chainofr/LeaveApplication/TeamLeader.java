package LeaveApplication;

public class TeamLeader extends LeaveHandler{
    @Override
    public String applyLeave(Leave leave){
        if(leave.getDays() <= 7){
            if(leave.getLevel() <= 4){
                return "Leave Approved by TeamLeader";
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
