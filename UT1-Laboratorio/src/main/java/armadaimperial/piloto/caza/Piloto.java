package armadaimperial.piloto.caza;

import java.io.Serializable;

/**
 *
 * @author Antonio Cano Ruiz y Álvaro José Hernández Sánchez
 */
public class Piloto implements Serializable {
    
    //Atributos de la clase Piloto
    private String id;
    private String nombre;
    private String planeta;
    private double notaMedia;
    
    //Se crea el constructor vacío
    public Piloto(){}
    
    //Constructor que inicializa los atributos
    public Piloto(String id, String nombre, String planeta, double notaMedia){
        this.id = id;
        this.nombre = nombre;
        this.planeta = planeta;
        this.notaMedia = notaMedia;
    }
    
    //Getter y Setter de la clase

    public String getId() {
        return id;
    }

    public String getNombre() {
        return nombre;
    }

    public double getNotaMedia() {
        return notaMedia;
    }

    public String getPlaneta() {
        return planeta;
    }

    public void setId(String id) {
        this.id = id;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public void setNotaMedia(double notaMedia) {
        this.notaMedia = notaMedia;
    }

    public void setPlaneta(String planeta) {
        this.planeta = planeta;
    }
    
    

    //Método toString con la información de cada piloto
    @Override
    public String toString() {
        return "ID Piloto: "+this.id+"; Nombre Piloto: "+this.nombre+"; Planeta Piloto: "+this.planeta+"; Nota Media Piloto: "+this.notaMedia;
    }
    
    
    
}
