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
			checkAlpha( checkStr );
		}

		System.out.println( strList.get(1) );

		
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

	static void checkAlpha( String checkStr ) {
		System.out.println( checkStr );
	}



}
