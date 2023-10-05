import java.util.Scanner;

//클래스 구현
//class 클래스명{
//	멤버선언
//	- 필드(멤버 변수)	: 특정 클래스에 있는 변수 
//	- 메소드(멤버 함수)	: 특정 클래스에 있는 함수
//	- 생성자
//	...
//}
class person {
	// 멤버 변수 선언부
	// 접근제어자 - 자료형 - 변수명;
	private String name;
	private int age;
	private String gender;
	
	//getter():값 반환 /setter():값 설정
	public String getName() {
		return name;
	}
	public void setName(String name) {
		this.name = name;
	}
	public int getAge() {
		return age;
	}
	public void setAge(int age) {
		this.age = age;
	}
	public String getGender() {
		return gender;
	}
	public void setGender(String gender) {
		this.gender = gender;
	}

	// 메소드 선언부
	// 접근제어자 - 반환형 - 함수명(매개변수){
	// 명령문
	// }
	public void Print() {
		System.out.println("이름 : " + this.name);
		System.out.println("나이 : " + this.age);
		System.out.println("성별 : " + this.gender);
	}

	// this 키워드 - "이 객체"
	// ㄴ> 멤버를 불러온 객체 자신을 가리키는 포인터 역할 수행

	// main에서 lee.Print(); -> lee객체를 가리킨다.

	// 접근제어자 > 멤버의 접근을 제어하는 문법
	// private > 외부에서 접근불가 / 소속 클래스 내에서만 접근가능
	// public > 어디서든 접근 가능
	// protected >

}

//컴파일러가 main함수를 찾을때 public class <파일명>을 가장 먼저 찾음
//<파일명>을 사용하는 public class는 하나만 존재해야함.
public class Class1 {
	public static void main(String[] args) {
		// 객체 : 육안으로 확인되는 사물/실체 > 클래스를 통해 만들어진 실체
		// ㄴ>같은 클래스를 통해 만들어진 인스턴스들을 포함하는 개념
		// 인스턴스 : 클래스를 통해 만들어진 것
		// ㄴ>각 인스턴스들은 같은 클래스를 통해 생성되었어도 각각 다르다.
		// 클래스 : 객체(인스턴스)를 찍어내는 틀
		Scanner sc = new Scanner(System.in);
		person lee = new person();
		lee.setName(sc.next());
		lee.setAge(sc.nextInt());
		lee.setGender(sc.next());
		
		lee.Print();
	}
}
