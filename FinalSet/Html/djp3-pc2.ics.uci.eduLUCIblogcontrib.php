<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
<title>I want to tell the world about my accepted paper</title>
<style>	
input.paper-attrib {
	width: 48em;
	font-family: Arial, Helvetica, sans-serif;
}
textarea {
	width: 100%;
	height: 24em;
}
table td {
	padding: 2px;
}
.paper-image {
	float:left;
	margin: 0 10px 10px 0;
}
</style>
</head>
<body>
<h1>Accepted paper details</h1>
<form id="paperForm" action="verify.php" method="post">
<table>
  <tr>
    <td>Name an animal that is known for wagging its tail (all lowercase):</td>
    <td><input type="text" class="paper-attrib" name="human"></td>
  </tr>
  <tr>
    <td>Title Of Paper (e.g., "Status On Display: A Field Trial of Nomatic*Viz"):</td>
    <td><input type="text" class="paper-attrib" name="title"></td>
  </tr>
  <tr>
    <td>Names to congratulate in the title (e.g., "Sharon and Don"):</td>
    <td><input type="text" class="paper-attrib" name="congrats"></td>
  </tr>
  <tr>
    <td>Authors/Collaborators and affiliations (e.g., "Informatics graduate student
	Sharon Ding and informatics faculty Don Patterson"):</td>
    <td><input type="text" class="paper-attrib" name="author"></td>
  </tr>
  <tr>
    <td>Conference/Venue (e.g., "ECSCW 2009"):</td>
    <td><input type="text" class="paper-attrib" name="venue"></td>
  </tr>
  <tr>
    <td>Image URL (the default is fine):</td>
    <td><input type="text" class="paper-attrib" name="image"
	value="http://luci.ics.uci.edu/wp-uploads/2010/05/82648953_f1b71703ef_m.jpg"></td>
  </tr>
  <tr>
    <td>Image credit (the default is fine):</td>
    <td><input type="text" class="paper-attrib" name="image-credit"
	value="<a href='http://www.flickr.com/photos/paulworthington/82648953/'>paulworthington</a>"></td>
  </tr>
  <tr>
    <td style="padding-top: 20px">What's a url that people can get a copy of the paper from? (e.g.,http://dx.doi.org/10.1016/j.artint.2007.01.006")
    </td>
    <td><input type="text" class="paper-attrib" name="paperURL"></td>
  </tr>
  <tr>
    <td style="padding-top: 20px">What's it about? (e.g.,"This paper describes
	their deployment of the status visualization last year for several months."
	or "Abstract: ...."):</td>
  </tr>
  <tr>
    <td colspan="2"><textarea name="abstract"></textarea></td>
  </tr>
  <tr>
    <td colspan="2" align="right">
<script type="text/javascript" src="http://www.google.com/recaptcha/api/challenge?k=6LfPiMQSAAAAAMUe9VvkPYhhSZy8j4sJuKdBtEiM"></script>

	<noscript>
  		<iframe src="http://www.google.com/recaptcha/api/noscript?k=6LfPiMQSAAAAAMUe9VvkPYhhSZy8j4sJuKdBtEiM" height="300" width="500" frameborder="0"></iframe><br/>
  		<textarea name="recaptcha_challenge_field" rows="3" cols="40"></textarea>
  		<input type="hidden" name="recaptcha_response_field" value="manual_challenge"/>
	</noscript>    </td>
  <tr>
    <td colspan="2" align="right"><input id="submitBtn" type="submit" value="Submit"></td>
  </tr>
</table>
</form>
<p>Roughly a sample of what is produced after it is manually editted:</p>
<h4>Congratulations to Sharon and Don! (ECSCW 2009 paper)</h4>
<table border="1">
<tr>
  <td>
  <img alt="penAndPaper.jpg" src="http://luci.ics.uci.edu/blog/archives/penAndPaper.jpg" width="240" height="180" /><br/>
Photo courtesy of
<a href="http://www.flickr.com/photos/paulworthington/82648953/">paulworthington</a>
                </td>
<td>
<p>
Congratulations to Informatics graduate student Sharon Ding and informatics faculty Don Patterson on having their paper, "Status On Display: A Field Trial of Nomatic*Viz "
Nomatic*Viz accepted to ECSCW 2009.  This paper describes their deployment of the status visualization last year for several months. 
</p>
<p>Get a copy from here: http://www.mydomain.com/mypaper.pdf</p>
</td>
</tr>
</table>

<script>
var pForm = document.getElementById("paperForm");
pForm.onsubmit = function () {
	if (pForm.title.value==""||pForm.congrats.value=""||pForm.author.value==""||pForm.venue.value==""||pForm.abstract.value=="") {
		alert("Please complete all required fields.");
		return false;
	} else {
		paperForm.submit();
	}
}
</script>
</body>
</html>

