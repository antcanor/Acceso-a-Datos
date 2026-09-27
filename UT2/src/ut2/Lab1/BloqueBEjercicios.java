package ut2.Lab1;

import java.io.*;
import java.util.Scanner;
import java.io.RandomAccessFile;

/**
 *
 * @author Antonio Cano Ruiz
 */
public class BloqueBEjercicios {
    
    public static void ejercicio4(String archivoLeer){
        //Se coge el nombre del archivo, y su extension, ya que los vamos a utilizar para el otro archivo
        String[] archivo = archivoLeer.split("\\.");
        String nombre = "copia_"+archivo[0]+"."+archivo[1];
        
        
        System.out.println("Se comienza a leer el archivo");
        try(FileInputStream fis = new FileInputStream(archivoLeer);
                FileOutputStream fos = new FileOutputStream(nombre);) {
            
            //Se leen los bytes del archivo original, y si copian en el nuevo archivo copia
            fos.write(fis.readAllBytes());
            System.out.println("Archivo copiado con éxito");
                
            
        }catch(FileNotFoundException e){
            System.out.println("NO se ha encontrado el archivo a leer");
        }catch(IOException e){
            System.out.println("Error al intentar leer el archivo");
        }
    }
    
    
    public static void ejercicio5(String archivo){
        int numeroLineas= 0;
        int numeroPalabras=0;
        File f = new File(archivo);
        if(f.exists() && f.isFile()){
            try(FileReader fr = new FileReader(f);
                    BufferedReader br = new BufferedReader(fr)){
                String linea;
                while((linea = br.readLine())!= null){
                    numeroLineas++;
                    
                    String[] palabras = linea.split(" ");
                    for(String p : palabras){
                        if(p.equals("Quijote")) numeroPalabras++;
                    }
                }
                
                System.out.println("Numero de lineas: "+numeroLineas);
                System.out.println("Numero de palabras: "+numeroPalabras);
                
            }catch(FileNotFoundException e){
                System.out.println("NO se ha encontrado el archivo a leer");
            }catch(IOException e){
                System.out.println("Error al intentar leer el archivo");
            }
        }
        
    }
    
    public static void ejercicio6(String nombreArchivo){
        System.out.println("\n\n EJERCICIO 6");
        
        try(Scanner sc = new Scanner(System.in);FileWriter fw = new FileWriter(nombreArchivo,true); BufferedWriter bw = new BufferedWriter(fw)){
            for (int i = 0; i < 3; i++) {
                String nombreAlumno;double notaAlumno;
                System.out.println("Como se llama el alumno "+i+": ");
                nombreAlumno= sc.nextLine();
                System.out.println("¿Qué nota quieres ponerle a "+ nombreAlumno+" ?");
                notaAlumno = Double.parseDouble(sc.nextLine());
                
                bw.write("Alumno : "+nombreAlumno+"; Nota: "+notaAlumno+"\n");
                
            }
                
        }catch(IOException e){
            System.out.println("Error al abrir el archivo");
        }
    }
    
    public static void ejercicio7(String archivo){
        try(RandomAccessFile raf = new RandomAccessFile(archivo, "rw")){
            raf.writeInt(1);
            raf.writeInt(2);
            raf.writeInt(3);
            
            //Se vuelve al byte numero 4 ( ya que los enteros los forman 4 bytes)
            raf.seek(4);
            //Se sustituye el byte numero 4 con el entero 999
            raf.writeInt(999);
            
            //Se vuelve el puntero al byte numero 0
            raf.seek(0);
            
            System.out.println("Primer entero: "+raf.readInt());
            System.out.println("Segundo entero: "+raf.readInt());
            System.out.println("Tercer entero: "+raf.readInt());
            
            
        }catch(IOException e){
            System.out.println("Error");
        }
    }
    
    public static void main(String[] args) {
        ejercicio4("logo.png");
        ejercicio5("quijote.txt");
        ejercicio6("calificaciones.txt");
        ejercicio7("datos.dat");
        
    }
}
