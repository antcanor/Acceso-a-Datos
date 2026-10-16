package com.alianzarebelde.holonet;

import java.util.List;
/**
 *
 * @author Antonio Cano Ruiz
 */
public interface EscuadronDAO {
    void crear(EscuadronDTO escuadron);
    
    List<EscuadronDTO> obtenerTodos();
    
    EscuadronDTO buscarPorId(int id);
    
    boolean actualizar(EscuadronDTO escuadron);
    
    boolean eliminar(int id);
    
}
