package armadaimperial.ut2.examen.javabean;

import java.io.Serializable;
import jakarta.xml.bind.annotation.XmlElement;
import jakarta.xml.bind.annotation.XmlRootElement;
import jakarta.xml.bind.annotation.XmlType;
/**
 *
 * @author Antonio Cano Ruiz
 */
@XmlRootElement(name = "sistemaCritico")
@XmlType(propOrder = {"instalacionONave", "componente"})
public class SistemaCritico implements Serializable{
    private String instalacionONave;
    private String componente;
    
    public SistemaCritico(){
        
    }
    public SistemaCritico(String instalacionONave, String componente){
        this.instalacionONave= instalacionONave;
        this.componente=componente;
    }
    
    @XmlElement(name = "instalacionONave")
    public String getInstalacionONave() {
        return instalacionONave;
    }
    
    public void setInstalacionONave(String instalacionONave) {
        this.instalacionONave = instalacionONave;
    }
    
    @XmlElement(name = "componente")
    public String getComponente() {
        return componente;
    }

    public void setComponente(String componente) {
        this.componente = componente;
    }
    
}
