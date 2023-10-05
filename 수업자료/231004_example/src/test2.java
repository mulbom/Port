import java.util.*;

class Clock {
	private int hour = 0;
	private int minute = 0;
	private int second = 0;

	public int getHour() {
		return hour;
	}

	public void setHour(int hour) {
		this.hour = hour;
	}

	public int getMinute() {
		return minute;
	}

	public void setMinute(int minute) {
		this.minute = minute;
	}

	public int getSecond() {
		return second;
	}

	public void setSecond(int second) {
		this.second = second;
	}

	public String AmPm(int hour) {
		String m = null;
		if (hour >= 12 && hour < 24) {
			m = "Pm";
		} else {
			m = "Am";
		}
		return m;
	}

	public void PrintTime() {
		System.out.println(AmPm(hour) + " " + this.hour + "시 " + this.minute + "분 " + this.second + "초 ");
	}

}

public class test2 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		Clock c1 = new Clock();
		Clock c2 = new Clock();
		while (true) {
			c2.setHour(sc.nextInt());
			if (c2.getHour() >= 0 && c2.getHour() < 24) {
				break;
			}
		}
		while (true) {
			c2.setMinute(sc.nextInt());
			if (c2.getMinute() >= 0 && c2.getMinute() < 60) {
				break;
			}
		}
		while (true) {
			c2.setSecond(sc.nextInt());
			if (c2.getSecond() >= 0 && c2.getSecond() < 60) {
				break;
			}
		}
		c1.PrintTime();
		c2.PrintTime();
	}
}
