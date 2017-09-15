import java.util.*;
import java.io.*;

public class Q1_LettersNotUsed {

	public static void main( String[] args ) {
		Scanner scanner = new Scanner( System.in );
		System.out.print( "Input cases: " );
		int numOfCase = scanner.nextInt();

		ArrayList<String> strList = addStr( numOfCase );

		for ( int i=0; i<numOfCase; i++ ) {
			String checkStr = strList.get(i);
			checkAlpha( checkStr, i );
		}

		System.out.println();

		
	}

	static ArrayList<String> addStr( int numOfCase ) {
		int strCount = 0;
		ArrayList<String> strList = new ArrayList<>();
		while ( strCount < numOfCase ) {
			System.out.print( "Input string #" + (strCount+1) + ": " );
			Scanner scanner = new Scanner( System.in );
			strList.add( scanner.next() );
			strCount += 1;
		
		}
		return strList;
	}

	static void checkAlpha( String checkStr, int i ) {

		checkStr = checkStr.toLowerCase();
		ArrayList<String> alphaList = new ArrayList<>(Arrays.asList("a", "b", "c", "d", "e"));
		System.out.println();

		for ( int j=4; j>-1; j-- ) {
			String alphaStr = alphaList.get(j);
			char alpha = alphaStr.charAt(0);
			System.out.println("char alpha: " + alpha);

			for ( int k=0; k<checkStr.length(); k++ ) {
				if ( alpha == checkStr.charAt(k) ) {
					alphaList.remove(j);
					System.out.println(alphaList);
					break;
				}
			}
		}
		System.out.println();
		System.out.print( "Letters missing in case #" + (i+1) + ": " );

		for ( int l=0; l<alphaList.size(); l++ ) System.out.print( alphaList.get(l) );
	}



}
