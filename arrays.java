import java.util.Scanner;

public class arrays {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        // Pedir al usuario la longitud de los vectores
        System.out.print("Ingrese la longitud de los vectores: ");
        int n = sc.nextInt();
        
        // Declarar los vectores y pedir al usuario sus valores
        int[] vector1 = new int[n];
        int[] vector2 = new int[n];
        System.out.println("Ingrese los valores del primer vector:");
        for (int i = 0; i < n; i++) {
            System.out.print("Valor " + (i+1) + ": ");
            vector1[i] = sc.nextInt();
        }
        System.out.println("Ingrese los valores del segundo vector:");
        for (int i = 0; i < n; i++) {
            System.out.print("Valor " + (i+1) + ": ");
            vector2[i] = sc.nextInt();
        }
        
        // Calcular el producto escalar
        int productoEscalar = 0;
        for (int i = 0; i < n; i++) {
            productoEscalar += vector1[i] * vector2[i];
        }
        
        // Mostrar el resultado
        System.out.println("El producto escalar es: " + productoEscalar);
    }

}
