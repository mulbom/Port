package review230927;

import java.util.Scanner;

public class Func {
	public static int plu(int a, int b) {
		return a + b;
	}

	public static int sub(int a, int b) {
		return a - b;
	}

	public static int mul(int a, int b) {
		return a * b;
	}

	public static double div(int a, int b) {
		return (double)a / b;
		// int / int = int
		// double / int = double
		// int / double = double
		// double / double = double
	}

	public static int rem(int a, int b) {
		return a % b;
	}

	public static void main(String[] args) {
		// 함수 : 특정 목적을 위해 묶어둔"명령문들의 집합"

		// 예제 : 계산기 구현 (+,-,*,/,%)
		Scanner scan = new Scanner(System.in);

		int n1 = scan.nextInt();
		int n2 = scan.nextInt();
		char oper = scan.next().charAt(0);

		switch (oper) {
		case '+': {
			System.out.println("덧셈결과 : " + plu(n1, n2));
			break;
		}
		case '-': {
			System.out.println("뺄셈결과 : " + sub(n1, n2));
			break;
		}
		case '*': {
			System.out.println("곱셈결과 : " + mul(n1, n2));
			break;
		}
		case '/': {
			System.out.println("나눗셈결과 : " + div(n1, n2));
			break;
		}
		case '%': {
			System.out.println("나머지셈결과 : " + rem(n1, n2));
			break;
		}
		default: {
			System.out.println("잘못된 입력입니다.");
		}
		}
	}
}
