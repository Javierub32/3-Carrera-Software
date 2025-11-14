package practica5.ejercicio1;

public class CreadorCirculo extends CreadorFigura {
    private double radio;

    public CreadorCirculo(double radio) {
        this.radio = radio;
    }

    @Override
    public Figura crearFigura() {
        return new Circulo(radio);
    }
}
