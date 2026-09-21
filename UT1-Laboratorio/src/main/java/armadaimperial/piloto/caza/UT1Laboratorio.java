package armadaimperial.piloto.caza;

import java.io.*;
import java.util.List;
import java.util.ArrayList;
import java.io.IOException;

/**
 *
 * @author Antonio Cano Ruiz y Álvaro José Hernández Sánchez
 */
public class UT1Laboratorio {
    
    public static String guardarEnBinario(List<Piloto> pilotos, String archivoBinario){
        System.out.println("\nComienza la serialización");
        //EL try-with-resources Cierra automáticamente los flujos
        try(FileOutputStream fos = new FileOutputStream(archivoBinario);
            ObjectOutputStream oos = new ObjectOutputStream(fos);) {
            
            //Se guarda la lista de pilotos
            for(Piloto p : pilotos){
                oos.writeObject(p);
                System.out.println(p);
            }
            
        } catch (IOException e) {
            //Se gestiona la excepción al guardar
            System.err.println("Error al guardar: " + e.getMessage());
        }
        
        //Se devuelve el nombre del archivo, para poder usarlo al leer.
        return archivoBinario;
        
    }
    
   public static void leerBinario(String binario){
       System.out.println("\nComienza la deserialización");
       try(FileInputStream fis = new FileInputStream(binario);
           ObjectInputStream ois = new ObjectInputStream(fis);) {

           while(true) {
               try{
                   //Se van creando los objetos de Piloto con la información del archivo binario
                   Piloto p = (Piloto) ois.readObject();
                   System.out.println(p);
                   
                }catch(EOFException e) {
                    //Excepción al terminar de leer el archivo
                    System.out.println("Archivo leido");
                    break;
               }
               
           }
           
       } catch (IOException e) {
           //Excepción al leer el archivo
           System.err.println("Error al recuperar: " + e.getMessage());
       }catch (ClassNotFoundException e){
           //Excepción al hacer el casting 
           System.err.println("Erroral buscar clase Piloto: " + e.getMessage());
       }
       
       
   }

    public static void main(String[] args) {
        
        //Se busca el archivo
        File fichero = new File("nuevos_pilotos.txt");
        
        try(FileReader fr = new FileReader(fichero);
            BufferedReader br = new BufferedReader(fr);) {
            
            //Se crea lista de pilotos, que se inicializa como vacía
            ArrayList<Piloto> pilotos = new ArrayList<>();
            String linea;
            
            //EL bucle se ejectuca hasta que readLine() devuelva un null
            while((linea = br.readLine()) != null){
                
                //Se separa la información del piloto, y se guarda en un array de cadenas
                String[] piloto = linea.split(",");
                
                //Se comprueba que cada piloto tiene sus 4 atributos
                if(piloto.length==4){
                    
                    //Se crea el piloto y se añade en la lista
                    Piloto p = new Piloto(piloto[0], piloto[1], piloto[2], Double.parseDouble(piloto[3]));
                    pilotos.add(p);
                }
                
            }
            
            //Se guarda en el archivo binario
            String binario = guardarEnBinario(pilotos, "matriculados.dat");
            
            //Se lee el archivo y se deserializa
            leerBinario(binario);
                       
            
        } catch (IOException e) {
            //Excapción al abrir el fichero
            System.err.println("Error al procesar el fichero: " + e.getMessage());
        }
        
    }
}
