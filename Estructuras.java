
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



