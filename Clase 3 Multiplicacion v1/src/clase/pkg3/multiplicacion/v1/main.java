
package clase.pkg3.multiplicacion.v1;

import java.util.Scanner;

public class main {
    public static void main(String[] args) {
        int numero1 = 10;
        int numero2 = 12;     
        int contador = 1;
        int iterador = 1;
        
        do{
            int resultado = iterador * contador;
            System.out.println(iterador +" x "+ contador +" = "+ resultado);
            contador++;
            
        }while (contador <= numero2);
        
        Scanner Scan = new Scanner (System.in);
        System.out.println("");
    }
    
}
