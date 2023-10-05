package java231005;

import java.util.Scanner;

class Phone {
	private String os;
	private int year;
	private String color;
	
	public String getOs() {
		return os;
	}
	public void setOs(String os) {
		this.os = os;
	}
	public int getYear() {
		return year;
	}
	public void setYear(int year) {
		this.year = year;
	}
	public String getColor() {
		return color;
	}
	public void setColor(String color) {
		this.color = color;
	}
	
	public void Print() {
		System.out.println("운영체제 : "+this.os);
		System.out.println("출시년도 : "+this.year+"년");
		System.out.println("색상 : "+this.color);
	}
	public void Print(String os, int year, String color) {
		this.os=os;
		this.year=year;
		this.color=color;
		System.out.println("운영체제 : "+this.os);
		System.out.println("출시년도 : "+this.year+"년");
		System.out.println("색상 : "+this.color);
	}
}

public class review {
	public static void main(String[] args) {
		// 객체 >> 클래스를 통해 만들어진 실체
		// 인스턴스 >> 클래스를 통해 만들어진 것
		// ▶▶ 객체가 인스턴스들을 포함하는 개념
		// 클래스 >> 객체를 찍어내는 틀
		Scanner cin = new Scanner(System.in);
		Phone p= new Phone();
		
		p.setOs("Android");
		p.setYear(2021);
		p.setColor("Black");
		
		System.out.println("Os : "+p.getOs());
		System.out.println("Year : "+p.getYear());
		System.out.println("Color : "+p.getColor());
		p.Print();
		p.Print(cin.next(), cin.nextInt(), cin.next());
	}
}
