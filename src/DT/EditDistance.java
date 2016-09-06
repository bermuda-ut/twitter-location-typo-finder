package DT;

public class EditDistance {
	public static int editDistance(String f, String t, int i, int d, int r, int m) {
		int lf = f.length(),
			lt = t.length();
		int A[][] = new int[lt+1][lf+1]; // lt rows, lf columns

		for (int j = 1; j <= lf; j++) A[0][j] = j * d;
		for (int k = 1; k <= lt; k++) A[k][0] = k * i;
		
		for(int j = 1; j <= lt; j++) {
			for(int k = 1; k <= lf; k++) {
				int q = (f.charAt(k-1) == t.charAt(j-1)) ? m : r;
				A[j][k] = max(A[j][k-1] + d,
							A[j-1][k] + i,
							A[j-1][k-1] + q);
			}
		}

		//print2D(A);
		
		return A[lt][lf];
	}
	
	public static int globalEditDistance(String f, String t) {
		return editDistance(f, t, -1, -1, -1, 1);
	}
	
	private static int max(int i1, int i2, int i3) {
		int max = i1;
		if(i2 > max)
			max = i2;
		if(i3 > max)
			max = i3;
		return max;
	}
	
	public static void print2D(int[][] A) {
		for(int i = 0; i < A.length; i++) {
			for(int j = 0; j < A[i].length; j++) {
				System.out.printf("%3d ", A[i][j]);
			}
			System.out.printf("\n");
		}
	}
}
