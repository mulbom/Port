import java.util.Scanner;

public class Clock {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        System.out.print("초를 입력하세요 : ");
        int s = scan.nextInt();

        conClock(s);
    }

    public static void conClock(int s) {
        //3600이상의 값을 받으면 오류 메시지를 출력한다.
        if (s >= 3600) {
            System.out.println("Error : 3600 미만의 값을 입력해주세요.");
        } else {
            int h = s / 3600;
            int m = (s % 3600) / 60;
            int ss = s % 60;

            System.out.println(h + "시간" + m + "분" + ss + "초");
        }
    }
}
