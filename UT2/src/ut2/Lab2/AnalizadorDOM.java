package ut2.Lab2;

import java.io.File;
import javax.xml.parsers.DocumentBuilder;
import javax.xml.parsers.DocumentBuilderFactory;
import org.w3c.dom.Document;
import org.w3c.dom.Element;
import org.w3c.dom.Node;
import org.w3c.dom.NodeList;

/**
 *
 * @author antonio
 */
public class AnalizadorDOM {
    public static void main(String[] args) {
        
        try {
            // Cargamos el archivo XML
            File f = new File("imperio.xml");

            // Creamos el parser DOM
            DocumentBuilderFactory factory = DocumentBuilderFactory.newInstance();
            DocumentBuilder builder = factory.newDocumentBuilder();

            // Parseamos el XML y creamos el árbol DOM
            Document doc = builder.parse(f);

            // Normalizamos el documento
            doc.getDocumentElement().normalize();

            // Mostramos el nombre del nodo raíz
            System.out.println("Nodo raíz: " + doc.getDocumentElement().getNodeName());

            // Obtenemos todas las etiquetas <nave>
            NodeList naves = doc.getElementsByTagName("nave");

            // Recorremos todas las naves
            for (int i = 0; i < naves.getLength(); i++) {
                Node nodo = naves.item(i);

                // Comprobamos que el nodo sea un elemento
                if (nodo.getNodeType() == Node.ELEMENT_NODE) {
                    Element nave = (Element) nodo;

                    // Obtenemos los atributos de la nave
                    String id = nave.getAttribute("id");
                    String clase = nave.getAttribute("clase");

                    // Obtenemos el contenido de nombre y piloto
                    String nombre = nave.getElementsByTagName("nombre").item(0).getTextContent();
                    String piloto = nave.getElementsByTagName("piloto").item(0).getTextContent();

                    // Mostramos los datos de la nave
                    System.out.println("ID de Nave: " + id + "; Clase: " + clase +
                            "; Nombre: " + nombre + "; Piloto: " + piloto);
                }
            }

        } catch (Exception e) {
            // Mostramos el mensaje de error
            System.err.println("Error al leer el árbol DOM: " + e.getMessage());
        }


    }
    
}
