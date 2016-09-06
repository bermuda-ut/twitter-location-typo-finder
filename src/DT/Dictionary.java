package DT;

import java.io.IOException;
import java.io.BufferedReader;

public class Dictionary {
    public static final int DICT_MAX_LEN = 1500000;
    private String[] words = new String[DICT_MAX_LEN];
    public static int dictLen = 0;

    public Dictionary(BufferedReader dictBf) throws IOException{
        int i = 0;
		String line;
        System.err.println("Loading Dict..");
		while((line = dictBf.readLine()) != null) {
            words[i] = line.replace("\n", "");
            i++;
		}
		dictLen = i;
        System.err.println("Read " + i + " words.");
    }
    
    public String[] getWords() {
    	return words;
    }
}