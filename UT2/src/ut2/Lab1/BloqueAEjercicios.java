package ut2.Lab1;

import java.io.File;
import java.io.IOException;
import java.util.Scanner;

/**
 *
 * @author Antonio Cano Ruiz
 */
public class BloqueAEjercicios {
    
    public static void ejercicio1(){
        String ruta = "ficheros_dam";
        File f = new File(ruta);
        
        //Se crea el directorio, y el archivo setup.log
        if(!f.exists()){
            if(f.mkdir()){
                System.out.println("Directorio '" + ruta + "' creado con éxito.");
                
                File log = new File(ruta, "setup.log");
                try{
                    if(log.createNewFile()){
                        System.out.println("Fichero '" + log.getName() + "' creado correctamente.");
                    }else{
                        System.out.println("El fichero '" + f.getName() + "' ya existe en el disco.");   
                    }
                }catch (IOException e){
                    System.err.println("❌ Error al crear el archivo físico: " + e.getMessage());
                }
                
                
            }
        }else{
            
            //Si existe ya el directorio, se imprime el numero de archivos que lo componen
            boolean esDirectorio = f.isDirectory();
            
            if(esDirectorio){
                int nArchivos = f.listFiles().length;
                System.out.println("Es un directorio y contiene: "+nArchivos+" archivos.");
            }else{
                System.out.println("No es un directorio");
            }
        }
    }
    
    
    public static void ejercicio2(String ruta){
        
        //Primero se comprueba que el archivo exista, y si existe, se intenta eliminar.
        //Si no existe,saca el mensaje de que NO existe el archivo
        File temp = new File(ruta, "temp.bak");
        if(temp.exists() && temp.isFile()){
            System.out.println(temp.delete()?"Archivo borrado correctamente":"El archivo no se ha podido eliminar");
            
        }else if(!temp.exists()){
            System.out.println("NO existe el archivo");
        }
    }
    
    
    public static void ejercicio3(){
        
        //Lo primero se crean los directorios.
        //Si ya existe se notifica, al igual que cuando se crea o cuando no se puede crear
        
        File carpeta = new File("MurciaFP/2026/AccesoDatos");
        File nuevaCarpeta = new File("MurciaFP/2026/AD_Backup");
        
        if(carpeta.mkdirs()){
            System.out.println("Estructura de carpetas creada correctamente");
        }else if(carpeta.exists()){
            System.out.println("La estructura de carpetas ya existía");
        }else{
            System.out.println("No se ha podido crear la estructura de carpetas");
            return;
        }
        
        //Se cambia el nombre de la carpeta
        if(carpeta.renameTo(nuevaCarpeta)){
            System.out.println("Se ha cambiado el nombre de la carpeta");
        }else{
            System.out.println("No se ha podido cambiar el nombre de la carpeta");
        }
        
    }
    
    public static void main(String[] args) {
        ejercicio1();
        
        Scanner sc = new Scanner(System.in);
        System.out.print("Indica la ruta donde se van a borrar los archivos: ");
        String ruta = sc.nextLine();
        
        ejercicio2(ruta);
        
        ejercicio3();
        
        sc.close();
        
    }
    
}
