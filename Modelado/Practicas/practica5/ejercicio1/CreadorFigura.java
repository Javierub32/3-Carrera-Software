package practica5.ejercicio1;

public abstract class CreadorFigura {
	public abstract Figura crearFigura();

	public void dibujarFigura() {
		Figura figura = crearFigura();
		figura.dibujar();
	}
}
