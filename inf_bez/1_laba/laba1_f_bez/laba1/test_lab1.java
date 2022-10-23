import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Test;

class test_lab1 {

	@Test
	void test_crypto() {
		lab1 l=new lab1();
		String text="Lorem ipsum dolor sit amet consectetur adipiscing elit sed do eiusmod tempor incididunt ut labore et dolore magna aliqua Ut enim ad minim veniam quis nostrud exercitation ullamco laboris nisi ".toLowerCase();
		String _text= l.crypt(text);
		String result=l.decrypt(_text);
		System.out.println("test 1");
		System.out.println("	original:  "+text);
		System.out.println("	crypt   :  "+_text);
		System.out.println("	decrypt :  "+result);	
		assertEquals(text, result);
	}

	@Test
	void test_crypto_enhanced() {
		lab1 l=new lab1();
		boolean rez=true;
		String text="Lorem ipsum dolor sit amet consectetur adipiscing elit sed do eiusmod tempor incididunt ut labore et dolore magna aliqua Ut enim ad minim veniam quis nostrud exercitation ullamco laboris nisi ".toLowerCase();
		String _text= l.crypt(text);
		System.out.println("test 2");
		int d[]=new int[10];
		for(int i=0;i<d.length;i++) {
			int ind=(int)(Math.random()*text.length());
			if(text.charAt(ind)==' ') continue;
			d[i]=text.charAt(ind)-_text.charAt(ind);
			System.out.print(text.charAt(ind)-_text.charAt(ind) + " ");
			if(i>0) rez = rez && d[i]==d[i-1]; 
		}
		assert(!rez);
	}

	
	
}
