package review230927;

import java.util.Scanner;

public class test2 {
	public static int getHour(int s) {
		return (s / 60) / 60;
	}

	public static int getMin(int s) {
		return (s / 60) % 60;
	}

	public static int getSec(int s) {
		return s % 60;
	}

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int sec;
		while (true) {
			sec = sc.nextInt();
			if (sec > 86400 || sec < 0) {
				System.out.println("잘못된 입력입니다.");
			} else {
				break;
			}
		}
		System.out.println(getHour(sec) + "시 " + getMin(sec) + "분 " + getSec(sec) + "초");
	}
}
