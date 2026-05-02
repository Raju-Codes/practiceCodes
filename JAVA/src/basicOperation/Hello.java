package basicOperation;

import java.util.Scanner;

public class Hello {
    static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
//        int x;
//        int y;
//        int z;
//        x = y = z=10;
//        System.out.println("Value of x "+ x);
//        System.out.println("Value of y "+ y);
//        System.out.println("Value of z "+ z);
//        z=100;
//        System.out.println("Value of x "+ x);
//        System.out.println("Value of y "+ y);
//        System.out.println("Value of z "+ z);

        int[] myArray = new int [5];
        for (int i=0; i < myArray.length; i++){
            myArray[i]=sc.nextInt();
        }
        for (int i=0; i < myArray.length; i++){
            System.out.print(myArray[i]+ " ");        }
    }
}
