package org.dam.accesoadatos.ut4.pruebas;

import org.hibernate.Session;
import org.dam.accesoadatos.ut4.Nave;
import org.dam.accesoadatos.ut4.Planeta;
import org.dam.accesoadatos.ut4.util.HibernateUtil;

public class TestUnoMuchos {
	public static void main(String[] args) {
        System.out.println("======= CONSULTA DE INVENTARIO CENTRAL DE PLANETAS =======");

        // Buscaremos el Planeta con ID 1 (El astillero que guardamos en la sesión anterior)
        try (Session session = HibernateUtil.getSessionFactory().openSession()) {
            
            System.out.println("🔍 Recuperando datos del planeta astillero...");
            Planeta planetaDestino = session.get(Planeta.class, 1);
            
            if (planetaDestino != null) {
                System.out.println("\n🌍 PLANETA LOCALIZADO: " + planetaDestino.getNombrePlaneta());
                System.out.println("🚀 Sector Espacial: " + planetaDestino.getSectorGalactico());
                
                System.out.println("\n⏳ Cargando flota amarrada en los muelles de este planeta...");
                // ¡OJO ALUMNOS!: Al llamar al método size() o iterar la lista, Hibernate activa la carga
                // y lanza de forma automática el SELECT secundario contra PostgreSQL de forma perezosa (LAZY).
                int totalNaves = planetaDestino.getListaNaves().size();
                System.out.println("📈 Total de naves censadas en el hangar: " + totalNaves);
                
                System.out.println("--- Manifiesto de la Flota Desplegada ---");
                for (Nave n : planetaDestino.getListaNaves()) {
                    System.out.println("   » 🛸 Nave: " + n.getNombre() + " | Modelo: " + n.getModelo());
                }
                
            } else {
                System.out.println("❌ No se encontró ningún planeta con el ID 1 en la base de datos.");
            }
            
        } catch (Exception e) {
            System.err.println("❌ Error en la exploración de hangares: " + e.getMessage());
        } finally {
            HibernateUtil.shutdown();
            System.out.println("==========================================================");
        }
    }
}

