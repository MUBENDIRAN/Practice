class overriding{
	 void mube(int a,int b){
		System.out.println(a+b);
	}
	 void machi(int a,int b){
		System.out.println(a-b);
	}
	public static void main(String[] args){
		overriding obj = new overriding();
		obj.mube(6,8);
		obj.machi(6,8);
	}}

