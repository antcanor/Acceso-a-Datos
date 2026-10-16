package ut2.Lab2;

import jakarta.xml.bind.annotation.XmlElement;
import jakarta.xml.bind.annotation.XmlRootElement;
import jakarta.xml.bind.annotation.XmlType;
import java.io.Serializable;

/**
 *
 * @author Antonio Cano Ruiz
 */

@XmlRootElement(name = "personaje")
public class Personaje implements Serializable{
    private String nombre;
    private String rango;
    
    
}
