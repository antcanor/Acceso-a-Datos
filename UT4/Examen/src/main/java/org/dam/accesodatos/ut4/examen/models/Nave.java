package org.dam.accesodatos.ut4.examen.models;

import jakarta.persistence.*;
import java.io.Serializable;

@Entity
@Table(name = "naves")
@Inheritance(strategy = InheritanceType.SINGLE_TABLE) // Estrategia base
@DiscriminatorColumn(name = "tipo_nave", discriminatorType = DiscriminatorType.STRING)
public abstract class Nave implements Serializable {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column(name = "nave_id")
    private int id;

    @Column(name = "nombre", nullable = false, length = 100)
    private String nombre;

    @Column(name = "modelo", length = 50, nullable = false)
    private String modelo;

    @Column(name = "estado_sistema", nullable = false, length = 20)
    private String estadoSistema;

    @ManyToOne(fetch = FetchType.LAZY)
    @JoinColumn(name = "planeta_origen_id")
    private Planeta planetaOrigen;

    public Nave(){}

    public Nave(String nombre, String modelo, String estadoSistema, Planeta planetaOrigen) {
        this.nombre = nombre;
        this.modelo = modelo;
        this.estadoSistema = estadoSistema;
        this.planetaOrigen = planetaOrigen;
    }

    public int getId() {
        return id;
    }

    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public String getModelo() {
        return modelo;
    }

    public void setModelo(String modelo) {
        this.modelo = modelo;
    }

    public String getEstadoSistema() {
        return estadoSistema;
    }

    public void setEstadoSistema(String estadoSistema) {
        this.estadoSistema = estadoSistema;
    }

    public Planeta getPlanetaOrigen() {
        return planetaOrigen;
    }

    public void setPlanetaOrigen(Planeta planetaOrigen) {
        this.planetaOrigen = planetaOrigen;
    }

    @Override
    public String toString() {
        return "Nave{" +
                "id=" + id +
                ", nombre='" + nombre + '\'' +
                ", modelo='" + modelo + '\'' +
                ", estadoSistema='" + estadoSistema + '\'' +
                ", planetaOrigen=" + planetaOrigen +
                '}';
    }
}
