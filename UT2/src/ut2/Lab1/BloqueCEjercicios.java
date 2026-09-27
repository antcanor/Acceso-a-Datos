package ut2.Lab1;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.util.Scanner;
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
 * @author antonio
 */
public class BloqueCEjercicios {
    
    public static void ejercicio8(){
        System.out.print("Inserta la ruta del archivo que se quiere leer: ");
        Scanner sc = new Scanner(System.in);
        String ruta = sc.nextLine();
        
        try(BufferedReader br = new BufferedReader(new FileReader(ruta))){
            
            String linea;
            
            while((linea = br.readLine())!= null){
                System.out.println(linea);
            }
            System.out.println("Archivo leido al completo");
        }catch(FileNotFoundException e){
            System.out.println("Te has equivocado al especificar la ruta");
        }catch(IOException e){
            System.out.println("Error al abrir el archivo");
        }finally{
            sc.close();
        }
        
    }
    
    public static void ejercicio9(){
        File f = new File("datos_notas.txt");
        try(BufferedReader br = new BufferedReader(new FileReader(f))){
            String linea;
            
            while((linea = br.readLine())!= null){
                try {
                    double nota = Double.parseDouble(linea);
            
                } catch (NumberFormatException e) {
                    System.err.println("Error al parsear una linea a double");
                }
            }
            
            System.out.println("Archivo leido al completo");
        }catch(FileNotFoundException e){
            System.out.println("NO se ha encontrado el archivo");
        }catch(IOException e){
            System.out.println("Error al abrir el archivo");
        }
    }
    
    public static void ejercicio10(){
        try {
        DocumentBuilderFactory factory = DocumentBuilderFactory.newInstance();
        DocumentBuilder builder = factory.newDocumentBuilder();
        
        Document doc = builder.newDocument();
        
        Element instituto = doc.createElement("instituto");
        doc.appendChild(instituto);
        
        
        Element modulo = doc.createElement("modulo");
        modulo.setAttribute("codigo", "DAM");
        
        modulo.appendChild(doc.createTextNode("Acceso a Datos"));
        
        
        instituto.appendChild(modulo);
        
        TransformerFactory transformerFactory = TransformerFactory.newInstance();
        Transformer transformer = transformerFactory.newTransformer();
        
        DOMSource source = new DOMSource(doc);
        StreamResult result = new StreamResult(new File("instituto.xml"));
        
        transformer.transform(source, result);
        System.out.println("Archvio guardado con éxito.");
        
    } catch (ParserConfigurationException e) {
        System.out.println("Error de configuración del analizador XML");
    } catch (TransformerException e) {
        System.out.println("Error al transformar el documento a archivo físico");
    }            
    }
    
    
    public static void main(String[] args) {
        ejercicio8();
        ejercicio9();
        ejercicio10();
        
    }
}
