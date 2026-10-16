package com.alianzarebelde.holonet;

import java.util.Scanner;
import java.util.List;

/**
 *
 * @author Antonio Cano Ruiz
 */
public class HoloNet {
	
    private static final Scanner sc = new Scanner(System.in);


    public static void main(String[] args) {
        EscuadronDAO dao;

        try {
            dao = new EscuadronDAOImpl();
        } catch (IllegalStateException e) {
            System.err.println("Error de conexión con HoloNet.");
            System.err.println(e.getMessage());
            return;
        }

        boolean salir = false;
        
        while(!salir) {
            mostrarMenu();

            try {
            	 int opcion = leerEntero("Seleccione una opción: ");

                switch (opcion) {
                    case 1 -> {
                    	String nombre = leerTexto("Nombre: ");
                        String base = leerTexto("Base: ");
                        int cazas = leerEntero("Número de cazas: ");

                        if (nombre.isBlank() || base.isBlank() || cazas < 0) {
                            System.out.println("Datos inválidos. Revise los campos.");
                            return;
                        }

                        EscuadronDTO nuevo = new EscuadronDTO();
                        nuevo.setNombre(nombre);
                        nuevo.setSectorBase(base);
                        nuevo.setNumeroCazas(cazas);

                        dao.crear(nuevo);
                        System.out.println("Escuadrón registrado correctamente.");
                    }

                    case 2 -> {
                    	List<EscuadronDTO> escuadrones = dao.obtenerTodos();

                        if (escuadrones.isEmpty()) {
                            System.out.println("No hay escuadrones registrados.");
                            return;
                        }
                        escuadrones.forEach(System.out::println);
                    }

                    case 3 -> {
                    	int id = leerEntero("ID del escuadrón: ");
                        EscuadronDTO encontrado = dao.buscarPorId(id);

                        System.out.println(encontrado != null ? encontrado : "Escuadrón no encontrado.");
                    }

                    case 4 -> {
                    	int id = leerEntero("ID a actualizar: ");
                        EscuadronDTO existente = dao.buscarPorId(id);

                        if (existente == null) {
                            System.out.println("Escuadrón no encontrado.");
                            return;
                        }

                        String nombre = leerTexto("Nuevo nombre: ");
                        String base = leerTexto("Nueva base: ");
                        int cazas = leerEntero("Nuevo número de cazas: ");

                        if (nombre.isBlank() || base.isBlank() || cazas < 0) {
                            System.out.println("Datos inválidos.");
                            return;
                        }

                        existente.setNombre(nombre);
                        existente.setSectorBase(base);
                        existente.setNumeroCazas(cazas);

                        System.out.println(dao.actualizar(existente)
                                ? "Escuadrón actualizado correctamente."
                                : "No se pudo actualizar el escuadrón.");
                    }

                    case 5 -> {
                    	int id = leerEntero("ID a eliminar: ");

                        System.out.println(dao.eliminar(id)
                                ? "Escuadrón eliminado correctamente."
                                : "Escuadrón no encontrado.");
                    }

                    case 0 -> {
                    	salir = true;
                        System.out.println("Cerrando la terminal HoloNet...");
                    }

                    default -> System.out.println("Opción no válida.");
                }

            } catch (IllegalStateException e) {
                System.err.println("No se pudo completar la operación: " + e.getMessage());
            }
        }

        sc.close();
    }
    
    private static void mostrarMenu() {
        System.out.println("\n===== HOLONET =====");
        System.out.println("1. Registrar escuadrón");
        System.out.println("2. Mostrar todos los escuadrones");
        System.out.println("3. Buscar escuadrón por ID");
        System.out.println("4. Actualizar escuadrón");
        System.out.println("5. Eliminar escuadrón");
        System.out.println("0. Salir");
    }
    
    private static String leerTexto(String mensaje) {
        System.out.print(mensaje);
        return sc.nextLine().trim();
    }

    private static int leerEntero(String mensaje) {
        while (true) {
            try {
                return Integer.parseInt(leerTexto(mensaje));
            } catch (NumberFormatException e) {
                System.out.println("Error: introduzca un número válido.");
            }
        }
    }
}

