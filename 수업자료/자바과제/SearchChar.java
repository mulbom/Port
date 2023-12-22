import java.util.Scanner;

public class SearchChar {
    public static void main(String[] args) {
        /*
        입력값으로는, n과 n개의 단어, 그리고 검색하고자 하는 단어 하나(search)가 주어진다.
        n개의 단어 중에서, 찾고자 하는 단어가 있다면 검색이 성공했음을 알리도록 한다.
        다만, 찾고자 하는 단어가 없다면 검색이 실패했음을 알리도록 한다.
        이때, 구현하는 함수의 반환형은 boolean으로 설정하고
        입력 및 출력 모두 main 안에서 수행하도록 한다.*/
        //검색대상 단어가 몇개인지 입력받는다 n
        //단어를 n번 입력한다
        //n개의 단어에서 찾을 단어를 입력
        //판별
        //문제 이해가 이게 맞나 모르겠네요...
        Scanner scan = new Scanner(System.in);

        System.out.print("검색 대상 단어는 몇개인가요 : ");
        int n = scan.nextInt();

        String[] chars = new String[n];
        System.out.println("단어를 입력하세요 : ");
        for (int i = 0; i < n; i++) {
            chars[i] = scan.next();
        }

        System.out.print("검색할 단어를 입력하세요: ");
        String searchw = scan.next();

        boolean isFound = search(chars, searchw);

        if (isFound) {
            System.out.println("성공");
        } else {
            System.out.println("실패");
        }
    }

    public static boolean search(String[] c, String sw) {
        for (String word : c) {
            if (word.equals(sw)) {
                return true;
            }
        }
        return false;
    }
}
