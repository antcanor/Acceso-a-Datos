package org.dam.accesodatos.ut4.examen.services;

import org.dam.accesodatos.ut4.examen.models.CazaLigero;
import org.dam.accesodatos.ut4.examen.models.DestructorEstelar;
import org.dam.accesodatos.ut4.examen.models.Nave;
import org.hibernate.*;
import org.dam.accesodatos.ut4.examen.util.HibernateUtil;
import org.hibernate.query.Query;

import java.util.Collections;
import java.util.List;

public class HoloNetService {

    public List<CazaLigero> obtenerCazasOperativosPorBando(String bando){
        try (Session session = HibernateUtil.getSessionFactory().openSession()) {

            // HQL interactúa con la clase CazaLigero y su atributo, no con las tablas SQL
            String hql = "SELECT n FROM CazaLigero n " +
                    "INNER JOIN n.planetaOrigen p " +
                    "WHERE TYPE(n) = CazaLigero " +
                    "AND p.afiliacion = :bando " +
                    "AND n.estadoSistema <> :estadoMantenimiento";

            Query<CazaLigero> query = session.createQuery(hql, CazaLigero.class);
            query.setParameter("bando", bando);
            query.setParameter("estadoMantenimiento", "Mantenimiento");

            return query.list();

        } catch (Exception e) {
            System.err.println("❌ Error al consultar los cazas: " + e.getMessage());
            return Collections.emptyList();
        }
    }

    public List<Nave> obtenerFlotaCriticaPolimorfica(){
        try (Session session = HibernateUtil.getSessionFactory().openSession()) {
            // Consulta polimórfica (sobre Nave) que precarga el planeta con FETCH
            String hql = "FROM Nave n " +
                    "INNER JOIN FETCH n.planetaOrigen p " +
                    "WHERE n.estadoSistema = :estadoMantenimiento";

            Query<Nave> query = session.createQuery(hql, Nave.class);
            query.setParameter("estadoMantenimiento", "Critico");

            return query.list();

        } catch (Exception e) {
            System.err.println("❌ Error al obtener flota: " + e.getMessage());
            return Collections.emptyList();
        }
    }

    public List<Object[]> obtenerReporteGeneralFiltrado(){
        try (Session session = HibernateUtil.getSessionFactory().openSession()) {

            String hql = "SELECT n.nombre, TYPE(n), p.nombre " +
                    "FROM Nave n " +
                    "LEFT JOIN n.planetaOrigen p";

            Query<Object[]> query = session.createQuery(hql, Object[].class);

            return query.list();

        } catch (Exception e) {
            System.err.println("❌ Error al generar el reporte: " + e.getMessage());
            return Collections.emptyList();
        }
    }




    public void registrarNave(Nave nave) {
        Transaction tx = null;
        try (Session session = HibernateUtil.getSessionFactory().openSession()) {
            tx = session.beginTransaction();

            session.persist(nave); // Funciona para CazaTIE o DestructorEstelar

            tx.commit();
            System.out.println("✔ Nave registrada correctamente: " + nave.getNombre());
        } catch (Exception e) {
            if (tx != null && tx.isActive()) {
                tx.rollback();
            }
            System.err.println("❌ Error al registrar la nave: " + e.getMessage());
        }
    }

    public void actualizarEstadoDestructor(int id, int nuevosEscudos) {
        Transaction tx = null;
        try (Session session = HibernateUtil.getSessionFactory().openSession()) {
            tx = session.beginTransaction();

            // Recuperamos el objeto, que pasa a estado "Persistent"
            DestructorEstelar destructor = session.get(DestructorEstelar.class, id);

            if (destructor != null) {
                // Al modificarlo mediante el setter, Hibernate detecta el cambio automáticamente
                destructor.setCapacidadEscudos(nuevosEscudos);
                System.out.println("✔ Escudos actualizados en memoria para: " + destructor.getNombre());
            } else {
                System.out.println("⚠ No se encontró un Destructor con ID: " + id);
            }

            // El commit realiza el UPDATE automático en base de datos si hubo cambios
            tx.commit();
        } catch (Exception e) {
            if (tx != null && tx.isActive()) {
                tx.rollback();
            }
            System.err.println("❌ Error al actualizar el destructor: " + e.getMessage());
        }
    }

    public List<CazaLigero> obtenerCazasPorManiobra(int potenciaFuego) {
        try (Session session = HibernateUtil.getSessionFactory().openSession()) {

            // HQL interactúa con la clase CazaTIE y su atributo, no con las tablas SQL
            String hql = "FROM CazaLigero c WHERE c.potenciaFuego >= :minimo";

            Query<CazaLigero> query = session.createQuery(hql, CazaLigero.class);
            query.setParameter("minimo", potenciaFuego); // Parámetro con nombre

            return query.list();

        } catch (Exception e) {
            System.err.println("❌ Error al consultar los cazas: " + e.getMessage());
            return Collections.emptyList();
        }
    }
}
