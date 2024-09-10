package LeaveApplication;

public class Leave {
    private int days;
    private int level;
    private ReasonType msg;

    public Leave(int days, int level, ReasonType msg) {
        this.days = days;
        this.level = level;
        this.msg = msg;
    }


    public int getDays() {
        return this.days;
    }

    public void setDays(int days) {
        this.days = days;
    }

    public int getLevel() {
        return this.level;
    }

    public void setLevel(int level) {
        this.level = level;
    }

    public ReasonType getMsg() {
        return this.msg;
    }

    public void setMsg(ReasonType msg) {
        this.msg = msg;
    }
    
}
