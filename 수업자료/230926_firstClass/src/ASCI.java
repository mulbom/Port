import java.util.Scanner;

public class ASCI {
	public static void main(String[] args) {
		// 아스키코드
		char c = 37;
		System.out.println(c);

		Scanner scan = new Scanner(System.in);

		char ASKI = scan.next().charAt(0);
		System.out.println((int) ASKI);
	}
}
