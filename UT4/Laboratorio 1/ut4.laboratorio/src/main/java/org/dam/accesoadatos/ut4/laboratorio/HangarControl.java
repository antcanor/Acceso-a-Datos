package org.dam.accesoadatos.ut4.laboratorio;

import org.hibernate.Session;
import org.hibernate.Transaction;
import org.hibernate.query.Query;

import java.util.List;

import org.dam.accesoadatos.ut4.laboratorio.Nave;
import org.dam.accesoadatos.ut4.laboratorio.util.HibernateUtil;

public class HangarControl {
	
	public static void registrarNuevaNave(Nave nave) {
		if(nave == null) {
			System.out.println("❌ El atributo nave no puedo ser nulo.");
			return;
		}
		
		try (Session session = HibernateUtil.getSessionFactory().openSession()) {
			Transaction tx = null;
            try {
            	tx = session.beginTransaction();
                System.out.println("⏳ Persistiendo la nave en la base de datos...");
                
                session.persist(nave);

                tx.commit();
                
                System.out.println("✔ Transmisión guardada con éxito.");
                System.out.println("🚀 ID generado automáticamente por PostgreSQL: " + nave.getId());
                System.out.println(nave);
                
            } catch (Exception e) {
                if (tx != null) tx.rollback();
                System.err.println("Error en la modificación: " + e.getMessage());
            }
            
        } 
	}
	
	public static void actualizarEstadoNave(int idNave, String nuevoEstado) {
		try (Session session = HibernateUtil.getSessionFactory().openSession()) {
            Nave naveRecuperada = session.get(Nave.class, idNave);
            
            if (naveRecuperada != null) {
                System.out.println("✔ Nave localizada en el hangar: " + naveRecuperada);
                
                Transaction tx = null;
                try {
                    tx = session.beginTransaction();
                    
                    System.out.println("\n⚙ 2. Modificando estado del sistema a '"+nuevoEstado+"' ...");
                    
                    naveRecuperada.setEstadoSistema(nuevoEstado);
                    
                    tx.commit();
                    System.out.println("✔ Base de datos actualizada dinámicamente.");
                    
                } catch (Exception e) {
                    if (tx != null) tx.rollback();
                    System.err.println("Error en la modificación: " + e.getMessage());
                }
                
            } else {
                System.out.println("❌ No se encontró ninguna nave con el ID especificado.");
            }
        }
	}
	
	public static List<Nave> obtenerCazasPorModelo(String modeloBuscado){
		List<Nave> naves = null;
        System.out.println("\nFiltrando naves por modelo [" + modeloBuscado + "]...");
        
        try (Session session = HibernateUtil.getSessionFactory().openSession()) {
            String hqlFiltro = "FROM Nave n WHERE n.modelo = :modeloRef";
            
            Query<Nave> queryFiltro = session.createQuery(hqlFiltro, Nave.class);
            
            queryFiltro.setParameter("modeloRef", modeloBuscado);
            
            naves = queryFiltro.getResultList();
            
            System.out.println("--- Reporte del Filtrado ---");
            if (!naves.isEmpty()) {
                for (Nave n : naves) {
                    System.out.println("⚠ OBJETIVO -> ID: " + n.getId() 
                                     + " | Modelo: " + n.getModelo() 
                                     + " | Nombre: " + n.getNombre());
                }
            } else {
                System.out.println("ℹ No existen naves de ese modelo.");
            }
            
        } catch (Exception e) {
            System.err.println("❌ Error en el filtrado perimetral HQL: " + e.getMessage());
        }
        
        return naves;
	}
	
	public static void main(String[] args) {
		try {
            Nave n = new Nave("TIE Interceptor", "TI-v2", 1, "Critico");
            registrarNuevaNave(n);

            actualizarEstadoNave(n.getId(), "Estable");

            obtenerCazasPorModelo("TI-v2");
        } finally {
        	HibernateUtil.shutdown();
        }
		
	}
	
	
	
	

}
