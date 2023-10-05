import java.util.Scanner;

public class review {
	public static int getHour(int s) {
		return (s / 60) / 60;
	}

	public static int getMin(int s) {
		return (s / 60) % 60;
	}
	
	public static void print(int h) {
		if(h>=0&&h<=6) {
			System.out.println("취침중");
		}
		else if(h>6&&h<9) {
			System.out.println("출근하셔야죠...");
		}
		else if(h>=9&&h<=18) {
			System.out.println("근무중");
		}
		else {
			System.out.println("칼퇴!!!");
		}
	}
	public static void main(String[] args) {
		//하루 시간(시, 분)을 입력받고, 현재 진행중인 일과를 출력하기
		//오전 9시 이전 > 출근하셔야죠... 출력
		// 9~18시 > 근무중
		// 18시 이후 >칼퇴!!! 출력
		// 0시 ~ 6시 > 취침중
		Scanner sc = new Scanner(System.in);
		int s = sc.nextInt();
		int h = getHour(s);
		int m = getMin(s);
		System.out.println(h+"시 "+m+"분");
		print(h);
		
	}

}
