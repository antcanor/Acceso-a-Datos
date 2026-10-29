package org.dam.accesodatos.ut4.examen.models;

import jakarta.persistence.*;
import org.hibernate.annotations.ColumnDefault;

@Entity
@Table(name="planetas")
public class Planeta {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column(name = "planeta_id")
    private Integer id;

    @Column(name = "nombre", nullable = false, unique = true, length = 100)
    private String nombre;

    @Column(name = "clima", length = 50)
    private String clima;

    @Column(name = "afiliacion", length = 50)
    @ColumnDefault("'NEUTRAL'")
    private String afiliacion;

    public Planeta(){}

    public Planeta(Integer id, String nombre, String clima, String afiliacion) {
        this.id = id;
        this.nombre = nombre;
        this.clima = clima;
        this.afiliacion = afiliacion;
    }

    public Integer getId() {
        return id;
    }

    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public String getClima() {
        return clima;
    }

    public void setClima(String clima) {
        this.clima = clima;
    }

    public String getAfiliacion() {
        return afiliacion;
    }

    public void setAfiliacion(String afiliacion) {
        this.afiliacion = afiliacion;
    }
}
