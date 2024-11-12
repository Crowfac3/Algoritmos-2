package clase_8_ejercicio_7;

import java.util.Comparator;

public class Main {
    public static void main(String[] args) {
        try {
            // Crear un diccionario con claves y valores usando ABB
            DictionaryABB<String, Integer> dictionary = new DictionaryABB<>();

            // Crear comparador para el ABB de valores
            Comparator<Integer> valueComparator = new DefaultComparator<>();

            // Crear ABB para los valores asociados a la clave "A"
            ABBTDA<Integer> abbA = new arbolBB<>(valueComparator);
            abbA.insertar(10);
            abbA.insertar(20);
            abbA.insertar(30);
            
            // Agregar el ABB de valores al diccionario con clave "A"
            dictionary.put("A", abbA);

            // Crear ABB para los valores asociados a la clave "B"
            ABBTDA<Integer> abbB = new arbolBB<>(valueComparator);
            abbB.insertar(15);
            abbB.insertar(25);
            abbB.insertar(35);

            // Agregar el ABB de valores al diccionario con clave "B"
            dictionary.put("B", abbB);

            // Obtener y mostrar los valores para la clave "A"
            ABBTDA<Integer> valuesA = dictionary.get("A");
            System.out.println("Valores para la clave 'A': " + (valuesA != null ? valuesA.toString() : "null"));

            // Obtener y mostrar los valores para la clave "B"
            ABBTDA<Integer> valuesB = dictionary.get("B");
            System.out.println("Valores para la clave 'B': " + (valuesB != null ? valuesB.toString() : "null"));

            // Mostrar el tamaño del diccionario
            System.out.println("Tamaño del diccionario: " + dictionary.size());

            // Eliminar la clave "A" y mostrar el tamaño del diccionario actualizado
            dictionary.remove("A");
            System.out.println("Tamaño del diccionario después de eliminar 'A': " + dictionary.size());
        } catch (Exception e) {
            System.out.println("Se produjo un error: " + e.getMessage());
            e.printStackTrace();
        }
    }
}
