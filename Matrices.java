import java.util.Scanner;

public class Matrices {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        // Pedir al usuario las dimensiones de A y B
        System.out.print("Ingrese el número de filas de A: ");
        int m1 = sc.nextInt();
        System.out.print("Ingrese el número de columnas de A: ");
        int n1 = sc.nextInt();
        System.out.print("Ingrese el número de filas de B: ");
        int m2 = sc.nextInt();
        System.out.print("Ingrese el número de columnas de B: ");
        int n2 = sc.nextInt();

        // Crear las matrices A y B con las dimensiones especificadas por el usuario
        int[][] A = new int[m1][n1];
        int[][] B = new int[m2][n2];

        // Pedir al usuario los elementos de A y B
        System.out.println("Ingrese los elementos de la matriz A:");
        for (int i = 0; i < m1; i++) {
            for (int j = 0; j < n1; j++) {
                System.out.printf("A(%d,%d): ", i + 1, j + 1);
                A[i][j] = sc.nextInt();
            }
        }

        System.out.println("Ingrese los elementos de la matriz B:");
        for (int i = 0; i < m2; i++) {
            for (int j = 0; j < n2; j++) {
                System.out.printf("B(%d,%d): ", i + 1, j + 1);
                B[i][j] = sc.nextInt();
            }
        }

        // Imprimir las matrices A y B
        System.out.println("Matriz A:");
        imprimirMatriz(A);
        System.out.println("Matriz B:");
        imprimirMatriz(B);

        // Realizar las operaciones si es posible
        if (n1 == n2 && m1 == m2) { // Si las matrices son de las mismas dimensiones
            System.out.println("3A:");
            imprimirMatriz(multiplicarPorEscalar(A, 3));

            System.out.println("4B:");
            imprimirMatriz(multiplicarPorEscalar(B, 4));

            System.out.println("A + B:");
            imprimirMatriz(sumarMatrices(A, B));

            System.out.println("B × A:");
            imprimirMatriz(multiplicarMatrices(B, A));
        } else {
            System.out
                    .println("No es posible realizar las operaciones, las matrices no son de las mismas dimensiones.");
        }
    }

    // Función para imprimir una matriz en pantalla
    public static void imprimirMatriz(int[][] matriz) {
        for (int i = 0; i < matriz.length; i++) {
            for (int j = 0; j < matriz[0].length; j++) {
                System.out.print(matriz[i][j] + " ");
            }
            System.out.println();
        }
    }

    public static int[][] sumarMatrices(int[][] A, int[][] B) {
        int m = A.length;
        int n = A[0].length;
        int[][] C = new int[m][n];
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                C[i][j] = A[i][j] + B[i][j];
            }
        }
        return C;
    }

    public static int[][] multiplicarMatrices(int[][] A, int[][] B) {
        int m = A.length;
        int n = A[0].length;
        int p = B[0].length;
        int[][] C = new int[m][p];
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < p; j++) {
                for (int k = 0; k < n; k++) {
                    C[i][j] += A[i][k] * B[k][j];
                }
            }
        }
        return C;
    }

    public static int[][] multiplicarPorEscalar(int[][] A, int escalar) {
        int m = A.length;
        int n = A[0].length;
        int[][] C = new int[m][n];
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                C[i][j] = A[i][j] * escalar;
            }
        }
        return C;
    }

}
