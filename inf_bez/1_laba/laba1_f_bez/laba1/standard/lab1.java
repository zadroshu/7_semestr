
public class lab1 {
	public static final String alphabet = "abcdefghijklmnopqrstuvwxyz";
	public static int shift = 3;

	private String f(int s,String text) {
		String rez = "";
		for (char c : text.toCharArray()) {
			if (c != ' ') {
				int i = alphabet.indexOf(c);
				i = (i + s*shift + alphabet.length()) % alphabet.length();
				rez = rez + alphabet.charAt(i);
			} else
				rez = rez + " ";
		}
		return rez;
	}
	
	public String crypt(String text) {
		return f(1,text);
	}

	public String decrypt(String text) {
		return f(-1,text);
	}

	public static void main(String[] args) {
		lab1 l=new lab1();
		String c_text=l.crypt("hello world");
		System.out.println(c_text);
		System.out.println(l.decrypt(c_text));
	}

}
