import java.util.Scanner;

public class test {
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);

		String tes1 = scan.nextLine();
		System.out.println(tes1);

		char te[] = tes1.toCharArray();
		int alpha[] = new int[26];
		for (int size = tes1.length() - 1; size >= 0; size--) {
			for (int i = 97; i <= 122; i++) {
				if (te[size] == i) {
					alpha[i - 97] += 1;
				}
			}
			for (int j = 65; j <= 90; j++) {
				if (te[size] == j) {
					alpha[j - 65] += 1;
				}
			}
		}
		for (int i = 0, j = 65; i < 26; i++, j++) {
			if (alpha[i] != 0) {
				System.out.println((char) (j) + "의 갯수 : " + alpha[i]);
			}
		}
	}
}