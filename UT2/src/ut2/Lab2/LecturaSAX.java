package ut2.Lab2;

import java.io.File;
import org.xml.sax.Attributes;
import javax.xml.parsers.SAXParser;
import javax.xml.parsers.SAXParserFactory;
import org.xml.sax.SAXException;
import org.xml.sax.helpers.DefaultHandler;

/**
 *
 * @author Antonio Cano Ruiz
 */
public class LecturaSAX {
    public static void main(String[] args) {
        try {
            // Creamos el parser SAX
            SAXParserFactory spf = SAXParserFactory.newInstance();
            SAXParser sp = spf.newSAXParser();

            // Definimos el manejador de eventos
            DefaultHandler handler = new DefaultHandler() {

                // Indica si estamos leyendo el nombre de una nave
                private boolean esNombre = false;

                // Guarda la clase de la nave actual
                private String claseActual = "";

                // Se ejecuta al encontrar una etiqueta de apertura
                @Override
                public void startElement(String uri, String localName, String name, Attributes attributes) throws SAXException {

                    // Guardamos la clase de la nave
                    if (name.equalsIgnoreCase("nave")) {
                        claseActual = attributes.getValue("clase");

                    // Indicamos que vamos a leer el nombre
                    } else if (name.equalsIgnoreCase("nombre")) {
                        esNombre = true;
                    }
                }

                // Se ejecuta al encontrar texto dentro de una etiqueta
                @Override
                public void characters(char[] ch, int start, int length) throws SAXException {
                    if (esNombre) {
                        String nombreNave = new String(ch, start, length);

                        // Mostramos el nombre y la clase de la nave
                        System.out.println("Nave: " + nombreNave + "; Clase: " + claseActual);

                        // Dejamos de leer el nombre
                        esNombre = false;
                    }
                }
            };

            // Leemos el archivo XML usando el manejador
            sp.parse(new File("imperio.xml"), handler);

        } catch (Exception e) {
            // Mostramos el mensaje de error
            System.err.println("Error en la lectura SAX: " + e.getMessage());
        }
    }
}
