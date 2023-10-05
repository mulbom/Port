
public class overloading {
	public static int sum() {
		return 1+1;
	}
	public static int sum(int a) {
		return a+1;
	}
	public static int sum(int a,int b) {
		return a+b;
	}
	public static void main(String[] args) {
		//오버로딩 : 함수에 적용되는 개념 / 매개변수 구성이 다를 경우 동일 명칭으로 사용해도 충돌하지 않는다.
		int a=1;
		int b=2;
		System.out.println(sum());
		System.out.println(sum(a));
		System.out.println(sum(a,b));
	}
}
