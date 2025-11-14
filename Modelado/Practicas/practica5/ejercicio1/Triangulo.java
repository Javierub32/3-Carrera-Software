package practica5.ejercicio1;

public class Triangulo implements Figura {
    private double base;
    private double altura;
	private DibujaTriangulo dt;

    public Triangulo(double base, double altura) {
        this.base = base;
        this.altura = altura;
		this.dt = new DibujaTriangulo(base, altura);
    }

    @Override
    public void dibujar() {
        System.out.println("Dibujando un triángulo de base " + base + " y altura " + altura);
        System.out.println("Su área es: " + area());
		dt.dibujarTriangulo();
    }

    @Override
    public double area() {
        return (base * altura) / 2;
    }
}
