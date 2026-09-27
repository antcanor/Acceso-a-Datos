package ut2;

import java.io.File;
import java.io.IOException;

/**
 *
 * @author antonio
 */
public class GestionDirectorios {
    
    public static void main(String[] args){
        String rutaBase="PracticasDAM";
        
        File directorioBase = new File(rutaBase);
        
        System.out.println("===Iniciando Gestión de Ficheros===");
        
        if(!directorioBase.exists()){
            
            if(directorioBase.mkdir()){
                System.out.println("✔ Directorio '" + rutaBase + "' creado con éxito.");
            }
            
        }else{
            System.out.println("ℹ El directorio '" + rutaBase + "' ya existía.");
        }
        
        
        File nuevoFichero = new File(directorioBase, "notas_evaluacion.txt");
        
         try {
            if (nuevoFichero.createNewFile()) {
                System.out.println("✔ Fichero '" + nuevoFichero.getName() + "' creado correctamente.");
            } else {
                System.out.println("ℹ El fichero '" + nuevoFichero.getName() + "' ya existe en el disco.");   
            }
            
            System.out.println("\n--- Propiedades del Fichero ---");
            System.out.println("Ruta absoluta: " + nuevoFichero.getAbsolutePath());
            System.out.println("¿Es un fichero ejecutable?: " + nuevoFichero.canExecute());
            System.out.println("Tamaño actual en bytes: " + nuevoFichero.length());

        } catch (IOException e) {
            System.err.println("❌ Error al crear el archivo físico: " + e.getMessage());
        }
    }
}
      
