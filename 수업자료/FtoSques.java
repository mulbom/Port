import java.util.Scanner;

//5번
class Coffee {
    private int espresso;

    public Coffee(int e) {//생성자
        this.espresso = e;
    }

    public int getEspresso() {
        return espresso;
    }

    public void setEspresso(int espresso) {
        this.espresso = espresso;
    }
}

class Americano extends Coffee {
    private int water;

    public Americano(int e, int w) {
        super(e);
        this.water = w;
    }

    public void printAme() {
        System.out.println("에스프레소 : " + getEspresso() + " ml");
        System.out.println("물 : " + water + " ml");
    }

    public void goodAme() {
        // 1:2
        if (getEspresso() * 2 == water) {
            System.out.println("황금 비율 아메리카노입니다.");
        } else if (getEspresso() > water) {
            System.out.println("어딘가 밸런스가 안 맞는 아메리카노입니다.(쓴)");
        } else {
            System.out.println("어딘가 밸런스가 안 맞는 아메리카노입니다.(연한)");
        }
    }
}

class Moka extends Coffee {
    private int milk;
    private int choco;

    public Moka(int e, int m, int c) {
        super(e);
        this.milk = m;
        this.choco = c;
    }

    public void printMoka() {
        System.out.println("에스프레소 : " + getEspresso() + " ml");
        System.out.println("우유 : " + milk + " ml");
        System.out.println("초콜릿 : " + choco + " ml");
    }

    public void goodMoka() {
        // 2:2:1 에스프레소 초코 우유
        if (getEspresso() == choco && getEspresso() / 2 == milk) {
            System.out.println("황금 비율 카페모카입니다.");
        } else {
            System.out.println("어딘가 밸런스가 안 맞는 카페모카입니다.");
        }
    }
}

public class FtoSques {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        System.out.println("아메리카노를 주문하세요(샷 물) : ");
        Americano ame = new Americano(scan.nextInt(), scan.nextInt());
        System.out.println("주문한 아메리카노");
        ame.printAme();
        ame.goodAme();

        System.out.println("카페모카를 주문하세요(샷 우유 초콜릿) : ");
        Moka moka = new Moka(scan.nextInt(), scan.nextInt(), scan.nextInt());
        System.out.println("주문한 카페모카");
        moka.printMoka();
        moka.goodMoka();
    }
}