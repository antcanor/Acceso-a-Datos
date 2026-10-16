package armadaimperial.ut2.examen.xml;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;
import javax.xml.parsers.DocumentBuilder;
import javax.xml.parsers.DocumentBuilderFactory;
import javax.xml.parsers.ParserConfigurationException;
import javax.xml.transform.Transformer;
import javax.xml.transform.TransformerException;
import javax.xml.transform.TransformerFactory;
import javax.xml.transform.dom.DOMSource;
import javax.xml.transform.stream.StreamResult;
import org.w3c.dom.Document;
import org.w3c.dom.Element;

/**
 *
 * @author Antonio Cano Ruiz
 */
public class UT2ExamenXml {
    
    public static Map<String, List<String>> sacarObjetivos (){
        String archivo = "estado_sistemas.txt";
        File f = new File(archivo);
        
        Map<String, List<String>> mapaObjetivos = new LinkedHashMap<>();
        
        try(FileReader fr = new FileReader(f);
            BufferedReader br = new BufferedReader(fr);) {
            
            String linea;
            
            while((linea = br.readLine()) != null){
                
                
                String[] sistemas = linea.split(",");
              
                if(sistemas.length==3 && sistemas[2].trim().equalsIgnoreCase("Critico")){
                    String objetivo = sistemas[0].trim();
                    String componente = sistemas[1].trim();
                    
                    if (!mapaObjetivos.containsKey(objetivo)) {
                        mapaObjetivos.put(objetivo, new ArrayList<>());
                    }

                    mapaObjetivos.get(objetivo).add(componente);
                }
            }
         } catch (FileNotFoundException e) {
            //Excapción al abrir el fichero
            System.err.println("Error: Transmisión imperial no encontrada");
        }catch(IOException e) {
            System.err.println("Error:"+e);
        }
        
        return mapaObjetivos;
    }
    
    public static void descubrirObjetivos(Map<String, List<String>> mapaObjetivos){
        File destino = new File("rebelde.xml");
        try {
            DocumentBuilderFactory factory = DocumentBuilderFactory.newInstance();
            DocumentBuilder builder = factory.newDocumentBuilder();

            Document doc = builder.newDocument();

            Element objetivos = doc.createElement("objetivos");
            doc.appendChild(objetivos);
            
            for (Map.Entry<String, List<String>> entrada : mapaObjetivos.entrySet()) {
                Element sistema = doc.createElement("sistema");
                sistema.setAttribute("objetivo", entrada.getKey());

                for (String nombreComponente : entrada.getValue()) {
                    Element componente = doc.createElement("componente");
                    componente.appendChild(doc.createTextNode(nombreComponente));
                    sistema.appendChild(componente);
                }

                objetivos.appendChild(sistema);
            }
            
            TransformerFactory transformerFactory = TransformerFactory.newInstance();
            Transformer transformer = transformerFactory.newTransformer();

            DOMSource source = new DOMSource(doc);
            StreamResult result = new StreamResult(new File("objetivos_sabotaje.xml"));

            transformer.transform(source, result);
            System.out.println("Archvio guardado con éxito.");

        } catch (ParserConfigurationException e) {
            System.out.println("Error de configuración del analizador XML");
        } catch (TransformerException e) {
            System.out.println("Error al transformar el documento a archivo físico");
        }  
    }

    public static void main(String[] args) {
        descubrirObjetivos(sacarObjetivos());
    }
                   
}
