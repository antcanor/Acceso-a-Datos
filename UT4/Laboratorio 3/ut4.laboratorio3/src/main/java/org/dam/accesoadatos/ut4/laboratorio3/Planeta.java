package org.dam.accesoadatos.ut4.laboratorio3;

import jakarta.persistence.*;
import java.io.Serializable;
import java.util.List;

@Entity
@Table(name = "planetas")
public class Planeta implements Serializable {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column(name = "planeta_id")
    private int id;

    @Column(name = "nombre", nullable = false, length = 100)
    private String nombre;

    @Column(name = "afiliacion", nullable = false, length = 50)
    private String afiliacion;
    
    // mappedBy: Indica "vete a la clase Nave y busca el atributo privado llamado planetaOrigen"
    // cascade: Si borramos un planeta, podemos arrastrar o desvincular sus naves asociadas
    @OneToMany(mappedBy = "planetaOrigen", cascade = CascadeType.ALL, fetch = FetchType.LAZY)
    private List<Nave> listaNaves = new java.util.ArrayList<>();

    // Constructor obligatorio JPA
    public Planeta() {}
    
    public Planeta(String nombrePlaneta, String sectorGalactico) {
        this.nombre = nombrePlaneta;
        this.afiliacion = sectorGalactico;
    }

    // Getters y Setters
    public int getId() { return id; }
    public void setId(int id) { this.id = id; }
    public String getNombrePlaneta() { return nombre; }
    public void setNombrePlaneta(String nombrePlaneta) { this.nombre = nombrePlaneta; }
    public String getSectorGalactico() { return afiliacion; }
    public void setSectorGalactico(String sectorGalactico) { this.afiliacion = sectorGalactico; }
    
    public List<Nave> getListaNaves() { return listaNaves; }
    public void setListaNaves(List<Nave> listaNaves) { this.listaNaves = listaNaves; }

    // MÉTODO HELPER (Práctica recomendada para sincronizar ambos lados de la relación en memoria)
    public void agregarNave(Nave nave) {
        this.listaNaves.add(nave);
        nave.setPlanetaOrigen(this); // Sincroniza la clave ajena de forma automática en la Nave
    }

    @Override
    public String toString() {
        return "Planeta [ID=" + id + ", Nombre=" + nombre + ", Sector=" + afiliacion + "]";
    }

}