package review230927;

import java.util.Scanner;

public class test {
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		int n = scan.nextInt();
		System.out.println("짝수 & 합");
		int hap = 0;

		for (int i = 1; i <= n; i++) {
			if (i % 2 == 0) {
				System.out.println(i);
				hap += i;
			}
		}
		System.out.println(hap);
		System.out.println("소수");
		int j;
		for (int i = 2; i <= n; i++) {
			// int count=0;
			for (j = 2; j < i; j++) {
				if (i % j == 0) {// j가 i의 약수일때,
					//count++;
					break; //이 위치로 들어오게 되면 소수가 아니게 된다.
				}
			}
			//count가 0을 유지하지 못한다면, 소수가 아니다.
			//count가 0을 유지하면, 소수라고 할 수 있다.
			//if(count==0){
			// 이 위치로 오게되면 소수이므로 출력하면 된다.
			//System.out.println(i);
			//}
			if (i == j) { 
				System.out.println(i); 
			}
		}
	}
}
