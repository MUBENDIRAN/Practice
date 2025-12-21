import java.util.Scanner;
public class Studentrank{
	public static void main(String[] args){
		Scanner sc = new Scanner(System.in);

		System.out.println("Enter the Number of Students");
		int n = sc.nextInt();
		sc.nextLine();
		String [] names = new String[n];
		double [] avg = new double[n];
		for(int i = 0;i<n;i++){
			System.out.println("\n--- Student "+ (i+1) + "---");
			System.out.print("Enter the name:");
			names[i] = sc.nextLine();
			System.out.println("Enter the marks of 5 subjects(0-100)");
		int s1 = sc.nextInt();
		int s2 = sc.nextInt();
		int s3 = sc.nextInt();
		int s4 = sc.nextInt();
		int s5 = sc.nextInt();
		sc.nextLine();
		int total = s1+s2+s3+s4+s5;
		avg[i] = total/5.0;
		}
	for(int i = 0;i < n;i++){
		for(int j = 0;j < n-1;j++){
			if ( avg[j] < avg[j+1]){
				double tempavg = avg[j];
				avg[j] = avg[j+1];
				avg[j+1] = tempavg;
				String tempname = names[j];
				names[j] = names[j+1];
				names[j+1] = tempname;
			}
		}
	}
	System.out.println("\n === Ranking ===");
	for (int i = 0;i < n;i++){

		String grade;
		switch ((int)(avg[i]/10)){
			case 10:
				grade = "S";
				break;
			case 9:
				grade = "O";
				break;
			case 8:
				grade = "A+";
				break;
			case 7:
				grade = "A";
				break;
			case 6:
				grade = "B+";
				break;
			case 5:
				grade = "B";
				break;
			case 4:
				grade = "C";
				break;
			default:
				grade = "RA";
				break;
	}
	System.out.printf("%d,%s (Avg:%.1f)-%s%n",i+1,names[i],avg[i],grade);
	}
	sc.close();
}
}

