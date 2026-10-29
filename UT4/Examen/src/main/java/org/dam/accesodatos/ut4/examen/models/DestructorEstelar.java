package org.dam.accesodatos.ut4.examen.models;

import jakarta.persistence.*;

@Entity
@DiscriminatorValue("DESTRUCTOR")
public class DestructorEstelar extends Nave {

    @Column(name = "capacidad_escudos")
    private int capacidadEscudos;

    public DestructorEstelar() {
        super();
    }

    public DestructorEstelar(String nombre, String modelo, String estadoSistema, Planeta planetaOrigen, int capacidadEscudos) {
        super(nombre, modelo, estadoSistema, planetaOrigen);
        this.capacidadEscudos = capacidadEscudos;
    }

    public int getCapacidadEscudos() {
        return capacidadEscudos;
    }

    public void setCapacidadEscudos(int capacidadEscudos) {
        this.capacidadEscudos = capacidadEscudos;
    }

    @Override
    public String toString() {
        return "DestructorEstelar{" +
                "capacidadEscudos=" + capacidadEscudos +
                '}';
    }
}
