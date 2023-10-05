import java.util.Scanner;

public class introduce {
	public static void main(String args[]) {
		Scanner scan = new Scanner(System.in);

		String name = scan.next();
		int age = scan.nextInt();
		char blood = scan.next().charAt(0);
		double h = scan.nextDouble();
		scan.nextLine();
		String introduce = scan.nextLine();

		System.out.println("이름 : " + name);
		System.out.println("나이 : " + age + "세");
		System.out.println("혈액형 : " + blood + "형");
		System.out.println("키 : " + h + "cm");
		System.out.println("자기소개 : " + introduce);

	}
}