package clase_8_ejercicio_7;

public class NodoABB<E extends Comparable<E>> {
	private E elemento;
	private NodoABB<E> padre, izq, der;
	
	public NodoABB( E element, NodoABB<E> padre ) {
	this.elemento = element;
	this.padre = padre;
	izq = der = null;
	}
	public E getElemento() { return elemento; }
	public NodoABB<E> getPadre() { return padre; }
	public NodoABB<E> getIzq() { return izq; }
	public NodoABB<E> getDer() { return der; }
	public void setElemento( E element ) { this.elemento = element; }
	public void setIzq( NodoABB<E> izq ) { this.izq = izq; }
	public void setDer( NodoABB<E> der ) { this.der = der; }
	public void setPadre( NodoABB<E> padre ) { this.padre = padre; }
}
