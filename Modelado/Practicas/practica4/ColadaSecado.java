package practica4;

public class ColadaSecado extends Colada {
    private int inicioS;
    private int tempSecado;
    LavadoraSecadora lavadora;

    //En las coladas de secado, no se conoce el inicio de secado cuando se crea
    public ColadaSecado(int temp, int rpm, int cantDetergente, EstadoPrenda estadoPrenda, Prenda prenda, int tempSecado, LavadoraSecadora lavadora) {
        super(temp, rpm, cantDetergente,estadoPrenda, prenda);
        this.tempSecado = tempSecado;
        inicioS = -1;
        this.lavadora = lavadora;

        //Para mantener la consistencia, añado esta colada a la Lavadora:
        lavadora.addColada(this);

		assert(cantDetergente <= lavadora.getCapDetergente());
		assert(tempSecado <= lavadora.getMaxTempSecado());
    }

    public int getInicioS() { return inicioS; }
    protected void setInicioS(int inicioS) { this.inicioS = inicioS; }

    public int getTempSecado() { return tempSecado; }
    protected void setTempSecado(int tempSecado) { this.tempSecado = tempSecado; }

    public LavadoraSecadora getLavadora(){return lavadora;}
}
