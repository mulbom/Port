import java.util.Scanner;

public class test1 {
	public static int getDaily(int mo, int da) {
		int dDay = 365;
		for (int i = 1; i < mo; i++) {
			if (i == 2) {
				dDay -= 28;
			} else if (i == 4 || i == 6 || i == 9 || i == 11) {
				dDay -= 30;
			} else {
				dDay -= 31;
			}
		}
		dDay -= da;
		return dDay;
	}

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		System.out.println("월 입력 : ");
		int mo = sc.nextInt();
		System.out.println("일 입력 : ");
		int da = sc.nextInt();
		System.out.println("연말까지 "+getDaily(mo, da) + "일 남았습니다.");
	}
}
