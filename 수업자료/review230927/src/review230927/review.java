package review230927;

import java.util.Scanner;

public class review {
	public static void main(String[] args) {
		// 출력문 3가지 : 3가지 (println, printf, print)
		Scanner scan = new Scanner(System.in);

		System.out.println("배아프다아아아아아아");
		System.out.printf("배가 아프다ㅏㅏㅏㅏㅏㅏ%d\n", 18);
		System.out.print("으엉어ㅏ어ㅏ아아ㅓ아어ㅏ어ㅏ어ㅏ\n");

		int i = scan.nextInt();
		double d = scan.nextDouble();
		float f = scan.nextFloat();
		long l = scan.nextLong();

		String s1 = scan.next();
		String s2 = scan.nextLine();
		char c = scan.next().charAt(0);
		
		// 아스키코드 : 컴퓨터가 문자를 이해할 수 있도록 특정 숫자와 문자를 일대일 대응 시킨 약속
		// 'A' = 65, 'a' = 97, '0' = 48
		
		// String 관련 함수
		// equals() : 문자열을 비교 -> 같으면 true 다르면 false
		// length() : 문자열의 길이 반환 ex) coffee = 6
		// charAt() : String형에 대해서, 특정 위치의 문자 접근할 때 사용 ex) coffee => coffee.charAt(1);
		// toCharArray() : String형 > char[]형 변환하는 함수
		
		// 배열 : 동일한 타입에 대해 여러 공간을 갖는 변수
		// 선언방법
		// 1. 초기화하면서 선언
		// (자료형) (배열명)[] = {값---};
		// int num[] = { 11,22,33,44,55};
		// String st[] = {"Hello","World"};
		// 2. 크기만 할당하며 선언
		// (자료형)(배열명)[] = new.(자료형)[배열크기];
		// int num[] = new.int[5];
		// String st[] = new.String[5];
	}
}
