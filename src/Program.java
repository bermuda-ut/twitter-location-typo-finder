import java.io.FileReader;
import java.io.IOException;
import java.io.BufferedReader;
import DT.*;

public class Program {

	public static void main(String[] args) throws IOException {
		FileReader	   dictFp, tweetFp;
		BufferedReader dictBf, tweetBf;
		double threshold;

		if(args.length < 3) {
			System.out.println("Usage:\njava Program <diciontary(location list) file> <search(tweet list) file> <Threshold %>");
			return;
		}

		try {
			dictFp  = new FileReader(args[0]);
			tweetFp = new FileReader(args[1]);
			threshold = Double.parseDouble(args[2]);
			dictBf  = new BufferedReader(dictFp);
			tweetBf = new BufferedReader(tweetFp);

		} catch(IOException e) {
			System.err.println("Unable to open dictionary and/or tweets");
			return;
		}

		Dictionary dict = new Dictionary(dictBf);
		TweetHandler tweet = new TweetHandler(tweetBf, dict, threshold);
		
		tweet.printResult();
	}
}
