<!DOCTYPE html 
    PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" 
    "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html>
<head>
  <title>SLI | Classes-2008F / Flocking | Attach</title>
  <meta http-equiv='Content-Style-Type' content='text/css' />
  <link rel='stylesheet' href='http://sli.ics.uci.edu/pmwiki/pub/skins/custom/pmwiki.css' type='text/css' />
  <!--HTMLHeader--><style type='text/css'><!--
  ul, ol, pre, dl, p { margin-top:0px; margin-bottom:0px; }
  code.escaped { white-space: nowrap; }
  .vspace { margin-top:1.33em; }
  .indent { margin-left:40px; }
  .outdent { margin-left:40px; text-indent:-40px; }
  a.createlinktext { text-decoration:none; border-bottom:1px dotted gray; }
  a.createlink { text-decoration:none; position:relative; top:-0.5em;
    font-weight:bold; font-size:smaller; border-bottom:none; }
  img { border:0px; }
  .editconflict { color:green; 
  font-style:italic; margin-top:1.33em; margin-bottom:1.33em; }

  table.markup { border:2px dotted #ccf; width:90%; }
  td.markup1, td.markup2 { padding-left:10px; padding-right:10px; }
  table.vert td.markup1 { border-bottom:1px solid #ccf; }
  table.horiz td.markup1 { width:23em; border-right:1px solid #ccf; }
  table.markup caption { text-align:left; }
  div.faq p, div.faq pre { margin-left:2em; }
  div.faq p.question { margin:1em 0 0.75em 0; font-weight:bold; }
  div.faqtoc div.faq * { display:none; }
  div.faqtoc div.faq p.question 
    { display:block; font-weight:normal; margin:0.5em 0 0.5em 20px; line-height:normal; }
  div.faqtoc div.faq p.question * { display:inline; }
   
    .frame 
      { border:1px solid #cccccc; padding:4px; background-color:#f9f9f9; }
    .lfloat { float:left; margin-right:0.5em; }
    .rfloat { float:right; margin-left:0.5em; }
a.varlink { text-decoration:none; }

--></style>
  <link href='http://sli.ics.uci.edu/pmwiki/pub}/commentboxplus/commentboxplus.css' rel='stylesheet' type='text/css' />  <meta name='robots' content='noindex,nofollow' />

</head>
<body>
<!--PageHeaderFmt-->
  <div id='wikilogo'><a href='http://sli.ics.uci.edu'><img src='/pmwiki/pub/skins/custom/SLI_white.png'
    alt='SLI' border='0' /></a></div>
  <div id='wikihead'>
  <form action='http://sli.ics.uci.edu'>
    <!-- <span class='headnav'><a href='http://sli.ics.uci.edu/Classes-2008F/RecentChanges'
      accesskey='c'>Recent Changes</a> -</span> --> 
    <input type='hidden' name='n' value='Classes-2008F.Flocking' />
    <input type='hidden' name='action' value='search' />
    <!-- <a href='http://sli.ics.uci.edu/Site/Search'>Search</a>: -->
    <input type='text' name='q' value='' class='inputbox searchbox' />
    <input type='submit' class='inputbutton searchbutton'
      value='Search' />
    <a href='http://sli.ics.uci.edu/Site/Search'>(?)</a>
  </form></div>
<!--/PageHeaderFmt-->
  <table id='wikimid' width='100%' cellspacing='0' cellpadding='0'><tr>
<!--PageLeftFmt-->
      <td id='wikileft' valign='top'>
        <ul><li><a class='wikilink' href='http://sli.ics.uci.edu/Classes/Classes'>Classes</a>
</li><li><a class='wikilink' href='http://sli.ics.uci.edu/Group/Group'>Group</a>
</li><li><a class='wikilink' href='http://sli.ics.uci.edu/Projects/Projects'>Research</a>
</li><li><a class='urllink' href='http://www.ics.uci.edu/~ihler/pubs.html' title='' rel='nofollow'>Publications</a>
</li><li><a class='wikilink' href='http://sli.ics.uci.edu/Code/Code'>Code</a>
</li></ul><div class='vspace'></div><hr />
<div class='vspace'></div>
</td>
<!--/PageLeftFmt-->
      <td id='wikibody' valign='top'>
<!--PageActionFmt-->
        <div id='wikicmds'><ul><li class='browse'><a class='wikilink' href='http://sli.ics.uci.edu/Classes-2008F/Flocking?action=login'>login</a>
</li></ul>
</div>
<!--PageTitleFmt-->
        <div id='wikititle'>
          <div class='pagegroup'><a href='http://sli.ics.uci.edu/Classes-2008F'>Classes-2008F</a> /</div>
          <h1 class='pagetitle'>Flocking</h1></div>
<!--PageText-->
<div id='wikitext'>
<p><strong>Password required</strong>
</p>
<form action='/Classes-2008F/Flocking?action=upload&upname=test_flock.m' method='post' 
    name='authform'>
<p>Name: <input type='text' name='authid' class='inputbox' /><br />Password: <input type='password' name='authpw' class='inputbox' />
<input type='submit' value='OK' class='inputbutton' />
</p></form>
<script language='javascript' type='text/javascript'><!--
    try { document.authform.authid.focus(); }
    catch(e) { document.authform.authpw.focus(); } //--></script></div>

      </td>
    </tr></table>
<!--PageFooterFmt-->
  <div id='wikifoot'>
    <div class='footnav' style='float:left'> Last modified November 04, 2008, at 04:14 PM</div>
    <div class='footnav' style='float:right; text-align:right'>
    <a href="http://www.ics.uci.edu">Bren School of Information and Computer Science</a><br>
    <a href="http://www.uci.edu">University of California, Irvine</a>
    </div>
  </div>
<!--HTMLFooter--><script type="text/javascript">
  var _gaq = _gaq || [];
  _gaq.push(["_setAccount", "UA-24148957-2"]);
	_gaq.push(["_trackPageview"]);
	(function() {
	  var ga = document.createElement("script"); ga.type = "text/javascript"; ga.async = true;
	  ga.src = ("https:" == document.location.protocol ? "https://ssl" : "http://www") + ".google-analytics.com/ga.js";
	  var s = document.getElementsByTagName("script")[0]; s.parentNode.insertBefore(ga, s);
	  })();
</script>
</body>
</html>

