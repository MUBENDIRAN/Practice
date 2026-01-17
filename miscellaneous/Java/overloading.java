class overloading{
	static void mube(int a){
		System.out.println(a);
	}
	static void mube(String s){
		System.out.println(s);
	}
	static void mube(int a, int b){
		System.out.println(a+b);
	}
	public static void main(String[] args){
		mube(8);
		mube("tharun");
		mube(3,6);
	}
}
