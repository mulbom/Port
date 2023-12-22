import java.util.Scanner;

public class multiplicationTables {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        System.out.print("원하는 단을 입력하세요 : ");
        int n = scan.nextInt();

        int[] dan = new int[9];

        for (int i = 0; i < 9; i++) {
            dan[i] = n * (i + 1);
        }

        for (int i = 0; i < 9; i++) {
            System.out.println(n + " x " + (i + 1) + " = " + dan[i]);
        }
    }
}
