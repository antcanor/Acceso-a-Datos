package com.alianzarebelde.holonet;

/**
 *
 * @author Antonio Cano Ruiz
 */
public class EscuadronDTO {
    private int idEscuadron;
    private String nombre;
    private String sectorBase;
    private int numeroCazas;
    
    public EscuadronDTO(){}

    public EscuadronDTO(int idEscuadron, String nombre, String sectorBase, int numeroCazas) {
        this.idEscuadron = idEscuadron;
        this.nombre = nombre;
        this.sectorBase = sectorBase;
        this.numeroCazas = numeroCazas;
    }

    public int getIdEscuadron() {
        return idEscuadron;
    }

    public void setIdEscuadron(int idEscuadron) {
        this.idEscuadron = idEscuadron;
    }

    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public String getSectorBase() {
        return sectorBase;
    }

    public void setSectorBase(String sectorBase) {
        this.sectorBase = sectorBase;
    }

    public int getNumeroCazas() {
        return numeroCazas;
    }

    public void setNumeroCazas(int numeroCazas) {
        this.numeroCazas = numeroCazas;
    }

    @Override
    public String toString() {
        return "EscuadronDTO{" + "idEscuadron=" + idEscuadron + 
                ", nombre=" + nombre + ", sectorBase=" + sectorBase + 
                ", numeroCazas=" + numeroCazas + '}';
    }
    
    
    
}
