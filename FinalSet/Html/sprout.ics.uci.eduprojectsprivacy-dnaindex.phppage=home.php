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
	
		
<h2>Highligts</h2>
<p> Recent advances in DNA sequencing technologies have put ubiquitous availability of fully sequenced human genomes within reach. It is no longer hard to imagine the day when everyone will have the means to obtain and store one's own DNA sequence. Widespread and affordable availability of fully sequenced genomes immediately opens up important opportunities in a number of health-related fields. In particular, common genomic applications and tests performed in vitro today will soon be conducted computationally, using digitized genomes. New applications will be developed as genome-enabled medicine becomes increasingly preventive and personalized. However, this progress also prompts significant privacy challenges associated with potential loss, theft, or misuse of genomic data. </p>
<p>We begin to address genomic privacy by focusing on a number of important applications: Paternity Tests, Ancestry Testing, Personalized Medicine, and Genetic Compatibility Tests. We investigate real-world practicality and usability of (as well as interest in) some of proposed privacy-preserving genomic tests.</p>
<p>Motivated by both medical and social applications, we aim to test viability of privacy-agile computational genomic tests in a portable and pervasive setting of modern smartphones. We also design a personal genomic toolkit (called GenoDroid) and implement it on the Android platform.</p>
<p>FatherFinder &ndash; an Android app that, on input of two simulated genomes, compute the paternal lineage between the two without revealing any other information about either parties DNA, is available from <a href="https://play.google.com/store/apps/details?id=com.fatherfinder" target="_blank">Google Play</a>.
</p>


<p></p>
<br>
<h2>People</h2>
<ul>
<li><a href="http://www.emilianodc.com" target=_blank>Emiliano De Cristofaro</a>, Computer Science Dept., University College London</li>
<li><a href="http://www.ics.uci.edu/~fabers" target=_blank>Sky Faber</a>, Computer Science Dept., UC Irvine</li>
<li><a href="http://www.6nelweb.com/bio/" target=_blank>Paolo Gasti</a>, Computer Science Dept., New York Institute of Technology</li>
<li><a href="http://www.ics.uci.edu/~gts" target=_blank>Gene Tsudik</a>, Computer Science Dept., UC Irvine</li>
</ul>

<h2>Collaborators</h2>
<ul>
<li><a href="http://www.igb.uci.edu/~pfbaldi" target=_blank>Pierre Baldi</a>, Institute for Genomics and Bioinformatics., UC Irvine</li>
<li><a href="mailto:rbaronio@uci.edu" target=_blank>Roberta Baronio</a>, Institute for Genomics and Bioinformatics., UC Irvine</li>
</ul>	</div>
	
	
	<div id="footer">
		Webmaster <a href="http://www.ics.uci.edu/~fabers">S. Faber</a>
	</div>


</div>
</body>

