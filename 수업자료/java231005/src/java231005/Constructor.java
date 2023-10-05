package java231005;

class Teacher {
	private String name;
	private String num;
	private int age;

	public void Print() {
		System.out.println("이름 : " + this.name);
		System.out.println("사원번호 : " + this.num);
		System.out.println("나이 : " + this.age);
	}

	// 생성자 >> 객체를 생성하는 메소드 ( 메소드 중 일부 )
	// 생성자도 오버로딩 가능
	// 생성자 형태
	// public 클래스명(매개변수구성,...) {
	// 객체 생성시 수행할 명령문
	// }
	public Teacher() {
		this.name = "null";
		this.num = "null";
		this.age = 0;
	}

	// public Teacher() {
	// 기본 생성자 >> 매개변수X, 수행할 명령문X
	// ㄴ> 사용자가 별도로 생성자를 만들지 않았을 때
	// ㄴ> default로 호출}
}

public class Constructor {
	public static void main(String[] args) {
		// 클래스명-객체명 = new 생성자 호출();
		Teacher t = new Teacher();
		t.Print();
	}
}
