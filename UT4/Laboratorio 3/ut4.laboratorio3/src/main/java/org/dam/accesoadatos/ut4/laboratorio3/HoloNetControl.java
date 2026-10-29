package org.dam.accesoadatos.ut4.laboratorio3;

import java.util.List;

import org.dam.accesoadatos.ut4.laboratorio3.util.HibernateUtil;
import org.hibernate.Session;
import org.hibernate.query.Query;

public class HoloNetControl {
	
	public static List<Nave> obtenerNavesPorBandoPlaneta(String bando){
	   String hql = "FROM Nave n INNER JOIN n.planetaOrigen p "
	               + "WHERE p.afiliacion = :bandoRef "
	               + "AND n.estadoSistema != 'Mantenimiento'";
	    
	    try (Session session = HibernateUtil.getSessionFactory().openSession()) {
	        Query<Nave> query = session.createQuery(hql, Nave.class);
	        query.setParameter("bandoRef", bando);
	        return query.getResultList();
	    }
		
	}
	
	public static List<Nave> obtenerFlotaCriticaConPlaneta(){
		 // FETCH JOIN fuerza la carga inmediata del objeto relacionado en memoria
	    String hql = "FROM Nave n INNER JOIN FETCH n.planetaOrigen WHERE n.estadoSistema = 'Critico'";
	    
	    try (Session session = HibernateUtil.getSessionFactory().openSession()) {
	        return session.createQuery(hql, Nave.class).getResultList();
	    }
	}

	public static List<Object[]> obtenerReportePlanetasAsignados(){
		String hql = "SELECT n.nombre, p.nombre FROM Nave n LEFT JOIN n.planetaOrigen p";
	    
	    try (Session session = HibernateUtil.getSessionFactory().openSession()) {
	        Query<Object[]> query = session.createQuery(hql, Object[].class);
	        return query.getResultList();
	    }
	}
	
	public static void main(String[] args) {
		
		List<Nave> naves = obtenerNavesPorBandoPlaneta("Imperio");
		for(Nave n : naves) {
			System.out.println(n);
		}
		
		List<Nave> flotaCtitica = obtenerFlotaCriticaConPlaneta();
		for(Nave n : flotaCtitica) {
			System.out.println(n + " | "+n.getPlanetaOrigen());
		}
		
		List<Object[]> reporte = obtenerReportePlanetasAsignados();
		for(Object[] fila : reporte) {
			String nombreNave = (String) fila[0];
		    String nombrePlaneta = (String) fila[1];
		    System.out.println("Nave: " + nombreNave + " | Planeta: " + nombrePlaneta);
		}
		
		
	}

}
