package java231005;

import java.util.Scanner;

class Account {
	private String acc_num;
	private String id;
	private String pw;

	public String getAcc_num() {
		return acc_num;
	}

	public void setAcc_num(String acc_num) {
		this.acc_num = acc_num;
	}

	public String getId() {
		return id;
	}

	public void setId(String id) {
		this.id = id;
	}

	public String getPw() {
		return pw;
	}

	public void setPw(String pw) {
		this.pw = pw;
	}

	public void Print() {
		System.out.println(this.acc_num);
		System.out.println(this.id);
		System.out.println(this.pw);
	}

	public void changePw() {
		Scanner cin = new Scanner(System.in);
		while (true) {
			this.changePw(cin.next());
			if (this.getPw().length() < 5) {
				System.out.println("비밀번호는 5자리 이상이어야 합니다.");
			} else {
				break;
			}
		}
	}

	public void changePw(String p) {
		this.pw = p;

	}

	public Account() {
		this.acc_num = "0000";
		this.id = "ex";
		this.pw = "0000";
	}

	public void Print(String n, String i, String p) {
		this.acc_num = n;
		this.id = i;
		this.pw = p;
		System.out.println("회원번호 : " + this.acc_num);
		System.out.println("Id : " + this.id);
		System.out.println("Pw : " + this.pw);

	}

	public Account(String n, String i, String p) {
		this.acc_num = n;
		this.id = i;
		this.pw = p;
	}
}

public class test1 {
	public static void main(String[] args) {
		Scanner cin = new Scanner(System.in);
		Account manager[] = new Account[3];
		for (int i = 0; i < 3; i++) {
			manager[i] = new Account();
		}
		for (int i = 0; i < 3; i++) {
			System.out.println(i + 1 + "." + "관리자 정보 입력");
			String id = cin.next();
			String pw = cin.next();
			manager[i].Print(manager[i].getAcc_num(), id, pw);
			System.out.println();
		}
		System.out.println("유저 정보 입력");
		Account user = new Account(cin.next(), cin.next(), cin.next());
		user.Print();

		System.out.println("변경할 패스워드 입력");
		user.changePw();
		user.Print();
		
	}
}
