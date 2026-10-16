package armadaimperial.ut2.examen.javabean;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;
import jakarta.xml.bind.JAXBContext;
import jakarta.xml.bind.Marshaller;

/**
 *
 * @author Antonio Cano Ruiz
 */
public class UT2ExamenJavaBean {
    
    public static List<SistemaCritico> lecturaArchivo(){
        ArrayList<SistemaCritico> listaSistemasCriticos = new ArrayList<>();
        String archivo = "estado_sistemas.txt";
        File f = new File(archivo);
        
        try(FileReader fr = new FileReader(f);
            BufferedReader br = new BufferedReader(fr);) {
            
            String linea;
            
            while((linea = br.readLine()) != null){
                
                
                String[] sistemas = linea.split(",");
              
                if(sistemas.length==3 && sistemas[2].trim().equalsIgnoreCase("Critico")){
                    String objetivo = sistemas[0].trim();
                    String componente = sistemas[1].trim();
                    listaSistemasCriticos.add(new SistemaCritico(objetivo, componente));
                }
            }
         } catch (FileNotFoundException e) {
            //Excapción al abrir el fichero
            System.err.println("Error: Transmisión imperial no encontrada");
        }catch(IOException e) {
            System.err.println("Error:"+e);
        }
        

        return listaSistemasCriticos;
    }
    
    public static void exportacionUrgente(List<SistemaCritico> listaSistemaCriticos){
        File destino = new File("objetivo_urgente.xml");

        try {
            // Creamos el contexto JAXB para la clase Personaje
            JAXBContext contexto = JAXBContext.newInstance(SistemaCritico.class);

            // Creamos el objeto encargado de convertir el objeto a XML
            Marshaller marshaller = contexto.createMarshaller();

            // Formateamos el XML para que sea más legible
            marshaller.setProperty(Marshaller.JAXB_FORMATTED_OUTPUT, Boolean.TRUE);
            
            SistemaCritico objetivoUrgente = listaSistemaCriticos.getFirst();
            // Convertimos el objeto a XML y lo guardamos en el archivo
            marshaller.marshal(objetivoUrgente, destino);

            System.out.println("Se ha generado el ficjero 'objetivo_urgente.xml' con el objetivo urgente");

        } catch (Exception e) {
            // Mostramos el mensaje de error
            System.err.println("Error en el Marshalling: " + e.getMessage());
        }
    }

    public static void main(String[] args) {
        exportacionUrgente(lecturaArchivo());
        
    }
}
