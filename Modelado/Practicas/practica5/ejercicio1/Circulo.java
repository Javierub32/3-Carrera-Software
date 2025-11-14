package practica5.ejercicio1;

public class Circulo implements Figura {
    private double radio;

    public Circulo(double radio) {
        this.radio = radio;
    }

    @Override
    public void dibujar() {
        System.out.println("Dibujando un círculo de radio " + radio);
        System.out.println("Su área es: " + area());
    }

    @Override
    public double area() {
        return Math.PI * radio * radio;
    }
}
