/*
 * 2015 CCSC Student Programming Contest
 *
 * < Problem 1 -- Letters Not Used >
 * For this problem, you are interested in displaying a list of all letters that do not
 * appear in a given input string. The letters in the output will be lowercase,
 * regardless of the case letters in the input string.
 *
 * < Input >
 * The first line of input contains a single integer n, (1 <= n <= 1000), which is the
 * number of test cases follow. Each test case consists of a single line of input
 * containing a string. Each string is of length n, (1 <= n <= 80). All input strings will
 * consist solely of letters and spaces, no punctuation or special symbols.
 *
 * < Output >
 * For each case, you should print out the statement:
 *	Letters missing in case x:
 * where x is the case number. Place a colon immediately after the case number along with
 * a single space. This is followed by all the letters which are not used in the input.
 * All letters should be lowercase and in ascending sorted order from a to z.
 *
 * < Sample Input >
 * 5
 * The quick brown fox jumped over the lazy dog
 * How much better wood would a woodchuck chuck today than yesterday
 * A skunk sat on a stump and thunk the stump stunk
 * Pack my box with five dozen liquor jugs
 * Razorback jumping frogs can level six piqued gymnasts
 *
 * < Output Corresponding to Sample Input >
 * Letters missing in case #1: s
 * Letters missing in case #2: fgijpqvxz
 * Letters missing in case #3: bcfgijlqrvwxyz
 * Letters missing in case #4: 
 * Letters missing in case #5: hw
 *											 
 */


import java.util.*;
import java.io.*;

public class Y15_01_LettersNotUsed {

	public static void main( String[] args ) {
		//input the cases to check;
		//call function addStr to add case by case to array list;
		System.out.print( "Input cases: " );
		Scanner scanner = new Scanner( System.in );
		int numOfCase = scanner.nextInt();
		ArrayList<String> strList = addStr( numOfCase );

		//for each case, call function checkAlpha to check missing alphabets;
		for ( int i=0; i<numOfCase; i++ ) {
			String str = strList.get(i);
			checkAlpha( str, i );
		}

		System.out.println();
	}

	//(Function)addStr: add case by case to an array list; return the array list to main;
	static ArrayList<String> addStr( int numOfCase ) {
		int strCount = 0;
		ArrayList<String> strList = new ArrayList<>();

		while ( strCount < numOfCase ) {
			System.out.print( "Input string #" + (strCount+1) + ": " );
			Scanner rawInStr = new Scanner( System.in );
			String inStr = rawInStr.nextLine();
			strList.add( inStr );
			strCount += 1;
		
		}

		return strList;
	}

	//check missing letters for each case;
	static void checkAlpha( String str, int i ) {

		str = str.toLowerCase();
		ArrayList<String> alphaList = new ArrayList<>(Arrays.asList("a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"));

		for ( int j=25; j>-1; j-- ) {
			String alphaStr = alphaList.get(j);
			char alphabet = alphaStr.charAt(0);

			for ( int k=0; k<str.length(); k++ ) {
				if ( (alphabet==str.charAt(k)) ) {
					alphaList.remove(j);
					break;
				}
			}
		}

		System.out.println();
		System.out.print( "Letters missing in case #" + (i+1) + ": " );

		for ( int l=0; l<alphaList.size(); l++ ) System.out.print( alphaList.get(l) );
	}
}
