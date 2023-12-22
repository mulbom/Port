abstract class shape {
    abstract void whatShape();
}
class Circle extends shape {
    @Override
    void whatShape() {
        System.out.println("원");
    }
}

class Triangle extends shape {
    @Override
    void whatShape() {
        System.out.println("삼각형");
    }
}

class Rectangle extends shape {
    @Override
    void whatShape() {
        System.out.println("사각형");
    }
}

public class EtoNques {
    public static void main(String[] args) {
        Circle c = new Circle();
        c.whatShape();
        Triangle t = new Triangle();
        t.whatShape();
        Rectangle r = new Rectangle();
        r.whatShape();
    }
}
