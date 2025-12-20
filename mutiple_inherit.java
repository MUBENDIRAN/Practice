interface camp{
	void camp();
}
interface coding{
	void coding();
}
class inter implements camp,coding{
	public void camp(){
		System.out.println("Placement and training");
	}
	public void coding(){
		System.out.println("Technical and Coding assesment");
	 }}
public class mutiple_inherit{
	public static void main(String[] args){
		inter mi = new inter();
		mi.camp();
		mi.coding();
	}
}

