package practica5.ejercicio1;

public class Main {
    public static void main(String[] args) {
        // Crear dos triángulos
        CreadorFigura creadorTriangulo1 = new CreadorTriangulo(5.0, 5.0);
        creadorTriangulo1.dibujarFigura();
        
        CreadorFigura creadorTriangulo2 = new CreadorTriangulo(5.0, 7.0);
        creadorTriangulo2.dibujarFigura();
        
        // Crear dos rectángulos
        CreadorFigura creadorRectangulo1 = new CreadorRectangulo(4.0, 6.0);
        creadorRectangulo1.dibujarFigura();
        
        CreadorFigura creadorRectangulo2 = new CreadorRectangulo(3.0, 8.0);
        creadorRectangulo2.dibujarFigura();
        
        // Crear dos círculos
        CreadorFigura creadorCirculo1 = new CreadorCirculo(3.0);
        creadorCirculo1.dibujarFigura();
        
        CreadorFigura creadorCirculo2 = new CreadorCirculo(5.0);
        creadorCirculo2.dibujarFigura();
    }
}
