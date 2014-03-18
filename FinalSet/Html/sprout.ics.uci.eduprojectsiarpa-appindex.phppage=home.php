<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"><html><head><title>Automatic Privacy Protection Program</title><meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1"><link href="css/default.css" rel="stylesheet" type="text/css" title="default" media="all"><script type="text/javascript">  var _gaq = _gaq || [];  _gaq.push(['_setAccount', 'UA-17817850-1']);  _gaq.push(['_trackPageview']);  (function() {    var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true;    ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';    var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ga, s);  })();</script>
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
		<div class="title">IARPA-APP</div>
		<div class="subtitle">Automatic Privacy Protection Program </div>
	</div>

	
	
	<div id="sidebar">
	
		<div class="sidebarHeader">Site Pages</div>
	
		<div class="sidebarText">
			<ul>
			<li><a href="index.php?page=home.php">Home</a></li>
			<li><a href="index.php?page=code.php">Code</a></li>
			
            <li><a href="index.php?page=related.php">Related Work</a></li>
	 <li><a href="index.php?page=pubs.php">Publications</a></li>		</ul>
		</div>
	

		<div style="margin:10px; filter:light;"> <a href="http://www.uci.edu"><img src="images/uci_logo.png" width="100" border="0" alt="UCI"></a> </div>
	
	
	</div>

	<div id="main">
	
		
<h2>The Project</h2>
<p>The goals of IARPA's Automatic Privacy Protection program are to "develop and demonstrate practical,
sound automated methods for the use of private information retrieval techniques in Intelligence Community systems, 
to automatically protect the private data of untargeted individuals, to assure that mandated policies are enforced,
and to enable more effective interagency and intergovernmental data sharing for improved security."</p>

<p>The governemnt, through IARPA, is funding four research teams to develop innovative new
techniques for practical private information retrieval (PIR) and one team to develop techniques
for monitoring queries for policy assurance.</p>
</p>

<p></p>
<br>
<h2>UCI Team</h2>
<p><a href="http://www.ics.uci.edu/~stasio">Stanislaw Jarecki</a>, <a href="http://www.ics.uci.edu/~gts">Gene Tsudik</a> (Principal Investigators).<br>
<a href="http://www.ics.uci.edu/~edecrist">Emiliano De Cristofaro</a>, <a href="mailto:xiaominl@uci.edu">Xiaomin Liu</a>, <a href="http://www.ics.uci.edu/~yanbinl">Yanbin Lu</a>.</p>

<p></p>
<br>
<h2>Funding Grants</h2>
<p>This project is supported by the U.S. Intelligence Advanced Research Projects Activity under grant: FA8750-09-2-0071.</p>

	</div>
	
	
	<div id="footer">
		Webmaster <a href="http://www.ics.uci.edu/~edecrist">E. De Cristofaro</a>
	</div>


</div>
</body>

