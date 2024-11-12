package clase_8_ejercicio_7;

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
