package practica5.ejercicio1;

public class Rectangulo implements Figura {
    private double base;
    private double altura;

    public Rectangulo(double base, double altura) {
        this.base = base;
        this.altura = altura;
    }

    @Override
    public void dibujar() {
        System.out.println("Dibujando un rectángulo de base " + base + " y altura " + altura);
        System.out.println("Su área es: " + area());
    }

    @Override
    public double area() {
        return base * altura;
    }
}
