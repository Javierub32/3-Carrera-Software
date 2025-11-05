package practica4;

import java.util.ArrayList;
import java.util.Enumeration;
import java.util.List;

import static java.util.Collections.enumeration;

public abstract class Colada {
    private int temp;
    private int rpm;
    private int cantDetergente;
    private int inicioL;
    private int inicioC;
    private int fin;
    private List<Estado> estados;

    //Cuando se crea una colada, suponemos que no conocemos el inicio de lavado ni centrifugado ni el fin de la colada
    public Colada(int temp, int rpm, int cantDetergente, EstadoPrenda estadoPrenda, Prenda prenda) {
        this.temp = temp;
        this.rpm = rpm;
        this.cantDetergente = cantDetergente;
        inicioL = -1;
        inicioC = -1;
        fin = -1;
        this.estados = new ArrayList<Estado>();
        //Una colada necesita, al menos, un estado, así que lo crea:
        Estado estado = new Estado(estadoPrenda,this,prenda);
        /* No necesitamos añadir el objeto estado a la lista estados,
        ya que se hace al crear el Estado (colada.addEstado(this))
         */
    }

    public int getTemp() { return temp; }
    protected void setTemp(int temp) { this.temp = temp; }

    public int getRpm() { return rpm; }
    protected void setRpm(int rpm) { this.rpm = rpm; }

    public int getCantDetergente() { return cantDetergente; }
    protected void setCantDetergente(int cantDetergente) { this.cantDetergente = cantDetergente; }

    public int getInicioL() { return inicioL; }
    protected void setInicioL(int inicioL) { 
        this.inicioL = inicioL;
		assert((this.inicioL == -1 && this.inicioC == -1) || (this.inicioL < this.inicioC));
    }

    public int getInicioC() { return inicioC; }
    protected void setInicioC(int inicioC) { 
        this.inicioC = inicioC;
		assert((this.inicioL == -1 && this.inicioC == -1) || (this.inicioL < this.inicioC));
    }

    public int getFin() { return fin; }
    protected void setFin(int fin) { this.fin = fin; }

    public Enumeration<Estado> getEstados() { return enumeration(estados); }
    protected void addEstado(Estado estado) { 
		estados.add(estado);
		assert(jerseyFresco());
		assert(demasiadasPrendasSucias())
	}
    protected void removeEstado(Estado estado) { estados.remove(estado); }

    //Los atributos derivados los convertimos en métodos:
    public int getPeso(){
        int sumaPeso=0;
        for (Estado e : estados){sumaPeso+=e.getPrenda().getPeso();}
        return sumaPeso;
    }

    //Un método para comprobar si una Colada contiene una prenda:
    public boolean contiene(Prenda prenda){
        boolean contiene = false;
        Enumeration<Estado> it = this.getEstados();
        while(it.hasMoreElements() && !contiene){
            if(it.nextElement().getPrenda()==prenda) contiene = true;
        }
        return contiene;
    }

	public void concluyeColada(int fin){
		this.setFin(fin);
		
		if (this.cantDetergente >= 50) {
			this.estados.forEach(estado -> estado.setEstado(EstadoPrenda.LIMPIO));
		}
		else {
			this.estados.forEach(estado -> {
				if (estado.getEstado() == EstadoPrenda.MUY_SUCIO) {
					estado.setEstado(EstadoPrenda.SUCIO);
				} else {
					estado.setEstado(EstadoPrenda.LIMPIO);
				}
			});
		}
		/*
		for (Estado e : this.estados) {
			if (this.cantDetergente >= 50) {
				e.setEstado(EstadoPrenda.LIMPIO);
			} else {
				if (e.getEstado() == EstadoPrenda.MUY_SUCIO) {
					e.setEstado(EstadoPrenda.SUCIO);
				} else {	
					e.setEstado(EstadoPrenda.LIMPIO);
				}
			}
		}
		 */
	}

	public Boolean jerseyFresco() {
		for (Estado e : this.estados) {
			if ((e.getPrenda().getTipo() == TipoPrenda.JERSEY) && this.temp > 30) {
				return false;
			}
		}
		return true;
	}

	public Boolean demasiadasPrendasSucias() {
		if (this.getPeso() > 5){
			int cantidadSucias = 0;
			int cantidadTotal = 0;

			for (Estado e: this.estados){
				if (e.getEstado() == EstadoPrenda.MUY_SUCIO) cantidadSucias += 1;
				cantidadTotal += 1;
			}

			if (cantidadSucias < cantidadTotal/2) return false;
			else return true;
		}
		return true;
	}
}
