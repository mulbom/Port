package java231006;

class Phone {
	public String tel;
	public Boolean foldable;
}

class smartPhone extends Phone {
	public String os;
	public String network;// (4G or 5G)
}

public class Extends {
	public static void main(String[] args) {
		// 상속 >> "부모로부터 자식이 상속받는다"
		// >> 부모, 자식 >> 상하관계 구성
		Phone p = new Phone();
		smartPhone sp = new smartPhone();
		
		p.tel="010-0000-0000";
		p.foldable=true;
		sp.tel="010-1111-1111";
		sp.foldable=false;
		sp.os="Android 10";
		sp.network="5G";
		System.out.println(p.tel);
		System.out.println(sp.tel);
	}
}
