class linux{
	String bash;
	
	linux(String sh){
		bash = sh;
		System.out.println("Bash in Linux = "+bash);
	}
}
public class construct{
	public static void main(String[] args){
		linux linus = new linux("Love");
	}
}


