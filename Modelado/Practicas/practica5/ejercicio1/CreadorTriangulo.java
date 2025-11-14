package practica5.ejercicio1;

public class CreadorTriangulo extends CreadorFigura {
    private double base;
    private double altura;

    public CreadorTriangulo(double base, double altura) {
        this.base = base;
        this.altura = altura;
    }

    @Override
    public Figura crearFigura() {
        return new Triangulo(base, altura);
    }
}
