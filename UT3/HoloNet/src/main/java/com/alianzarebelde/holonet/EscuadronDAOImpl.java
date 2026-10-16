package com.alianzarebelde.holonet;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.Statement;
import java.sql.SQLException;
import java.util.ArrayList;
import java.util.List;


/**
 *
 * @author Antonio Cano Ruiz
 */
public class EscuadronDAOImpl implements EscuadronDAO{
    
    private static final String URL= "jdbc:postgresql://localhost:5432/db_imperial";
    private static final String USER= "antonio";
    private static final String PASS = "admin";
    
    public EscuadronDAOImpl() {
        inicializarTabla();
    }
    
    private void inicializarTabla() {
        String sql = "CREATE TABLE IF NOT EXISTS escuadrones_imperiales (" +
            "idEscuadron SERIAL PRIMARY KEY, " +
            "nombre VARCHAR(100) NOT NULL, " +
            "sectorBase VARCHAR(100) NOT NULL, " +
            "numeroCazas INTEGER NOT NULL " +
            ")";
        
        try(Connection con = DriverManager.getConnection(URL, USER,PASS);Statement stmt = con.createStatement()){
            stmt.execute(sql);
            System.out.println("Tabla HoloNet creada correctamente.");
        }catch (SQLException e) {
            System.err.println("Error en la conexión a la HoloNet: " +e);
        }
    }
    
    @Override
    public void crear(EscuadronDTO escuadron) {
        String sql =
            "INSERT INTO escuadrones_imperiales " +
            "(nombre, sectorBase, numeroCazas) " +
            "VALUES (?, ?, ?)";
        
        try (Connection con = DriverManager.getConnection(URL, USER,PASS);
             PreparedStatement ps = con.prepareStatement(sql)) {

            ps.setString(1, escuadron.getNombre());
            ps.setString(2, escuadron.getSectorBase());
            ps.setInt(3, escuadron.getNumeroCazas());
            
            ps.execute();

            //System.out.println("Escuadrón creado correctamente.");
        } catch (SQLException e) {
            System.err.println("Error al crear el Escuadron: " +e);
        }
    }
    
    @Override
    public List<EscuadronDTO> obtenerTodos() {
        List<EscuadronDTO> lista = new ArrayList<>();

        String sql =
            "SELECT idEscuadron, nombre, sectorBase, numeroCazas " +
            "FROM escuadrones_imperiales ORDER BY idEscuadron";

        try (Connection con = DriverManager.getConnection(URL, USER,PASS);
             PreparedStatement ps = con.prepareStatement(sql);
             ResultSet rs = ps.executeQuery()) {

            while (rs.next()) {
                EscuadronDTO escuadron = new EscuadronDTO(
                    rs.getInt("idEscuadron"),
                    rs.getString("nombre"),
                    rs.getString("sectorBase"),
                    rs.getInt("numeroCazas")
                );

                lista.add(escuadron);
            }

        } catch (SQLException e) {
            System.err.println("Error al traer todos los escuadrones: " +e);
        }

        return lista;
    }
    
    @Override
    public EscuadronDTO buscarPorId(int id){
        String sql =
            "SELECT nombre, sectorBase, numeroCazas " +
            "FROM escuadrones_imperiales WHERE idEscuadron = ?";
        try (Connection con = DriverManager.getConnection(URL, USER,PASS);PreparedStatement ps = con.prepareStatement(sql);) {
            ps.setInt(1, id);
            
            try (ResultSet rs = ps.executeQuery()) {
                if (rs.next()) {
                    return new EscuadronDTO(
                        id,
                        rs.getString("nombre"),
                        rs.getString("sectorBase"),
                        rs.getInt("numeroCazas")
                    );
                }
            }

        } catch (SQLException e) {
            System.err.println("Error al buscar Escuadron: " +e);
        }

        return null;
    }
      
    @Override
    public boolean actualizar(EscuadronDTO escuadron) {
        String sql =
            "UPDATE escuadrones_imperiales SET " +
            "nombre = ?, sectorBase = ?, numeroCazas = ? " +
            "WHERE idEscuadron = ?";

        try (Connection con = DriverManager.getConnection(URL, USER,PASS);PreparedStatement ps = con.prepareStatement(sql);){

            ps.setString(1, escuadron.getNombre());
            ps.setString(2, escuadron.getSectorBase());
            ps.setInt(3, escuadron.getNumeroCazas());
            ps.setInt(4, escuadron.getIdEscuadron());

            return ps.executeUpdate()> 0;

        } catch (SQLException e) {
            System.err.println("Error al buscar Escuadron: " +e);
        }
        return false;
    }
    
    @Override
    public boolean eliminar(int id) {
        String sql =
            "DELETE FROM escuadrones_imperiales WHERE idEscuadron = ?";

        try (Connection con = DriverManager.getConnection(URL, USER,PASS);PreparedStatement ps = con.prepareStatement(sql);) {

            ps.setInt(1, id);

            return ps.executeUpdate()> 0;

        } catch (SQLException e) {
            System.err.println("Error al eliminar Escuadron: " +e);
        }
        return false;
    }
    
}
