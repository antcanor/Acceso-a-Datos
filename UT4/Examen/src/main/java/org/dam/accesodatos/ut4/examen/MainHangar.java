package org.dam.accesodatos.ut4.examen;

import org.dam.accesodatos.ut4.examen.models.CazaLigero;
import org.dam.accesodatos.ut4.examen.models.Nave;
import org.dam.accesodatos.ut4.examen.services.HoloNetService;
import org.dam.accesodatos.ut4.examen.util.HibernateUtil;
import org.hibernate.Session;
import org.hibernate.Transaction;
import java.util.List;

public class MainHangar {

    public static void main(String[] args) {

        System.out.println("=== INICIO PRUEBAS ===\n");


        HoloNetService servicio = new HoloNetService();

        System.out.println("--- 1. Obtener Cazas Operativos Por Bando ---");
        List<CazaLigero> cazasNeutral = servicio.obtenerCazasOperativosPorBando("Neutral");
        List<CazaLigero> cazaImperio = servicio.obtenerCazasOperativosPorBando("Imperio");
        List<CazaLigero> cazaAlianza = servicio.obtenerCazasOperativosPorBando("Alianza Rebelde");

        System.out.println("\t Cazas Bando NEUTRAL : ");
        for (CazaLigero c : cazasNeutral){
            System.out.println("\t\t "+c);
        }

        System.out.println("\t Cazas Bando IMPERIO :");
        for (CazaLigero c : cazaImperio){
            System.out.println("\t\t "+c);
        }

        System.out.println("\t Cazas Bando ALIANZA REBELDE :");
        for (CazaLigero c : cazaAlianza){
            System.out.println("\t\t "+c);
        }

        System.out.println("\n\n--- 2. Obtener Flota Crítica Polimórfica ---");

        List<Nave> flota = servicio.obtenerFlotaCriticaPolimorfica();
        for(Nave n : flota){
            System.out.println("\t "+ n);
        }

        System.out.println("\n\n--- 3. Obtener Reporte General ---");
        List<Object[]> reporte = servicio.obtenerReporteGeneralFiltrado();

        for (Object[] fila : reporte) {
            System.out.println("\t " + java.util.Arrays.toString(fila));
        }




        HibernateUtil.shutdown();
        System.out.println("\n=== FIN DE LA EJECUCIÓN ===");
    }
}
