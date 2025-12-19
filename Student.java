import java.util.Scanner;
public class Student{
	public static void main(String[] args){
		Scanner sc = new Scanner(System.in);

		System.out.println("Enter the Name");
		String name = sc.nextLine();
		System.out.println("Enter the marks of 5 subjects(0-100):");
		int s1 = sc.nextInt();
		int s2 = sc.nextInt();
		int s3 = sc.nextInt();
		int s4 = sc.nextInt();
		int s5 = sc.nextInt();
		int total = s1+s2+s3+s4+s5;
		double avg = total/5.0;
		String grade;
		switch ((int)(avg/10)){
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
	System.out.println("Name = " + name);
	System.out.println("Total = " + total);
	System.out.println("Avg = " + avg);
	System.out.println("Grade = " + grade);
	sc.close();
}
}

