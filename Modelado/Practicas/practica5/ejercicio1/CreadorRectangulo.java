package practica5.ejercicio1;

public class CreadorRectangulo extends CreadorFigura {
    private double base;
    private double altura;

    public CreadorRectangulo(double base, double altura) {
        this.base = base;
        this.altura = altura;
    }

    @Override
    public Figura crearFigura() {
        return new Rectangulo(base, altura);
    }
}
