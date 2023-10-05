import java.util.Scanner;

public class Tutorial {
	public static void main(String args[]) {
		Scanner scan = new Scanner(System.in);
		/*
		 * int i = scan.nextInt(); long l = scan.nextLong(); double d =
		 * scan.nextDouble(); float f = scan.nextFloat();
		 * 
		 * String s1 = scan.next(); String s2 = scan.nextLine();
		 * 
		 * char c = scan.next().charAt(0);
		 * 
		 * System.out.println("afdf"); System.out.println("afdf");
		 * //System.out.print("asdf");
		 * 
		 * System.out.println(i); System.out.println(l); System.out.println(d);
		 * System.out.println(f); System.out.println(s1); System.out.println(s2);
		 */

		String name = scan.next();
		int age = scan.nextInt();
		char blood = scan.next().charAt(0);
		double h = scan.nextDouble();
		String produce = scan.next();

		System.out.println("이름 : " + name);
		System.out.println("나이 : " + age);
		System.out.println("혈액형 : " + blood);
		System.out.println("키 : " + h);
		System.out.println("자기소개 : " + produce);
	}
}
