class assembly{
	void machine_lang(){
		System.out.println("The father of coding");
	}
}
class C extends assembly{
	void low_lang(){
		System.out.println("The Son of coding");
	}
}
class java extends C{
	void high_lang(){
		System.out.println("Son of low_lang and grandson of machine_lang");
	}
}
public class multi_level{
	public static void main(String[] args){
		java ja = new java();
		ja.machine_lang();
		ja.low_lang();
		ja.high_lang();
	}
}

