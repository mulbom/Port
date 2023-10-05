import java.util.Scanner;

public class String_Fucn {
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		// equals() = 문자열 비교함수
		String s1 = scan.next();
		String s2 = "abc";
		System.out.println(s1.equals(s2));

		// length = 문자열 크기/길이 반환함수
		System.out.println("입력값의 길이 : " + s1.length());

		// charAt() = 매개변수 요소에 접근/반환 함수
		System.out.println("1번째 요소 : " + s1.charAt(0));
		System.out.println("2번째 요소 : " + s1.charAt(1));
		System.out.println("3번째 요소 : " + s1.charAt(2));

		// toCharArray() = str > char 변환(값은 그대로)
		char ch[] = s1.toCharArray();
		System.out.println("1번째 요소 : " + ch[0]);
		System.out.println("2번째 요소 : " + ch[1]);
		System.out.println("3번째 요소 : " + ch[2]);
	}
}
