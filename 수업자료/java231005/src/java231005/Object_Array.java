package java231005;

import java.util.Scanner;

class Student {
	private String name;
	private String num;
	private int age;

	public String getName() {
		return name;
	}

	public void setName(String name) {
		this.name = name;
	}

	public String getNum() {
		return num;
	}

	public void setNum(String num) {
		this.num = num;
	}

	public int getAge() {
		return age;
	}

	public void setAge(int age) {
		this.age = age;
	}
	
	public void Print(String n, String nu, int a) {
		this.name=n;
		this.num=nu;
		this.age=a;
		System.out.println("이름 : "+this.name);
		System.out.println("학번 : "+this.num);
		System.out.println("나이 : "+this.age);
	}
}

public class Object_Array {
	public static void main(String[] args) {
		Scanner cin = new Scanner(System.in);
		// 객체 배열
		// 배열 선언(크기 지정/할당) -> 객체 선언(공간을 자세히 나눔)

		// 배열 선언
		// (자료형)(배열명)[] = new(자료형)[크기] -> 자료형 == 클래스명(사용 가능)
		// ex) int arr[] = new int[10];
		// 객체 선언
		// [클래스명][인스턴스명]=new [클래스명]();
		Student s[] = new Student[3];
		for (int i = 0; i < 3; i++) {
			s[i] = new Student();
		}
		for(int i=0;i<3;i++) {
			String n=cin.next();
			String num=cin.next();
			int a=cin.nextInt();
			
			s[i].Print(n, num, a);
		}
	}
}
