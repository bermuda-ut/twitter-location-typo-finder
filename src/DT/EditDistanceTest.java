package DT;
import java.io.FileReader;
import java.io.IOException;
import java.io.BufferedReader;

import static org.junit.Assert.*;
import org.junit.Test;
import java.util.HashMap;
import java.util.Map;

public class EditDistanceTest {
	
	
	@Test
	public void testDict() throws IOException {
		String LOC = "/home/noxm/Bermuda/COMP30018Project1/geo/US-loc-names.txt-customized.txt";
		String COMP = "Bklyn";
		FileReader dictFp  = new FileReader(LOC);
		BufferedReader dictBf  = new BufferedReader(dictFp);
		Dictionary dict = new Dictionary(dictBf);

        String[] dictList = dict.getWords();
        for(int i = 0; i < dictList.length; i++) {
			int score = EditDistance.globalEditDistance(COMP, dictList[i]);
			int wdlen = COMP.length();
			if(wdlen > 3 && score >= Math.floor(0.7 * wdlen)) {
				System.out.println(dictList[i]);
			}
        }
	}

	//@Test
	public void testGlobalEditDistance() {
		String s1 = "Global";
		String s2 = "gluabl";
		int score = EditDistance.globalEditDistance(s1, s2);
		System.out.println(score);
	}
	
	//@Test
	public void hashMapTest() {
		Map<String, String> result = new HashMap<String, String>();
		System.out.println(
			result.put("test", "") + " " +
			result.put("test", result.get("test") + "asdf ") + " " +
			result.containsKey("test") + " " +
			result.put("test", result.get("test") + "asdf ")
		);
		System.out.println(result);
	}

}
