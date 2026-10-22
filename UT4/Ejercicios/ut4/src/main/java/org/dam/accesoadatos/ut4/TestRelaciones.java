package org.dam.accesoadatos.ut4;

import org.hibernate.Session;
import org.hibernate.Transaction;
import org.dam.accesoadatos.ut4.Nave;
import org.dam.accesoadatos.ut4.Planeta;
import org.dam.accesoadatos.ut4.util.HibernateUtil;

public class TestRelaciones {
	public static void main(String[] args) {
        System.out.println("======= ASIGNACIÓN DE LOGÍSTICA COORDENADA =======");

        Transaction tx = null;
        try (Session session = HibernateUtil.getSessionFactory().openSession()) {
            tx = session.beginTransaction();

            // 1. Creamos el registro del Planeta base (Estado Transitorio)
            Planeta kuat = new Planeta("Astillero de Kuat", "Mundos del Núcleo");
            session.persist(kuat); // Al persistirlo, entra en estado Gestionado y obtiene un ID real de Postgres
            
            System.out.println("✔ Planeta base registrado de forma persistente: " + kuat);

            // 2. Creamos las naves asociándoles el objeto del planeta directamente en memoria
            Nave destructor1 = new Nave("Devastador", "Destructor Estelar Clase I", 9000, "Estable", kuat);
            Nave destructor2 = new Nave("Quimera", "Destructor Estelar Clase I", 9000, "Estable", kuat);

            // 3. Persistimos las naves
            // ¡OJO ALUMNOS!: Hibernate extraerá automáticamente el ID de 'kuat' y lo meterá como FK en la tabla naves.
            session.persist(destructor1);
            session.persist(destructor2);

            tx.commit();
            System.out.println("✔ Flota del sector asignada al planeta astillero de forma automatizada.");
            
        } catch (Exception e) {
            if (tx != null) tx.rollback();
            System.err.println("❌ Fallo en el despliegue orbital: " + e.getMessage());
        } finally {
            HibernateUtil.shutdown();
            System.out.println("==================================================");
        }
    }
}

