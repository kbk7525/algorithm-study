package boj;
import java.util.Scanner;
public class boj_15964 {
	public static void main(String[] args) {
		Scanner in = new Scanner(System.in);
		int a = in.nextInt();
		int b = in.nextInt();
		System.out.println(((a+b)*(a-b)));
		in.close();
	}
}
