package practica4;

public class ColadaNormal extends Colada {
    private int cantSuavizante;
    private LavadoraNormal lavadora;

    public ColadaNormal(int temp, int rpm, int cantDetergente,  EstadoPrenda estadoPrenda, Prenda prenda, int cantSuavizante, LavadoraNormal lavadora) {
        super(temp, rpm, cantDetergente,estadoPrenda, prenda);
        this.cantSuavizante = cantSuavizante;
        this.lavadora = lavadora;

        //Para mantener la consistencia, añado esta colada a la Lavadora:
        lavadora.addColada(this);
		assert(cantDetergente <= lavadora.getCapDetergente());
		assert(cantSuavizante <= lavadora.getCapSuavizante());
    }

    public int getCantSuavizante() {
        return cantSuavizante;
    }
    protected void setCantSuavizante(int cantSuavizante) {
        this.cantSuavizante = cantSuavizante;
    }

    public LavadoraNormal getLavadora(){return lavadora;}
}
