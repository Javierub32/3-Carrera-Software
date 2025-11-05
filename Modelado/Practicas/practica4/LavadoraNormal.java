package practica4;

import java.util.ArrayList;
import java.util.Enumeration;
import java.util.List;

import static java.util.Collections.enumeration;

public class LavadoraNormal extends Lavadora {
    private int capSuavizante;
    private List<ColadaNormal> coladas;

    public LavadoraNormal(String marca, int capDetergente, int maxTempLavado, int maxCentrifugado, int maxPeso, int capSuavizante) {
        super(marca, capDetergente, maxTempLavado, maxCentrifugado, maxPeso);
        this.capSuavizante = capSuavizante;
        this.coladas = new ArrayList<ColadaNormal>();

		assert(maxTempLavado <= 60);
		assert(maxCentrifugado <= 1800);
    }

    public int getCapSuavizante() { return capSuavizante; }
    protected void setCapSuavizante(int capSuavizante) { this.capSuavizante = capSuavizante; }

    public Enumeration<ColadaNormal> getColadas() { return enumeration(coladas); }
    protected void addColada(ColadaNormal colada) { coladas.add(colada); }
    protected void removeColada(ColadaNormal colada) { coladas.remove(colada); }

    //Los atributos derivados los convertimos en métodos
    public boolean enFuncionamiento(){
        ColadaNormal ultimaColada = coladas.get(coladas.size()-1);
        return (ultimaColada.getInicioC()!=-1 || ultimaColada.getInicioL()!=-1) && ultimaColada.getFin()==-1;
    }
}
