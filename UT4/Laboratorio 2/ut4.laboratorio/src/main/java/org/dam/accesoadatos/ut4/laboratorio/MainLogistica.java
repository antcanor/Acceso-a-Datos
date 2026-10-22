package org.dam.accesoadatos.ut4.laboratorio;

import org.dam.accesoadatos.ut4.laboratorio.Nave;
import org.dam.accesoadatos.ut4.laboratorio.Planeta;
import org.dam.accesoadatos.ut4.laboratorio.util.HibernateUtil;
import org.hibernate.Session;
import org.hibernate.Transaction;

public class MainLogistica {
	
	public static int parte1(){
		int id = 0;
		Transaction tx = null;
        try (Session session = HibernateUtil.getSessionFactory().openSession()) {
            tx = session.beginTransaction();

            // 1. Creamos el nuevo planeta
            Planeta corelia = new Planeta("Astillero de Corellia","Mundos del Núcleo");
            
            // 2. Creamos las naves en estado transitorio
            Nave n1 = new Nave("Caza TIE", "Caza TIE Básico", 2, "Estable", corelia);
            Nave n2 = new Nave("Caza TIE", "TIE Bomber", 2, "Crítico", corelia);

            // 3. Persistimos todo
            session.persist(corelia); 
            session.persist(n1);
            session.persist(n2);
            
            id = corelia.getId();
            
            tx.commit();
            System.out.println("✔ Flota del sector asignada al planeta astillero de forma automatizada.");
            
        } catch (Exception e) {
            if (tx != null) tx.rollback();
            System.err.println("❌ Fallo en el despliegue orbital: " + e.getMessage());
        } finally {
            HibernateUtil.shutdown();
            System.out.println("==================================================");
        }
        
        return id;
	}
	
	public static void parte2(int id) {
		// Buscamos el Planeta en base de datos
        try (Session session = HibernateUtil.getSessionFactory().openSession()) {
            
            System.out.println("🔍 Recuperando datos del planeta astillero...");
            Planeta planetaDestino = session.get(Planeta.class, id);
            
            if (planetaDestino != null) {
                System.out.println("\n🌍 PLANETA LOCALIZADO: " + planetaDestino.getNombrePlaneta());
                System.out.println("🚀 Sector Espacial: " + planetaDestino.getSectorGalactico());
                
                System.out.println("\n⏳ Cargando flota amarrada en los muelles de este planeta...");
               
                int totalNaves = planetaDestino.getListaNaves().size();
                System.out.println("📈 Total de naves censadas en el hangar: " + totalNaves);
                
                System.out.println("--- Manifiesto de la Flota Desplegada ---");
                for (Nave n : planetaDestino.getListaNaves()) {
                    System.out.println("   » 🛸 Nave: " + n.getNombre() + " | Modelo: " + n.getModelo());
                }
                
            } else {
                System.out.println("❌ No se encontró ningún planeta con el ID "+id+" en la base de datos.");
            }
            
        } catch (Exception e) {
            System.err.println("❌ Error en la exploración de hangares: " + e.getMessage());
        } finally {
            HibernateUtil.shutdown();
            System.out.println("==========================================================");
        }
	}

	public static void main(String[] args) {
		 int id = parte1();
		 
		 parte2(id);
		 

	}

}
