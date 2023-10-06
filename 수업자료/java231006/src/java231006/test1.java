package java231006;

class Clock {
	private int hour;
	private int minute;
	private int second;
	
	
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


	public void Setting(int a, int b, int c) {
		this.hour = a;
		this.minute = b;
		this.second = c;
	}
}

class Watch extends Clock {
	private String StrapColor;

	
	public String getStrapColor() {
		return StrapColor;
	}

	public void setStrapColor(String strapColor) {
		StrapColor = strapColor;
	}

	public void Setting(int a, int b, int c) {
		setHour(a);
		setMinute(b);
		setSecond(c);
		this.StrapColor = "Black";
	}

	public void Setting(int a, int b, int c, String d) {
		this.Setting(a, b, c);
		this.StrapColor = d;
	}
}

class SmartWatch extends Watch {
	private String os;

	
	public String getOs() {
		return os;
	}

	public void setOs(String os) {
		this.os = os;
	}

	public void Setting(int a, int b, int c) {
		setHour(a);
		setMinute(b);
		setSecond(c);
		setStrapColor("Black");
		this.os = "null";
	}

	public void Setting(int a, int b, int c, String d) {
		this.Setting(a, b, c);
		setStrapColor(d);
		this.os = "null";
	}

	public void Setting(int a, int b, int c, String d, String e) {
		this.Setting(a, b, c, d);
		this.os = e;
	}
}

public class test1 {
	public static void main(String[] args) {
		Clock c = new Clock();
		Watch w = new Watch();
		SmartWatch sw = new SmartWatch();
		
		
	}
}