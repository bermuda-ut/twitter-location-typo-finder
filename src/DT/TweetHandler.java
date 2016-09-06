package DT;

import java.io.IOException;
import java.io.BufferedReader;
import java.util.HashMap;
import java.util.Map;
import java.util.Set;
import java.util.Iterator;

public class TweetHandler {
	
	//private static final float THRESH_HOLD = 0.8f;
	private Map<String, String> result = new HashMap<String, String>();
	
	public void printResult() {
		int size = result.size();
		Set<String> keys = result.keySet();
		Iterator iterator = keys.iterator();
		
		while(iterator.hasNext()) {
			String k = (String) iterator.next();
			String v = result.get(k);
			if(v.length() > 0) {
				System.out.println(k + "\t" + v);
			}
		}
		
	}

	public TweetHandler(BufferedReader tweetBf, Dictionary dict, double threshold) throws IOException {
        int count = 0;
		String line;

        System.err.println("Loading Tweets..");
        String[] dictList = dict.getWords();

		while((line = tweetBf.readLine()) != null) {
			if(line.length() == 0)
				continue;
			System.err.println("#"+count+"\t"+line);
			String[] parts = line.split("\t");
			// userid tweetid tweet date
			String tweetId = parts[1];
			String[] words = parts[2].replaceAll("(\\.\\.)", " ").trim().split(" ");
			// people do this...often

			for(int i = 0; i < words.length; i++) {
				if(words[i].length() > 2) {
					// skip user names
					// words[i] = words[i].replaceAll("[^a-zA-z0-9]", "");
					if(result.containsKey(words[i])) {
						// skip if exists
						if(result.get(words[i]).length() != 0)
							result.put(words[i], result.get(words[i]) + " " + tweetId);
						continue;
					}

					result.put(words[i], "");
					// boolean first = true;
					boolean matched = false;

					for(int j = 0; j < Dictionary.dictLen; j++) {

						if(words[i].equals(dictList[j])) {
							// ignore exact match
							result.put(words[i], "");
							matched = false;
							break;
						}

						int score = EditDistance.globalEditDistance(words[i], dictList[j]);
						int wdlen = words[i].length();
						if(wdlen > 3 && score >= Math.floor(threshold * wdlen)) {
							/*
							if(first) {
								first = false;
								System.err.println("NEW WORD: " + words[i]);
							}

							result.put(words[i], result.get(words[i]) + dictList[j] + " ");
							System.err.println("MATCH WORD: " + dictList[j]);
							*/
							matched = true;
						}
					}
					
					//if(result.get(words[i]).length() != 0) {
                    if(matched) {
						result.put(words[i], result.get(words[i]) + "\t" + tweetId);
						System.err.println("> Identified " + words[i] + " as typo.");
					}
				}
			}
            count++;
		}
        System.err.println("Read " + count + " tweets.");
	}
}
