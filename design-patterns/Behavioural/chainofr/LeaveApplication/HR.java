package LeaveApplication;

public class HR extends LeaveHandler{
    @Override
    public String applyLeave(Leave leave){
        if(leave.getDays() <= 21){
            if(leave.getLevel() <= 3 && leave.getMsg().equals(ReasonType.REGULAR)){
                return "Leave Approved by APPROVED by HR";
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