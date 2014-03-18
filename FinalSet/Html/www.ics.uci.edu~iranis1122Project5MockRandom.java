From: "Saved by Windows Internet Explorer 8"
Subject: 
Date: Thu, 12 May 2011 22:16:12 -0700
MIME-Version: 1.0
Content-Type: text/html;
	charset="utf-8"
Content-Transfer-Encoding: quoted-printable
Content-Location: http://www.ics.uci.edu/~ehenniga/ics22/projects/project5/MockRandom.java
X-MimeOLE: Produced By Microsoft MimeOLE V6.1.7600.16776

=EF=BB=BF<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0 Transitional//EN">
<HTML><HEAD>
<META content=3D"text/html; charset=3Dutf-8" http-equiv=3DContent-Type>
<META name=3DGENERATOR content=3D"MSHTML 8.00.7600.16766"></HEAD>
<BODY><PRE>// MockRandom.java
//
// ICS 22 / CSE 22 Winter 2011
// Project #5: Signal to Noise
//
// This is a "mock object" that behaves sort of like a Random object =
from the
// Java library, except that it returns a predetermined sequence of =
numbers,
// rather than choosing the numbers randomly.  While this wouldn't be a =
good
// thing to use in our random sentence generation program, it's a great =
help
// in testing, because it allows us to pass a "mock" random number =
generator
// into the sentence generation algorithm which will ultimately give us =
output
// that we can predict.
//
// An example of using MockRandom follows:
//
//     ArrayList&lt;Integer&gt; a =3D new ArrayList&lt;Integer&gt;();
//     a.add(5);
//     a.add(7);
//     a.add(9);
//
//     // This MockRandom will generate the numbers 5, 7, 9 in sequence,
//     // repeating, forever.
//     MockRandom mr =3D new MockRandom(a);
//
//     // The output here will be 5, 7, 9, 5, 7, 9, 5.
//     for (int i =3D 0; i &lt; 7; i++)
//         System.out.println(mr.nextInt());

import java.util.ArrayList;
import java.util.Random;


public class MockRandom extends Random
{
	private ArrayList&lt;Integer&gt; results;
	private int nextNum;


	public MockRandom(ArrayList&lt;Integer&gt; results)
	{
		this.results =3D results;
		nextNum =3D 0;
	}
=09

	public int nextInt()
	{
		int nextResult =3D Math.abs(results.get(nextNum));
		nextNum =3D (nextNum + 1) % results.size();
		return nextResult;
	}
=09
=09
	public int nextInt(int n)
	{
		return Math.abs(nextInt()) % n;
	}
}
</PRE></BODY></HTML>

