<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"><html><head><title>Security and Privacy in Genomics</title><meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1"><link href="css/default.css" rel="stylesheet" type="text/css" title="default" media="all">

<script type="text/javascript">

  var _gaq = _gaq || [];
  _gaq.push(['_setAccount', 'UA-23227607-1']);
  _gaq.push(['_trackPageview']);

  (function() {
    var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true;
    ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
    var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ga, s);
  })();

</script>

</head>


<script type="text/javascript">
<!--


  // this function is need to work around
  // a bug in IE related to element attributes
  function hasClass(obj) {
     var result = false;
     if (obj.getAttributeNode("class") != null) {
         result = obj.getAttributeNode("class").value;
     }
     return result;
  }

 function stripe(id) {

    // the flag we'll use to keep track of
    // whether the current row is odd or even
    var even = false;

    // if arguments are provided to specify the colours
    // of the even & odd rows, then use the them;
    // otherwise use the following defaults:
    var evenColor = arguments[1] ? arguments[1] : "#fff";
    var oddColor = arguments[2] ? arguments[2] : "#eee";

    // obtain a reference to the desired table
    // if no such table exists, abort
    var table = document.getElementById(id);
    if (! table) { return; }

    // by definition, tables can have more than one tbody
    // element, so we'll have to get the list of child
    // &lt;tbody&gt;s
    var tbodies = table.getElementsByTagName("tbody");

    // and iterate through them...
    for (var h = 0; h < tbodies.length; h++) {

     // find all the &lt;tr&gt; elements...
      var trs = tbodies[h].getElementsByTagName("tr");

      // ... and iterate through them
      for (var i = 0; i < trs.length; i++) {

        // avoid rows that have a class attribute
        // or backgroundColor style
        if (!hasClass(trs[i]) && ! trs[i].style.backgroundColor) {

         // get all the cells in this row...
          var tds = trs[i].getElementsByTagName("td");

          // and iterate through them...
          for (var j = 0; j < tds.length; j++) {

            var mytd = tds[j];

            // avoid cells that have a class attribute
            // or backgroundColor style
            //if (! hasClass(mytd) && ! mytd.style.backgroundColor) {

              mytd.style.backgroundColor = even ? evenColor : oddColor;

            //}
          }
        }
        // flip from odd to even, or vice-versa
        even =  ! even;
      }
    }
  }
// -->
</script><body>

<div class="page">

	<div id="header">
		<div class="title">S.P.I.G.</div>
		<div class="subtitle">Security and Privacy in Genomics</div>
	</div>

	
	
	<div id="sidebar">
	
		<div class="sidebarHeader">Site Pages</div>
	
		<div class="sidebarText">
			<ul>
			<li><a href="index.php?page=home.php">Home</a></li>
			<li><a href="index.php?page=code.php">Code</a></li>
			
<!--            <li><a href="index.php?page=related.php">Related Work</a></li> -->
	 <li><a href="index.php?page=pubs.php">Publications</a></li>		</ul>
		</div>
	

		<div style="margin:10px; filter:light;"> <a href="http://www.uci.edu"><img src="images/uci_logo.png" width="100" border="0" alt="UCI"></a> </div>
	
	
	</div>

	<div id="main">
	
		<h1>Publications</h1>
<p></p>
<ul>
<li>Emiliano De Cristofaro, Sky Faber, Gene Tsudik<br/>
<b><a href="http://www.emilianodc.com/PAPERS/WPES13.pdf" target="_blank">Secure Genomic Testing with Size- and Position-Hiding Private Substring Matching</a></b><br/>
12th ACM Workshop on Privacy in the Electronic Society (WPES 2013)</br><br>
</li>
<li>Erman Ayday, Emiliano De Cristofaro, Jean-Pierre Hubaux, Gene Tsudik<br>
<b><a href="http://arxiv.org/abs/1306.1264" TARGET="_blank">The Chills and Thrills of Whole Genome Sequencing</a></b><br>IEEE Computer, to appear, 2013<br>
Also presented as a poster at Usenix Security 2013 and discussed at HotSec 2013<br><br>
</li>
<li>Emiliano De Cristofaro, Sky Faber, Paolo Gasti, Gene Tsudik<br/>
<b><a href="http://www.emilianodc.com/PAPERS/WPES12.pdf" target="_blank">GenoDroid: Are Privacy-Preserving Genomic Tests Ready for Prime Time?</a></b><br/>
11th ACM Workshop on Privacy in the Electronic Society (WPES 2012)</br>
Media Coverage: [<a href="http://www.newscientist.com/article/mg21628896.300-want-to-keep-your-genome-safe-theres-an-app-for-that.html" target="_blank">NewScientist</a>]
[<a href="http://www.privacysurgeon.org/blog/incision/gene-genie-your-genome-may-soon-be-on-a-smartphone-app/" target="_blank">Privacy Surgeon</a>]
[<a href="http://news.uci.edu/features/gene-genie/" target="_blank">UCIrvine News</a>]
[<a href="http://www.ocregister.com/articles/dna-383823-genome-tsudik.html" target="_blank">OC Register</a>]
</br>
[<a href="http://www.computer.org/portal/web/news/home/-/blogs/smartphone-application-secures-dna-data" target="_blank">IEEE Computer Society</a>]
[<a href="http://mhealthwatch.com/new-app-makes-smartphone-a-secure-dna-data-bank-19442/" target="_blank">MHealthWatch</a>]
[<a href="http://www.fiercemobilehealthcare.com/story/smartphone-app-enables-secure-storage-testing-dna-data/2013-01-28" target="_blank">FierceMobileHealthCare</a>]
[<a href="http://blogs.ocweekly.com/navelgazing/2013/02/maury_may_be_able_to_say_you_a.php" target="_blank">OC Weekly</a>]
</br>
[<a href="http://news.uci.edu/press-releases/uci-app-safely-stores-dna-on-smartphones/" target="_blank">UCIrvine News</a>]
[<a href="http://www.scpr.org/programs/airtalk/2013/01/24/30221/are-you-my-father-theres-an-app-for-that/" target="_blank">KPCC</a>]
[<a href="http://ktla.com/2013/01/23/uci-develops-app-that-stores-dna-info-on-smartphones-2/#axzz2LNcmk9Ix" target="_blank">KTLA</a>]
[<a href="http://www.eweek.com/mobile/android-paternity-test-app-developed-by-uc-irvine-computer-scientists" target="_blank">eWEEK</a>]
[<a href="http://biotech.about.com/b/2013/01/26/safely-access-your-genetic-profile-on-your-smart-phone.htm" target="_blank">About</a>]
[<a href="http://mobihealthnews.com/21017/android-gene-test-presages-future-of-data-privacy/" target="_blank">MobiHealth News</a>]
<br>
<br>
</li>
<li>
Pierre Baldi, Roberta Baronio, Emiliano De Cristofaro, Paolo Gasti, Gene Tsudik <br>
<b><a href="http://arxiv.org/pdf/1110.2478.pdf" target="_blank">Countering GATTACA: Efficient and Secure Testing of Fully-Sequenced Human Genomes</a></b> <br>
18th ACM Conference on Computer and Communications Security (CCS 2011) <br/>
Media Coverage: [<a href="http://www.technologyreview.com/printer_friendly_blog.aspx?id=27252" target="_blank">MIT Technology Review</a>]
[<a href="http://www.newscientist.com/article/mg21228346.500-keeping-a-lid-on-your-digital-dna.html" target="_blank" target="_blank">NewScientist</a>]
[<a href="http://www.kurzweilai.net/how-cryptography-will-guarantee-genomic-privacy
" target="_blank">Kurzweilai</a>]
</li>
</ul>

<h2></h2>

<p></p>





	</div>
	
	
	<div id="footer">
		Webmaster <a href="http://www.ics.uci.edu/~fabers">S. Faber</a>
	</div>


</div>
</body>

