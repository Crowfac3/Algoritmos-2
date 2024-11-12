package clase_8_ejercicio_7;

public interface Map<K,V> { 
	public int size(); 
	public boolean isEmpty(); 
	public V get(K k); 
	public V put(K k, V v); 
	public V remove(K k); 
	public K[] keys(); 
	public V[] values(); 
	public Entry<K,V>[] entries(); 
}
