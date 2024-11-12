package clase_8_ejercicio_7;

public interface ABBTDA<E extends Comparable<E>> {
	public boolean pertenece( E elemento );
	public void insertar( E elemento );
	public E eliminar( E elemento );
	public String toString();
}
