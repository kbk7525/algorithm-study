package boj;
import java.util.Scanner;

//dp를 활용한 문제
public class boj_11727 {
	public static void main(String[] args) {
		Scanner in = new Scanner(System.in);
		int n = in.nextInt();
		int dp[] = new int[1001];
		dp[1] = 1;
		dp[2] = 3;
		for(int i = 3; i <= n; i++) {
			dp[i] = (dp[i-1] + dp[i-2]*2) % 10007;
		}
		System.out.println(dp[n]);
		in.close();
	}
}