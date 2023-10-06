package java231006;

import java.util.Scanner;

class Americano {
	private int water;
	private int coffee;
	private String ice;

	public int getWater() {
		return water;
	}

	public void setWater(int water) {
		this.water = water;
	}

	public int getCoffee() {
		return coffee;
	}

	public void setCoffee(int coffee) {
		this.coffee = coffee;
	}

	public String getIce() {
		return ice;
	}

	public void setIce(String ice) {
		this.ice = ice;
	}

	public void GoodAme() {
		if (this.water == this.coffee * 2) {
			System.out.println("황금비율");
		} else if (this.water > this.coffee * 2) {
			System.out.println("연한 아메리카노");
		} else if (this.water < this.coffee * 2) {
			System.out.println("진한 아메리카노");
		}
	}

	public void Amount() {
		if (this.coffee + this.water > 750) {
			System.out.println("많다");
		} else if (this.coffee + this.water == 750) {
			System.out.println("적당하다");
		} else if (this.coffee + this.water < 750) {
			System.out.println("적다");
		}
	}

	public Americano() {
		this.water = 500;
		this.coffee = 250;
		this.ice = "있음";
		System.out.println("디폴트");
		GoodAme();
		Amount();
	}

	public Americano(int a, int b, String c) {
		this.water = a;
		this.coffee = b;
		this.ice = c;
		System.out.println("커스텀");
		GoodAme();
		Amount();
	}
}

public class review {
	public static void main(String[] args) {
		Scanner cin = new Scanner(System.in);
		// Americano ame[] = new Americano[2];
		Americano order = new Americano(cin.nextInt(), cin.nextInt(), cin.next());
		// for (int i = 0; i < 2; i++) {
		// ame[i] = new Americano();
		// }
	}
}
