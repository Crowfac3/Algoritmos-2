
//#######################
//##### MYEXCEPTION #####
//#######################


public class MyException extends RuntimeException{
	/**
	 * 
	 */
	private static final long serialVersionUID = 1L;

	public MyException(String s){
		super(s);
	}
}




//################
//##### NODO #####
//################

public class Node<E> {
	private E element;
	private Node<E> next;
	//constructores
	public Node(E newElement, Node<E> n){
		element=newElement; 
		next=n;
	}
	public Node(E newElement){
		element=newElement; 
		next=null;
	}
	public Node(){
		element=null; 
		next=null;
	}
	//metodos
	public E getElement(){
		return element;
	}
	public Node<E> getNext(){
		return next;
	}
	public void setElement(E newElement){
		element=newElement;
	}
	public void setNext(Node<E> n){
		next=n;
	}
}

//#################
//##### STACK #####
//#################

public interface Stack<E> {
	public void push(E item);
	public E pop();
	public E top();
	public boolean isEmpty();
	public int size();
}

//#######################
//##### ARRAY STACK #####
//#######################

public class ArrayStack<E> implements Stack<E> {
	private E[] array;
    private int size;
    @SuppressWarnings("unchecked")
	public ArrayStack() {
        array = (E[]) new Object[10];
        size = 0;
    }
    @SuppressWarnings("unchecked")
	public ArrayStack(int initialSize) {
        array = (E[]) new Object[initialSize];
        size = 0;
    }

    public void push(E element) {
    	//Podría generar una excepción si se alcanza la capacidad máxima del arreglo
        if (size == array.length) {
            resizeArray();
        }
        array[size] = element;
        size++;
    }
    private void resizeArray() {
        @SuppressWarnings("unchecked")
		E[] newArray = (E[]) new Object[2 * array.length];
        for (int i = 0; i < array.length; i++) {
            newArray[i] = array[i];
        }
        array = newArray;
    }

    public E pop() {
        if (size == 0)
            throw new MyException("La pila está vacía, no puedo desapilar un elemento");
        E top = array[size - 1];
        array[size - 1] = null;
        size--;
        return top;
    }

    public E top() {
        if (size == 0)
            throw new MyException("No se puede ver el primer elemento porque la pila está vacía");
        E top = array[size - 1];
        return top;
    }
    
    public boolean isEmpty() {
    	return size==0;
    }

    public int size() {
        return size;
    }
}

//########################
//##### LINKED STACK #####
//########################


public class LinkedStack<E> implements Stack<E>{
	private Node<E> top;
    private int size;
    public LinkedStack() {
        top = null;
        size = 0;
    }
    
    public void push(E element) {
    	Node<E> newNode = new Node<E>(element, top);
        top = newNode;
        size++;
    }

    public E pop() {
        if (size == 0)
            throw new MyException("La pila está vacía, no puedo desapilar un elemento");
        Node<E> oldTop = top;
        top = oldTop.getNext();
        oldTop.setNext(null);
        size--;
        return oldTop.getElement();
    }

    public E top() {
        if (size == 0)
            throw new MyException("No se puede ver el primer elemento porque la pila está vacía");
        return top.getElement();
    }
    
    public boolean isEmpty() {
    	return size==0;
    }

    public int size() {
        return size;
    }
}


//################
//##### LIST #####
//################


public interface List<E>{
	public void addFirst(E newElement);
	public void addLast(E newElement);
	public void removeFirst()throws MyException;
	public void removeLast()throws MyException;
	public void remove(E element)throws MyException;
	public void First();
	public void advance();
	public E getCurrent();
	public boolean atEnd();
	public int getSize();
}


//#######################
//##### LINKED LIST #####
//#######################

public class LinkedList<E> implements List<E> {
	private Node<E> head;
	private int size;
	private Node<E> current;
	//constructor
	public LinkedList(){
		head=null; 
		size=0;
	}
	public void addFirst(E newElement){
		Node<E> n=new Node<E>(newElement);
		n.setNext(head);
		head=n;
		size++;
	}
	
	public void addLast(E newElement){
		Node<E> n=new Node<E>(newElement);
		if(head==null)
			head=n;
		else{
			Node<E> i=head;
			while(i.getNext()!=null)
				i=i.getNext();
			i.setNext(n);
		}
		size++;
	}

	public void removeFirst()throws MyException{
		if(head==null)
			throw new MyException("La lista está vacia, no se puede eliminar primero");
		Node<E> aux=head.getNext();
		head.setNext(null);
		head=aux;
		size--;
	}
	
	public void removeLast()throws MyException{
		if(head==null)
			throw new MyException("La lista está vacia, no se puede eliminar ultimo");
		if(size==1)
			head=null;
		else{
			Node<E> aux=head;
			Node<E> aux2=aux.getNext();
			while(aux2.getNext()!=null){aux=aux2;aux2=aux2.getNext();}
			aux.setNext(null);
		}
		size--;
	}
	
	public void remove(E element)throws MyException{
		if(head==null)
			throw new MyException("La lista está vacia, no se puede eliminar");
		if(element.equals(head.getElement()))
			removeFirst();
		Node<E> aux=head;
		while(aux!=null && !aux.getNext().getElement().equals(element)) 
			aux=aux.getNext();
		if(aux==null)
			throw new MyException("El elemento no pertenece a la lista, no se puede eliminar");
		Node<E> aEliminar = aux.getNext();
		aux.setNext(aEliminar.getNext());
		aEliminar.setNext(null);
		size--;
	}
	
	public void removeAll(E element)throws MyException{
		if(head==null)
			throw new MyException("La lista está vacia, no se puede eliminar");
		Node<E> aux=head;
		while(aux!=null) 
		{
			if(aux.getElement().equals(element))
				remove(element);
			aux=aux.getNext();
		}
		
	}
	
	public void First(){current=head;}
	
	public void advance()throws MyException{
		if(current==null)
			throw new MyException("Fuera de lista");
		else
			current=current.getNext();
	}
	
	public E getCurrent()throws MyException{
		if(current==null)
			throw new MyException("No se puede devolver el nodo actual porque es nulo");
		return current.getElement();
	}
	
	public boolean atEnd(){return current==null;}
	
	public int getSize() {
		return size;
	}
	
	public E elementAt(int pos) {
		if(pos>size) {
			throw new MyException("El índice está fuera del rango de la lista");
		}
		Node<E> aux=head;
		int contador=0;
		while(contador<pos) {
			aux=aux.getNext();
			contador++;
		}
		return aux.getElement();
	}
	
	public void removeAt(int pos) {
		if(pos>size) {
			throw new MyException("El índice está fuera del rango de la lista");
		}
		if(size==1)
			head=null;
		Node<E> aux=head;
		int contador=0;
		while(contador<pos-1) {
			aux=aux.getNext();
			contador++;
		}
		Node<E> aEliminar = aux.getNext();
		aux.setNext(aEliminar.getNext());
		aEliminar.setNext(null);
		size--;
	}
	
}



//#################
//##### ENTRY #####
//#################


public interface Entry <K,V> { 
	public K getKey(); 
	public V getValue(); 
	public void setValue(V v);
	public void setKey(K k);
}

//###################
//##### ENTRADA #####
//###################

public class Entrada<K,V> implements Entry<K,V> {
	 private K clave;
	 private V valor;
	 public Entrada(K k, V v) { clave = k; valor = v; }
	 public K getKey() { return clave; }
	 public V getValue() { return valor; }
	 public void setKey( K k ) { clave = k; }
	 public void setValue(V v) { valor = v; }
	 public String toString( ) {
		 return "(" + getKey() + "," + getValue() + ")" ;
	 }
}

//###############
//##### MAP #####
//###############


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


//#####################
//##### ARRAY MAP #####
//#####################

public class ArrayMap<K,V> implements Map<K,V> {
	
	private Entry<K,V>[] array;
	private int size;
	
	public ArrayMap() {
		array = (Entry<K,V>[])new Entrada[100];
		size = 0;
	}
	
	public V remove(K k) {
		int i=0;
		boolean encontreClave=false;
		while(!encontreClave && i<size) {
			if(array[i].getKey().equals(k))
				encontreClave=true;
			else
				i++;
		}
		if(!encontreClave)
			return null;
		else {
			V auxiliar = array[i].getValue();
			array[i] = array[size-1];
			size--;
			return auxiliar;
		}
	}
	
	public V get(K k) {
		int i=0;
		boolean encontreClave=false;
		while(!encontreClave && i<size) {
			if(array[i].getKey()==k)
				encontreClave=true;
			else
				i++;
		}
		if(!encontreClave)
			return null;
		else {
			return array[i].getValue();
		}
	}
	
	public V put(K k, V v) {
		int i=0;
		boolean encontreClave=false;
		while(!encontreClave && i<size) {
			if(array[i].getKey().equals(k))
				encontreClave=true;
			else
				i++;
		}
		if(!encontreClave) {
			if(size<array.length) {
				array[size] = new Entrada(k,v);
				size++;
				return null;
			}
			else
				throw new MyException("El arreglo está lleno");
		}
		else {
			V auxiliar = array[i].getValue();
			array[i].setValue(v);
			return auxiliar;
		}
	}
	
	public int size() {return size;}
	public boolean isEmpty(){return size==0;}
	
	public Entry<K,V>[] entries(){
		Entry<K,V>[] auxArray = (Entry<K,V>[])new Entrada[size];
		for(int i=0;i<size;i++)
			auxArray[i]=new Entrada(array[i].getKey(),array[i].getValue());
		return auxArray;
	}
	
	
		
	public K[] keys() {
		//me creo un arreglo auxiliar
		K[] aux = (K[])new Object[size];
		//recorro array pidiendo las claves
		for(int i=0;i<size;i++)
		//las agrego a auxiliar
			aux[i]=array[i].getKey();
		//devuelvo auxiliar
		return aux;
	}
	
	public V[] values() {
		//me creo un arreglo auxiliar
		V[] aux = (V[])new Object[size];
		//recorro array pidiendo las claves
		for(int i=0;i<size;i++)
		//las agrego a auxiliar
			aux[i]=array[i].getValue();
		//devuelvo auxiliar
		return aux;
	}
	
}


//###############
//##### SET #####
//###############



import LinkedList;

public interface Set<E> {
	public void insert(E x);
	public void delete(E x);
	public boolean member(E x);
	public Set<E> intersection(Set<E> S);
	public Set<E> union(Set<E> S);
	public LinkedList<E> values();
}

//###########################
//##### LINKED SET LIST #####
//###########################

//esta implementación usa una lista interna, NO es lo que pedía el enunciado pero puede funcionar

public class LinkedSetList<E> implements Set<E>{
	private LinkedList<E> listaInterna;
	public LinkedSetList(){}
	public void insert(E x) {
		if(!member(x)) {
			listaInterna.addFirst(x);
		}	
	}
	public void delete(E x) {
		listaInterna.remove(x);
	}
	public boolean member(E x) {
		listaInterna.First();
		boolean encontre =false;
		while(!encontre && !listaInterna.atEnd()) {
			if(listaInterna.getCurrent().equals(x))
				encontre=true;
			listaInterna.advance();
		}
		return encontre;
	}
	
	public Set<E> intersection(Set<E> S)
	{
		Set<E> salida = new LinkedSet<E>();
		listaInterna.First();
		while(!listaInterna.atEnd()) {
			if(S.member(listaInterna.getCurrent()))
				salida.insert(listaInterna.getCurrent());
			listaInterna.advance();
		}
		return salida;
	}
	public Set<E> union(Set<E> S)
	{
		Set<E> salida = new LinkedSet<E>();
		listaInterna.First();
		while(!listaInterna.atEnd()) {
			salida.insert(listaInterna.getCurrent());
			listaInterna.advance();
		}
		LinkedList<E> valoresS = S.values();
		valoresS.First();
		while(!valoresS.atEnd()) {
			salida.insert(valoresS.getCurrent());
			valoresS.advance();
		}
		return salida;
	}
	
	public LinkedList<E> values(){
		return listaInterna;
	}
	
}


//######################
//##### LINKED SET #####
//######################


public class LinkedSet<E> implements Set<E> {
	private Node<E> head;
	private int size;
	private Node<E> current;
	//constructor
	public LinkedSet(){
		head=null; 
		size=0;
	}
	public void insert(E x) {
		if(!member(x)) {
			Node<E> n=new Node<E>(x);
			n.setNext(head);
			head=n;
			size++;
		}	
	}
	public void delete(E x) {
		if(head!=null && x.equals(head.getElement()))
		{
			Node<E> aux=head.getNext();
			head.setNext(null);
			head=aux;
			size--;
		}
		Node<E> aux=head;
		while(aux!=null && !aux.getNext().getElement().equals(x)) 
			aux=aux.getNext();
		if(aux!=null)
		{
			Node<E> aEliminar = aux.getNext();
			aux.setNext(aEliminar.getNext());
			aEliminar.setNext(null);
			size--;
		}
	}
	public boolean member(E x) {
		Node<E> aux = head;
		boolean encontre =false;
		while(!encontre && aux!=null) {
			if(aux.getElement().equals(x))
				encontre=true;
			aux=aux.getNext();
		}
		return encontre;
	}
	public Set<E> intersection(Set<E> S)
	{
		Set<E> salida = new LinkedSet<E>();
		Node<E> aux = head;
		while(aux!=null) {
			if(S.member(aux.getElement()))
				salida.insert(aux.getElement());
			aux=aux.getNext();
		}
		return salida;
	}
	public Set<E> union(Set<E> S)
	{
		Set<E> salida = new LinkedSet<E>();
		Node<E> aux = head;
		while(aux!=null) {
			salida.insert(aux.getElement());
			aux=aux.getNext();
		}
		LinkedList<E> valoresS = S.values();
		valoresS.First();
		while(!valoresS.atEnd()) {
			salida.insert(valoresS.getCurrent());
			valoresS.advance();
		}
		return salida;
	}
	public LinkedList<E> values(){
		LinkedList<E> salida = new LinkedList<E>();
		Node<E> aux = head;
		while(aux!=null) {
			salida.addFirst(aux.getElement());
			aux=aux.getNext();
		}
		return salida;
	}
}


//#####################
//##### ARRAY SET #####
//#####################


public class ArraySet<E> implements Set<E> {
	private E[] array;
	private int size;
	
	public ArraySet() {
		array = (E[])new Object[100];
		size = 0;
	}
	
	public void insert(E x) {
		if(!member(x)) {
			//inserto un nuevo elemento que no estaba
			if(size<array.length) {
				array[size] = x;
				size++;
			}
			else
				//podría hacer un resize
				throw new MyException("El arreglo está lleno");
		}
		
	}
	public void delete(E x) {
		int i=0;
		boolean encontreElemento=false;
		while(!encontreElemento && i<size) {
			if(array[i].equals(x))
			{
				encontreElemento=true;
				array[i] = array[size-1];
				size--;
			}
			else
				i++;
		}
		
	}
	public boolean member(E x) {
		int i=0;
		boolean encontreElemento=false;
		while(!encontreElemento && i<size) {
			if(array[i].equals(x))
				encontreElemento=true;
			else
				i++;
		}
		return encontreElemento;
	}
	public Set<E> intersection(Set<E> S){
		ArraySet<E> salida = new ArraySet<E>();
		for(int i = 0; i<size;i++) {
			if(S.member(array[i]))
				salida.insert(array[i]);
		}
		return salida;
		
		//Si quería verlo parado del lado de S:
		/*LinkedList<E> valoresS = S.values();
		valoresS.First();
		while(!valoresS.atEnd())
		{
			E elemento = valoresS.getCurrent();
			if(member(elemento))
				salida.insert(elemento);
			valoresS.advance();
		}*/
	}
	public Set<E> union(Set<E> S){
		ArraySet<E> salida = new ArraySet<E>();
		for(int i = 0; i<size;i++) {
			salida.insert(array[i]);
		}
		LinkedList<E> valoresS = S.values();
		valoresS.First();
		while(!valoresS.atEnd())
		{
			E elemento = valoresS.getCurrent();
			salida.insert(elemento);
			valoresS.advance();
		}
		return salida;
	}
	public LinkedList<E> values(){
		LinkedList<E> salida = new LinkedList<E>();
		for(int i = 0; i<size;i++) {
			salida.addFirst(array[i]);
		}
		return salida;
	}

}


//###################
//##### ABB TDA #####
//###################


public interface ABBTDA<E extends Comparable<E>> {
	public boolean pertenece( E elemento );
	public void insertar( E elemento );
	public E eliminar( E elemento );
	public String toString();
}


//####################
//##### NODO ABB #####
//####################


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

//######################
//##### COMPARATOR #####
//######################


public class DefaultComparator<E> implements java.util.Comparator<E> { 

	public int compare( E a, E b ) { return((Comparable)a).compareTo(b); } 
}


//#######################
//##### ArbolBB ABB #####
//#######################

import java.util.Comparator;
public class arbolBB<E extends Comparable<E>> implements ABBTDA<E> {
	protected NodoABB<E> raiz;
	protected int size;
	Comparator<E> comp;
	//CONSTRUCTOR
	public arbolBB(Comparator<E> comp) { 
		raiz = new NodoABB<E>(null,null); 
		size = 0;
		this.comp = comp;
	}
	
	//PARA BUSCAR UN ELEMENTO
	public boolean pertenece( E elemento ) { 
		return buscar(elemento).getElemento() != null; 
	}
	private NodoABB<E> buscar( E elemento ) {
		return buscarAux( elemento, raiz );
	}
	private NodoABB<E> buscarAux( E elemento, NodoABB<E> nodov ) {
		 if( nodov.getElemento() == null ) 
			 return nodov;
		 else{
			 int c = comp.compare( elemento, nodov.getElemento() );
			 if( c == 0 ) return nodov;
			 else 
				 if( c < 0 ) 
					 return buscarAux( elemento, nodov.getIzq() );
				 else 
					 return buscarAux( elemento, nodov.getDer() );
		 }
	}
	
	//PARA INSERTAR UN ELEMENTO
	public void insertar( E elemento ) {
		NodoABB<E> nodov = buscar( elemento );
		if( nodov.getElemento() == null ) {
			nodov.setElemento( elemento );
			nodov.setIzq( new NodoABB<E>( null, nodov ) );
			nodov.setDer( new NodoABB<E>( null, nodov ) );
			size++;
		}
	}
	
	//La solución anterior es más simple pero podía ir por la alternativa
	//insertar alternativo recursivo como lo vimos en clase:
	public void insertar2( E elemento ) {
		insertarAux( elemento, raiz ); 
	}
	private void insertarAux( E elemento, NodoABB<E> nodov ) {
		if( nodov.getElemento() == null ) {
			nodov.setElemento( elemento ); size++;
			nodov.setIzq( new NodoABB<E>( null, nodov ) );
			nodov.setDer( new NodoABB<E>( null, nodov ) );
		} 
		else {
			int c = comp.compare( elemento, nodov.getElemento() );
			if( c == 0 ) {  /* ¿Qué hacemos si el elemento ya está? */ }
			else 
				if( c < 0 ) 
					insertarAux( elemento, nodov.getIzq() );
				else 
					insertarAux( elemento, nodov.getDer() );
		}
	}
	 
	//PARA ELIMINAR UN ELEMENTO
	// retorna null si no pudo eliminar a k, retorna k si la pudo eliminar
	public E eliminar( E elemento ) {
		NodoABB<E> p = buscar( elemento );
		if( p.getElemento() != null ) {
			E eliminado = p.getElemento();
			eliminarAux( p );
			size--;
			return eliminado;
		} 
		else 
			return null;
	}
	private boolean isExternal( NodoABB<E> p ) { 
		return p.getIzq().getElemento() == null && p.getDer().getElemento() == null; 
	}
	private boolean soloTieneHijoIzquierdo( NodoABB<E> p ) {
		return p.getIzq().getElemento() != null &&  p.getDer().getElemento() == null;
	}
	private boolean soloTieneHijoDerecho( NodoABB<E> p ) {
		return p.getDer().getElemento() != null && p.getIzq().getElemento() == null;
	}
	
	private void eliminarAux(NodoABB<E> p) {
	    if (isExternal(p)) { // Si el nodo es una hoja (es decir, no tiene hijos)
	        // Convertir el nodo en un nodo "dummy" y eliminar sus referencias a los hijos
	        p.setElemento(null);
	        p.setIzq(null);
	        p.setDer(null);
	    } else {
	        if (soloTieneHijoIzquierdo(p)) { // Si el nodo tiene solo un hijo izquierdo
	            if (p.getPadre() == null) { // Caso especial: si el nodo es la raíz
	                // La raíz pasa a ser el hijo izquierdo y se elimina la referencia al padre
	                raiz = p.getIzq();
	                raiz.setPadre(null);
	            } else if (p.getPadre().getIzq() == p) { // Si el nodo a eliminar es el hijo izquierdo de su padre
	                // Se engancha el hijo izquierdo del nodo a su abuelo (el padre del nodo a eliminar)
	                p.getPadre().setIzq(p.getIzq());
	                p.getIzq().setPadre(p.getPadre());
	            } else { // Si el nodo a eliminar es el hijo derecho de su padre
	                // Se engancha el hijo izquierdo del nodo a su abuelo (el padre del nodo a eliminar)
	                p.getPadre().setDer(p.getIzq());
	                p.getIzq().setPadre(p.getPadre());
	            }
	        } else if (soloTieneHijoDerecho(p)) { // Si el nodo tiene solo un hijo derecho
	            if (p.getPadre() == null) { // Caso especial: si el nodo es la raíz
	                // La raíz pasa a ser el hijo derecho y se elimina la referencia al padre
	                raiz = p.getDer();
	                raiz.setPadre(null);
	            } else if (p.getPadre().getIzq() == p) { // Si el nodo a eliminar es el hijo izquierdo de su padre
	                // Se engancha el hijo derecho del nodo a su abuelo (el padre del nodo a eliminar)
	                p.getPadre().setIzq(p.getDer());
	                p.getDer().setPadre(p.getPadre());
	            } else { // Si el nodo a eliminar es el hijo derecho de su padre
	                // Se engancha el hijo derecho del nodo a su abuelo (el padre del nodo a eliminar)
	                p.getPadre().setDer(p.getDer());
	                p.getDer().setPadre(p.getPadre());
	            }
	        } else { // Si el nodo tiene ambos hijos (nodo con dos hijos)
	            // Se reemplaza el elemento del nodo con el valor mínimo del subárbol derecho
	            p.setElemento(eliminarMinimo(p.getDer()));
	        }
	    }
	}
	
	// Elimina el nodo con elemento mínimo del subárbol que tiene como raíz a p
	// El mínimo rótulo del subárbol que tiene como raíz a p es el rótulo del primer nodo que 
	// encuentro yendo a la izquierda que no tiene hijo izquierdo 
	private E eliminarMinimo( NodoABB<E> p ) {
		if( p.getIzq().getElemento() == null ) {  // El hijo izquierdo de p es un dummy
			E aRetornar = p.getElemento();  // salvo el rótulo a devolver
			if( p.getDer().getElemento() == null ) { // p es hoja (pues sus hijos son dummy)
				p.setElemento( null ); // Convierto a p en dummy haciendo nulo su rótulo
				p.setIzq( null ); // y desenganchando sus dos hijos dummy
				p.setDer( null );
			} 
			else { 
				// p solo tiene hijo derecho (xq no tiene izquierdo)
				// Engancho al padre de p con el hijo derecho de p.
				// Seguro tiene que ser el hijo derecho de su padre.
				p.getPadre().setDer( p.getDer() );
				p.getDer().setPadre( p.getPadre() );
			}
			return aRetornar;
		} 
		else { // Si p tiene hijo izquierdo, entonces p.getRotulo() no es el mínimo.
			// El mínimo tiene que estar en el subárbol izquierdo
			return eliminarMinimo( p.getIzq() );
		}
	
	}

	//un método para mostrar el árbol
	public String toString() {
		return inorder( raiz );
	}
	private String inorder( NodoABB<E> nodov ) {
		if( nodov.getElemento() != null ) {
			return "(" + inorder( nodov.getIzq()) + nodov.getElemento() + inorder( nodov.getDer() ) + ")";
		}	 
		else return "";
	}
	
}

//############################
//##### COMPARAR NOMRBES #####
//############################


public class Nombre implements Comparable<Nombre>{
	private String Valor;
	public Nombre (String input) {
		Valor = input;
	}
	public String getValor() {return Valor;}
	public int compareTo(Nombre otroNombre) {
		return Valor.compareTo(otroNombre.getValor());
	}
}


//##################
//##### AVLTDA #####
//##################


public interface AVLTDA <E extends Comparable<E>> {
	public boolean pertenece( E elemento );
	public void insertar( E elemento );
	public E eliminar( E elemento );
	public String toString();
}


//####################
//##### NODO AVL #####
//####################


public class NodoAVL<E> {
	private NodoAVL<E> padre;
	private E elemento;
	private int altura; //diferencia vs ABB
	private boolean eliminado; // diferencia vs ABB
	private NodoAVL<E> izq, der;
	public NodoAVL (E elem, NodoAVL<E> padre){ 
		altura = 0; 
		eliminado = false;
		this.elemento = elem;
		this.padre = padre;
		izq = der = null;
	}
	public E getElemento() { return elemento; }
	public NodoAVL<E> getPadre() { return padre; }
	public NodoAVL<E> getIzq() { return izq; }
	public NodoAVL<E> getDer() { return der; }
	public int getAltura() {return altura;}
	public boolean getEliminado() {return eliminado;}
	public void setElemento( E element ) { this.elemento = element; }
	public void setIzq( NodoAVL<E> izq ) { this.izq = izq; }
	public void setDer( NodoAVL<E> der ) { this.der = der; }
	public void setPadre( NodoAVL<E> padre ) { this.padre = padre; }
	public void setAltura(int alt) {this.altura=alt;}
	public void setEliminado(boolean elim) {this.eliminado=elim;}
}


//###############
//##### AVL #####
//###############


import Comparator;

public class AVL<E extends Comparable<E>> implements AVLTDA<E>   {
	protected NodoAVL<E> raiz;
	protected int size;
	Comparator<E> comp;
	//CONSTRUCTOR
	public AVL(Comparator<E> comp) { 
		raiz = new NodoAVL<E>(null,null); 
		size = 0;
		this.comp = comp;
	}
	//PERTENECE ES IGUAL A ABB
	public boolean pertenece( E elemento ) { 
		return buscar(elemento).getElemento() != null; 
	}
	private NodoAVL<E> buscar( E elemento ) {
		return buscarAux( elemento, raiz );
	}
	private NodoAVL<E> buscarAux( E elemento, NodoAVL<E> nodov ) {
		 if( nodov.getElemento() == null ) 
			 return nodov;
		 else{
			 int c = comp.compare( elemento, nodov.getElemento() );
			 if( c == 0 ) return nodov;
			 else 
				 if( c < 0 ) 
					 return buscarAux( elemento, nodov.getIzq() );
				 else 
					 return buscarAux( elemento, nodov.getDer() );
		 }
	}
	
	//VEAMOS AHORA LOS CAMBIOS EN INSERTAR
	public void insertar(E x)
	{
		insertaux( raiz, x );
	}
	private int max(int i, int j )
	{
		return i>j ? i : j;
	}
	private void insertaux(NodoAVL<E> t, E item) {
		if (t.getElemento() == null) {
			t.setElemento(item);
			t.setAltura(1);
			t.setIzq(new NodoAVL<>(null, t));
			t.setDer(new NodoAVL<>(null, t));
		} else {
			int comparacion = comp.compare(item, t.getElemento());
			if (comparacion < 0) {
				insertaux(t.getIzq(), item);
				if (Math.abs(t.getIzq().getAltura() - t.getDer().getAltura()) > 1) {
					// Determina si es una Rotación I o II
					if (comp.compare(item, t.getIzq().getElemento()) < 0)
						rotacion_I(t);  // Rotación simple a la derecha
					else
						rotacion_II(t); // Rotación doble a la derecha
				}
			} else if (comparacion > 0) {
				insertaux(t.getDer(), item);
				if (Math.abs(t.getIzq().getAltura() - t.getDer().getAltura()) > 1) {
					// Determina si es una Rotación III o IV
					if (comp.compare(item, t.getDer().getElemento()) > 0)
						rotacion_III(t);  // Rotación simple a la izquierda
					else
						rotacion_IV(t);   // Rotación doble a la izquierda
				}
			} else {
				// Si el elemento ya está presente, lo actualizamos (opcional según diseño)
				t.setElemento(item);
			}
			// Actualiza la altura del nodo
			t.setAltura(1 + Math.max(altura(t.getIzq()), altura(t.getDer())));
		}
	}

	
	// Rotación Simple a la Derecha (Rotación I)
	private void rotacion_I(NodoAVL<E> raizSubArbol) {
		NodoAVL<E> nodoIzq = raizSubArbol.getIzq();
		raizSubArbol.setIzq(nodoIzq.getDer());
		if (nodoIzq.getDer() != null) {
			nodoIzq.getDer().setPadre(raizSubArbol);
		}
		nodoIzq.setPadre(raizSubArbol.getPadre());

		if (raizSubArbol.getPadre() == null) {
			raiz = nodoIzq;
		} else if (raizSubArbol == raizSubArbol.getPadre().getDer()) {
			raizSubArbol.getPadre().setDer(nodoIzq);
		} else {
			raizSubArbol.getPadre().setIzq(nodoIzq);
		}
		nodoIzq.setDer(raizSubArbol);
		raizSubArbol.setPadre(nodoIzq);

		// Actualizar las alturas
		raizSubArbol.setAltura(1 + max(altura(raizSubArbol.getIzq()), altura(raizSubArbol.getDer())));
		nodoIzq.setAltura(1 + max(altura(nodoIzq.getIzq()), altura(nodoIzq.getDer())));
	}

	// Rotación Doble a la Derecha (Rotación II)
	private void rotacion_II(NodoAVL<E> raizSubArbol) {
		rotacion_III(raizSubArbol.getIzq());
		rotacion_I(raizSubArbol);
	}

	// Rotación Simple a la Izquierda (Rotación III)
	private void rotacion_III(NodoAVL<E> raizSubArbol) {
		NodoAVL<E> nodoDer = raizSubArbol.getDer();
		raizSubArbol.setDer(nodoDer.getIzq());
		if (nodoDer.getIzq() != null) {
			nodoDer.getIzq().setPadre(raizSubArbol);
		}
		nodoDer.setPadre(raizSubArbol.getPadre());

		if (raizSubArbol.getPadre() == null) {
			raiz = nodoDer;
		} else if (raizSubArbol == raizSubArbol.getPadre().getIzq()) {
			raizSubArbol.getPadre().setIzq(nodoDer);
		} else {
			raizSubArbol.getPadre().setDer(nodoDer);
		}
		nodoDer.setIzq(raizSubArbol);
		raizSubArbol.setPadre(nodoDer);

		// Actualizar las alturas
		raizSubArbol.setAltura(1 + max(altura(raizSubArbol.getIzq()), altura(raizSubArbol.getDer())));
		nodoDer.setAltura(1 + max(altura(nodoDer.getIzq()), altura(nodoDer.getDer())));
	}

	// Rotación Doble a la Izquierda (Rotación IV)
	private void rotacion_IV(NodoAVL<E> raizSubArbol) {
		rotacion_I(raizSubArbol.getDer());
		rotacion_III(raizSubArbol);
	}
	
	public E eliminar(E elemento) {
		NodoAVL<E> nodoAEliminar = buscar(elemento);
		if (nodoAEliminar == null || nodoAEliminar.getElemento() == null) {
			return null; // Elemento no encontrado
		}
		E eliminado = nodoAEliminar.getElemento();
		raiz = eliminarNodo(raiz, elemento);
		return eliminado;
	}

	private NodoAVL<E> eliminarNodo(NodoAVL<E> nodo, E elemento) {
		if (nodo == null || nodo.getElemento() == null) {
			return nodo;
		}

		int comparacion = comp.compare(elemento, nodo.getElemento());

		if (comparacion < 0) {
			nodo.setIzq(eliminarNodo(nodo.getIzq(), elemento));
		} else if (comparacion > 0) {
			nodo.setDer(eliminarNodo(nodo.getDer(), elemento));
		} else {
			// Nodo encontrado
			if (nodo.getIzq().getElemento() == null) {
				return nodo.getDer();
			} else if (nodo.getDer().getElemento() == null) {
				return nodo.getIzq();
			} else {
				// Nodo con dos hijos
				NodoAVL<E> sucesor = encontrarMin(nodo.getDer());
				nodo.setElemento(sucesor.getElemento());
				nodo.setDer(eliminarNodo(nodo.getDer(), sucesor.getElemento()));
			}
		}

		// Actualizar la altura y balancear el nodo
		nodo.setAltura(1 + Math.max(altura(nodo.getIzq()), altura(nodo.getDer())));
		return balancear(nodo);
	}

	private NodoAVL<E> encontrarMin(NodoAVL<E> nodo) {
		while (nodo.getIzq().getElemento() != null) {
			nodo = nodo.getIzq();
		}
		return nodo;
	}
	
	
	private NodoAVL<E> balancear(NodoAVL<E> nodo) {
		int balance = obtenerBalance(nodo);

		// Rotación derecha
		if (balance > 1 && obtenerBalance(nodo.getIzq()) >= 0) {
			return rotacionDerecha(nodo);
		}

		// Rotación izquierda-derecha
		if (balance > 1 && obtenerBalance(nodo.getIzq()) < 0) {
			nodo.setIzq(rotacionIzquierda(nodo.getIzq()));
			return rotacionDerecha(nodo);
		}

		// Rotación izquierda
		if (balance < -1 && obtenerBalance(nodo.getDer()) <= 0) {
			return rotacionIzquierda(nodo);
		}

		// Rotación derecha-izquierda
		if (balance < -1 && obtenerBalance(nodo.getDer()) > 0) {
			nodo.setDer(rotacionDerecha(nodo.getDer()));
			return rotacionIzquierda(nodo);
		}

		return nodo;
	}
	
	private NodoAVL<E> rotacionDerecha(NodoAVL<E> y) {
		NodoAVL<E> x = y.getIzq();
		NodoAVL<E> T2 = x.getDer();

		x.setDer(y);
		y.setIzq(T2);

		y.setAltura(1 + max(altura(y.getIzq()), altura(y.getDer())));
		x.setAltura(1 + max(altura(x.getIzq()), altura(x.getDer())));

		return x;
	}

	private NodoAVL<E> rotacionIzquierda(NodoAVL<E> x) {
		NodoAVL<E> y = x.getDer();
		NodoAVL<E> T2 = y.getIzq();

		y.setIzq(x);
		x.setDer(T2);

		x.setAltura(1 + max(altura(x.getIzq()), altura(x.getDer())));
		y.setAltura(1 + max(altura(y.getIzq()), altura(y.getDer())));

		return y;
	}
	
	private int altura(NodoAVL<E> nodo) {
		return nodo == null ? -1 : nodo.getAltura();
	}

	private int obtenerBalance(NodoAVL<E> nodo) {
		return nodo == null ? 0 : altura(nodo.getIzq()) - altura(nodo.getDer());
	}
}



//#####################
//##### GRAFO TDA #####
//#####################

public interface GrafoTDA<E> {
	void agregarVertice(E v); //grafo inicializado y ∄ vértice
	void eliminarVertice(E v); //grafo inicializado y ∃ vértice
	E[] vertices(); //grafo inicializado
	void agregarArista(E v1, E v2, int peso); //grafo inicializado, ∄ arista y ∃ ambos vértices
	void eliminarArista(E v1, E v2); //grafo inicializado y ∃ arista
	boolean existeArista(E v1, E v2); //grafo inicializado y ∃ ambos vértices
	int pesoArista(E v1, E v2); //grafo inicializado y ∃ arista
}

//#######################
//##### NODO ARISTA #####
//#######################

public class NodoArista<E> {
	private int peso;
	private NodoVertice<E> verticeDestino;
	private NodoArista<E> sigArista;
	
	public NodoArista() {}
	
	public int getPeso() {
		return peso;
	}
	public void setPeso(int peso) {
		this.peso = peso;
	}
	public NodoVertice<E> getVerticeDestino() {
		return verticeDestino;
	}
	public void setVerticeDestino(NodoVertice<E> verticeDestino) {
		this.verticeDestino = verticeDestino;
	}
	public NodoArista<E> getSigArista() {
		return sigArista;
	}
	public void setSigArista(NodoArista<E> sigArista) {
		this.sigArista = sigArista;
	}
	
}

//########################
//##### NODO VERTICE #####
//########################

public class NodoVertice<E> {
	private E vertice;
	private NodoArista<E> aristas;
	private NodoVertice<E> sigVertice;
	
	public NodoVertice() {}
	
	public E getVertice() {
		return vertice;
	}

	public void setVertice(E vertice) {
		this.vertice = vertice;
	}

	public NodoArista<E> getAristas() {
		return aristas;
	}

	public void setAristas(NodoArista<E> aristas) {
		this.aristas = aristas;
	}

	public NodoVertice<E> getSigVertice() {
		return sigVertice;
	}

	public void setSigVertice(NodoVertice<E> sigVertice) {
		this.sigVertice = sigVertice;
	}
	
}

//##########################################
//##### GRAFO CON MATRIZ DE ADYACENCIA #####
//##########################################

public class GrafoEst<E> implements GrafoTDA<E> {
	private int[][] mAdy; //Matriz de adyacencia
	private E[] etiqs; //Vector para mapeo a índices
	private int cantNodos;
	
	@SuppressWarnings("unchecked")
	public void inicializarGrafo() {
		mAdy = new int[100][100];
		etiqs = (E[])new Object[100];
		cantNodos = 0;
	}
	
	public void agregarVertice(E v) {
		etiqs[cantNodos] = v;
		for (int i = 0; i <= cantNodos; i++) {
			mAdy[cantNodos][i] = 0; //Nueva fila en 0
			mAdy[i][cantNodos] = 0; //Nueva columna en 0
		}
		cantNodos++;
	}
	
	public void eliminarVertice(E v) {
		int ind = vert2Indice(v); //índice del vértice por eliminar
		for (int k = 0; k < cantNodos; k++)
			mAdy[k][ind] = mAdy[k][cantNodos-1]; //se “pisa” la fila...
		for (int k = 0; k < cantNodos; k++)
			mAdy[ind][k] = mAdy[cantNodos-1][k]; //... y la columna
		etiqs[ind] = etiqs[cantNodos-1];
		cantNodos--;
	}
	
	private int vert2Indice(E v) { //Mapeamos vértice a índice
		int i = cantNodos-1;
		while(i >= 0 && etiqs[i] != v)
			i--;
		return i;
	}
	
	public E[] vertices() {
		@SuppressWarnings("unchecked")
		E[] salida = (E[])new Object[100];
		for (int i = 0; i < cantNodos; i++) {
			salida[i]=etiqs[i];
		}
		return salida;
	}
	
	public void agregarArista(E v1, E v2, int peso) {
		int o = vert2Indice(v1);
		int d = vert2Indice(v2);
		mAdy[o][d] = peso;
	}
	
	public void eliminarArista(E v1, E v2) {
		int o = vert2Indice(v1);
		int d = vert2Indice(v2);
		mAdy[o][d] = 0;
	}
	
	public boolean existeArista(E v1, E v2) {
		int o = vert2Indice(v1);
		int d = vert2Indice(v2);
		return mAdy[o][d] != 0;
	}
	
	public int pesoArista(E v1, E v2) {
		int o = vert2Indice(v1);
		int d = vert2Indice(v2);
		return mAdy[o][d];
	}
}


//#########################################
//##### GRAFO CON LISTA DE ADYACENCIA #####
//#########################################


public class GrafoDin<E> implements GrafoTDA<E> {
	private NodoVertice<E> origen;
	private int vertices;
	
	public GrafoDin() {
		origen = null;
	}
	
	public void agregarVertice(E v) { //El vértice se inserta al inicio de la lista de nodos
		NodoVertice<E> aux = new NodoVertice<E>();
		aux.setVertice(v);
		aux.setAristas(null);
		aux.setSigVertice(origen);
		origen = aux;
		vertices++;
	}
	
	
	
	public void eliminarVertice(E v) {
		if (origen.getVertice().equals(v)) //Es el origen
			origen = origen.getSigVertice(); //Se elimina el origen
		NodoVertice<E> aux = origen; //No es el origen; hay que buscarlo
		while (aux != null) { //Eliminamos aristas hacia v
			this.eliminarAristaNodo(aux, v);
			if (aux.getSigVertice() != null && aux.getSigVertice().getVertice().equals(v)) {
				aux.setSigVertice(aux.getSigVertice().getSigVertice()); //Si es el nodo, lo elimina
				vertices--;
			}
			aux = aux.getSigVertice(); //Sigue eliminando aristas
		}
		
	}
	
	private void eliminarAristaNodo(NodoVertice<E> nodo, E v) {
		NodoArista<E> aux = nodo.getAristas(); //Elimina de nodo las aristas hacia v
		if (aux != null) {
			if (aux.getVerticeDestino().getVertice().equals(v)) { //Hay que eliminar la primera arista
				nodo.setAristas(aux.getSigArista());
			} 
			else { //No es la primera; la buscamos
				while (aux.getSigArista() != null && !aux.getSigArista().getVerticeDestino().getVertice().equals(v))
					aux = aux.getSigArista();
				if (aux.getSigArista() != null) { //Eliminamos la arista
					aux.setSigArista(aux.getSigArista().getSigArista());
				}
			}
		}
	}
	
	public E[] vertices() {
		@SuppressWarnings("unchecked")
		E[] salida = (E[])new Object[vertices];
		NodoVertice<E> aux = origen;
		int i = 0;
		while (aux != null) {
			salida[i]=aux.getVertice();
			i++;
			aux = aux.getSigVertice();
		}
		return salida;
	}
	
	public void agregarArista(E v1, E v2, int peso ) {
		NodoVertice<E> n1 = vert2Nodo(v1); //Buscamos el nodo origen...
		NodoVertice<E> n2 = vert2Nodo(v2); //... y el nodo destino
		NodoArista<E> aux = new NodoArista<E>(); //La arista va al inicio de la lista...
		aux.setPeso(peso); //... de aristas salientes de v1
		aux.setVerticeDestino(n2);
		aux.setSigArista(n1.getAristas());
		n1.setAristas(aux);
	}
	
	private NodoVertice<E> vert2Nodo(E v) { //Dado un valor, busca el nodo correspondiente
		NodoVertice<E> aux = origen;
		while (aux != null && !aux.getVertice().equals(v))
			aux = aux.getSigVertice();
		return aux;
	}
	
	public void eliminarArista(E v1, E v2) {
		NodoVertice<E> n1 = vert2Nodo(v1);
		eliminarAristaNodo(n1, v2);
	}
	
	public boolean existeArista(E v1, E v2) {
		NodoVertice<E> n1 = vert2Nodo(v1);
		NodoArista<E> aux = n1.getAristas();
		while (aux != null && !aux.getVerticeDestino().getVertice().equals(v2)) {
			aux = aux.getSigArista();
		}
		//Solo si se encontro la arista buscada, aux no es null
		return aux != null;
	}
	
	public int pesoArista(E v1, E v2) {
		NodoVertice<E> n1 = vert2Nodo(v1);
		NodoArista<E> aux = n1.getAristas();
		while (!aux.getVerticeDestino().getVertice().equals(v2))
			aux = aux.getSigArista(); //Buscamos la arista
		return aux.getPeso();
	}
	

}
