package org.dam.accesodatos.ut4.examen.models;


import jakarta.persistence.*;

@Entity
@DiscriminatorValue("CAZA")
public class CazaLigero extends Nave{
    @Column(name = "potencia_fuego")
    private Integer potenciaFuego;

    public CazaLigero() {
        super();
    }

    public CazaLigero(String nombre, String modelo, String estadoSistema, Planeta planetaOrigen, Integer potenciaFuego) {
        super(nombre, modelo, estadoSistema, planetaOrigen);
        this.potenciaFuego = potenciaFuego;
    }

    public Integer getPotenciaFuego() {
        return potenciaFuego;
    }

    public void setPotenciaFuego(Integer potenciaFuego) {
        this.potenciaFuego = potenciaFuego;
    }

    @Override
    public String toString() {
        return "CazaLigero{" +
                "potenciaFuego=" + potenciaFuego +
                '}';
    }
}
