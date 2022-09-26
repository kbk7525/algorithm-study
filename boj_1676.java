package boj;

import java.util.Scanner;

public class boj_1676 {
	public static void main(String[] args) {
		Scanner in = new Scanner(System.in);
		int num = in.nextInt();
		int cnt = 0;
		//규칙을 찾아서 5 10 15.. 일때 0의 갯수가 1씩 늘어났음
		while(num >= 5) {
			cnt += num/5;
			num /= 5;
		}
		System.out.println(cnt);
		in.close();
	}
}