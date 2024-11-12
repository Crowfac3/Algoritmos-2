package clase_8_ejercicio_7;

public class DictionaryABB<K extends Comparable<K>, V extends Comparable<V>> implements Map<K, ABBTDA<V>> {
    private ABBTDA<Entrada<K, ABBTDA<V>>> tree;

    public DictionaryABB() {
        this.tree = new arbolBB<>(new DefaultComparator<Entrada<K, ABBTDA<V>>>());
    }

    // Agrega una clave y un ABB de valores asociados
    @Override
    public ABBTDA<V> put(K key, ABBTDA<V> values) {
        NodoABB<Entrada<K, ABBTDA<V>>> nodo = buscarNodo(key);
        if (nodo != null) {
            ABBTDA<V> valoresExistentes = nodo.getElemento().getValue();
            // Aquí se podría decidir cómo combinar los ABB (e.g., insertar valores)
            return valoresExistentes;
        } else {
            Entrada<K, ABBTDA<V>> entrada = new Entrada<>(key, values);
            tree.insertar(entrada);
            return values;
        }
    }

    // Obtiene los valores asociados a una clave
    @Override
    public ABBTDA<V> get(K key) {
        NodoABB<Entrada<K, ABBTDA<V>>> nodo = buscarNodo(key);
        return nodo != null ? nodo.getElemento().getValue() : null;
    }

    // Elimina una clave y sus valores asociados
    @Override
    public ABBTDA<V> remove(K key) {
        NodoABB<Entrada<K, ABBTDA<V>>> nodo = buscarNodo(key);
        if (nodo != null) {
            Entrada<K, ABBTDA<V>> entradaEliminada = tree.eliminar(nodo.getElemento());
            return entradaEliminada.getValue();
        }
        return null;
    }

    // Buscar nodo por clave
    private NodoABB<Entrada<K, ABBTDA<V>>> buscarNodo(K key) {
        NodoABB<Entrada<K, ABBTDA<V>>> nodo = ((arbolBB<Entrada<K, ABBTDA<V>>>) tree).raiz;
        while (nodo != null && nodo.getElemento() != null) {
            int comparacion = key.compareTo(nodo.getElemento().getKey());
            if (comparacion == 0) {
                return nodo;
            } else if (comparacion < 0) {
                nodo = nodo.getIzq();
            } else {
                nodo = nodo.getDer();
            }
        }
        return null;
    }

    @Override
    public int size() {
        return calcularTamaño(((arbolBB<Entrada<K, ABBTDA<V>>>) tree).raiz);
    }

    // Método auxiliar para calcular el tamaño del ABB recursivamente
    private int calcularTamaño(NodoABB<Entrada<K, ABBTDA<V>>> nodo) {
        if (nodo == null || nodo.getElemento() == null) {
            return 0;
        }
        return 1 + calcularTamaño(nodo.getIzq()) + calcularTamaño(nodo.getDer());
    }

    @Override
    public boolean isEmpty() {
        return size() == 0;
    }

    @Override
    public K[] keys() {
        // Implementar si es necesario
        return null;
    }

    @Override
    public ABBTDA<V>[] values() {
        // Implementar si es necesario
        return null;
    }

    @Override
    public Entry<K, ABBTDA<V>>[] entries() {
        // Implementar si es necesario
        return null;
    }
}

