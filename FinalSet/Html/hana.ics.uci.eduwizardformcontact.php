<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<title>Wizard Collaboration Survey Interest Form</title>
<link href="css/form.css" rel="stylesheet" type="text/css" />
<style type="text/css">
<!--
#other, #fundingsource {
	display:none;
}
-->
</style>
<script type="text/javascript" src="functions/WA_validation.js"></script>
</head>
<body>
<div id="content">
  <div id="bnr"><img  src="images/top.jpg" width="845" height="187" alt="Collaboration Success Wizard" /></div>
  <h1>Application for a Wizard Study</h1>
  <div class="formdesc">
    <p>This form is specifically intended for projects applying to the Collaboration Success Wizard steering committee to conduct a study of their project. More general inquiries can be addressed via email to
      <script type="text/javascript" src="functions/Hana-email.js"></script>.</p>
    <p>For purposes here, a "study" consists of the following:</p>
    <ol>
      <li>a recruitment period, in which project members are introduced to the study and are invited to participate in
        the study;</li>
      <li>a study period in which project members respond to the Wizard survey;</li>
      <li>upon completion of the Wizard, each respondent will immediately receive feedback tailored to their
        individual responses;</li>
      <li>following the end of the study period, the Wizard analysis team will examine the data aggregated over all
        respondents for this project and will prepare a report to the entire project about potential vulnerabilities
        that could threaten the success of their collaboration, as well as possible interventions to mitigate the
        identified vulnerabilities.</li>
    </ol>
  </div>
  <img src="images/required_star.gif" width="10" height="10" alt="asterisk" /> marks required fields
  <form action="/wizard/form/contact.php?" method="POST" name="form1" class="left" id="form1" onsubmit="WAValidateRQ(document.forms[0].Name,'-Fields with red stars are required.',document.forms[0].Name,0,false,'text');WAValidateRQ(document.forms[0].Institution,'-Fields with red stars are required.',document.forms[0].Institution,0,false,'text');WAValidateRQ(document.forms[0].Email,'-Fields with red stars are required.',document.forms[0].Email,0,false,'text');WAValidateEM(document.forms[0].Email,document.forms[0].Email.value,'- Invalid email address',document.forms[0].Email,0,true);WAValidateRQ(document.forms[0].Phone,'-Fields with red stars are required.',document.forms[0].Phone,0,false,'text');WAValidatePN(document.forms[0].Phone,'- Invalid phone number',false,true,'x-xxx-xxx-xxxx',document.forms[0].Phone,0,true);WAValidateRQ(document.forms[0].ProjectName,'-Fields with red stars are required.',document.forms[0].ProjectName,0,false,'text');WAValidateRQ(document.forms[0].ProjectStatus,'-Fields with red stars are required.',false,0,true,'radio');WAValidateRQ(document.forms[0].ProjectFunding,'-Fields with red stars are required.',false,0,true,'radio');WAValidateRQ(document.forms[0].StartDate,'-Fields with red stars are required.',document.forms[0].StartDate,0,true,'text');WAValidateRQ(document.forms[0].EndDate,'-Fields with red stars are required.',document.forms[0].EndDate,0,true,'text');WAValidateRQ(document.forms[0].Role,'-Fields with red stars are required.',document.forms[0].Role,0,true,'text');WAValidateRQ(document.forms[0].Participants,'-Fields with red stars are required.',document.forms[0].Participants,0,true,'textarea');WAValidateRQ(document.forms[0].NbrParticipants,'-Fields with red stars are required.',document.forms[0].NbrParticipants,0,true,'text');WAValidateNM(document.forms[0].NbrParticipants,'- Invalid integer format',1,1000,0,'','',',.',document.forms[0].NbrParticipants,0,true);WAValidateRQ(document.forms[0].WorkLocation,'-Fields with red stars are required.',false,0,true,'radio');WAValidateRQ(document.forms[0].AuthorityName,'-Fields with red stars are required.',document.forms[0].AuthorityName,0,true,'text');WAValidateRQ(document.forms[0].SurveyWilling,'-Fields with red stars are required.',false,0,true,'radio');WAValidateRQ(document.forms[0].Description,'-Fields with red stars are required.',document.forms[0].Description,0,true,'textarea');WAValidateRQ(document.forms[0].AuthorityContact,'- Fields with red stars are required.',document.forms[0].AuthorityContact,0,false,'text');WAAlertErrors('The following errors were found','Correct invalid entries to continue',true,false,false);return document.MM_returnValue">
    <label class="left" for="Name">Your Name <em><img src="images/required_star.gif"        
alt="required" /></em></label>
    <input name="Name" type="text" id="Name" maxlength="64" value="" />
    <br />
    <label  class="left" for="Institution">Your Institution <em><img src="images/required_star.gif"        
alt="required" /></em></label>
    <input name="Institution" type="text" id="Institution" maxlength="128" value="" />
    <br />
    <label class="left" for="Email">Email <em><img src="images/required_star.gif"        
alt="required" /></em></label>
    <input name="Email" type="text" id="Email" maxlength="128" value="" />
    <br />
    <label class="left" for="Phone">Phone <em><img src="images/required_star.gif"        
alt="required" /></em> </label>
    <input name="Phone" type="text" id="Phone" maxlength="32" value="" />
    <br />
    <label class="left" for="ProjectName">Project Name <em><img src="images/required_star.gif"        
alt="required" /></em></label>
    <input name="ProjectName" type="text" id="ProjectName" size="30" maxlength="64" value="" />
    <br />
    <div class="left">Project Status: Check one: <em><img src="images/required_star.gif"        
alt="required" /></em></div>
    <input name="ProjectStatus" type="radio" id="Past" value="Past" />
    <label for="Past">Ended, in the past</label>
    <input name="ProjectStatus" type="radio" id="Present" value="Present" />
    <label for="Present">Ongoing, in the present</label>
    <input name="ProjectStatus" type="radio" id="Proposed" value="Proposed" />
    <label for="Proposed">Proposed, for the future</label>
    <br />
    <div class="left">Project Funding: Check one: <em><img src="images/required_star.gif"        
alt="required" /></em></div>
    <input name="ProjectFunding" type="radio" id="Funded" value="Funded" onclick="ShowFS()" />
    <label for="Funded">Funded</label>
    <input name="ProjectFunding" type="radio" id="Pending" value="Pending" onclick="ShowFS()" />
    <label for="Pending">Pending</label>
    <input name="ProjectFunding" type="radio" id="Unfunded" value="Unfunded" onclick="HideFS()" />
    <label for="Unfunded">Unfunded</label>
    <br />
    <div id="fundingsource">
      <div class="left">Funding Source: If Funded or Pending <em><img src="images/required_star.gif"        
alt="required" /></em></div>
      <input name="NPFundedYN" type="checkbox" id="NPFundedYN"   value="Yes" onclick="CheckOther()" />
      <label for="NPFundedYN">Non-Profit</label>
      <input name="GovtFundedYN" type="checkbox" id="GovtFundedYN" value="Yes"  onclick="CheckOther()" />
      <label for="GovtFundedYN">Government</label>
      <input name="CorpFundedYN" type="checkbox" id="CorpFundedYN"  value="Yes"  onclick="CheckOther()" />
      <label for="CorpFundedYN">Corporate</label>
      <input name="OtherFundedYN" type="checkbox" id="OtherFundedYN"  value="Yes" onclick="CheckOther()" />
      <label for="OtherFundedYN">Other</label>
    </div>
    <br />
    <div id="other">
      <label for="OtherFundingSource" class="left"> &nbsp;&nbsp;Other Funding Source <em><img src="images/required_star.gif"        
alt="required" /></em> </label>
      <input name="OtherFundingSource" type="text"  id="OtherFundingSource" maxlength="128" value="" />
    </div>
    <div class="left">Project dates (This can be something like <i>Summer 2001</i> <br />
      or <i>12/01/1988</i> -- use <i>UNK</i> for unknown)<em><img src="images/required_star.gif"        
alt="required" /></em></div>
    <br />
    <label for="StartDate"> &nbsp;&nbsp;Start date </label>
    <input name="StartDate" type="text" class="dateright" id="StartDate" maxlength="128" value="" />
    <br />
    <br />
    <label for="EndDate"> &nbsp;&nbsp;End Date</label>
    <input name="EndDate" type="text" class="dateright" id="EndDate" maxlength="128" value="" />
    <br />
    <label class="left" for="Website">Project web site (if one exists)</label>
    <input name="Website" type="text" id="Website"  size="60" maxlength="128" value="http://" />
    <br />
    <label for="Description" class="left">Project Description <em><img src="images/required_star.gif"        
alt="required" /></em></label>
    <textarea name="Description" id="Description" cols="60" rows="5"></textarea>
    <br />
    <label for="Role" class="left">Your role(s) in this project <em><img src="images/required_star.gif"        
alt="required" /></em> </label>
    <textarea name="Role" cols="35" rows="3" id="Role"></textarea>
    <br />
    <label for="Participants" class="left">Participating Institutions <em><img src="images/required_star.gif"        
alt="required" /></em></label>
    <textarea name="Participants" id="Participants" cols="60" rows="5"></textarea>
    <br />
    <label for="NbrParticipants" class="left">Number of Individual Participants<br />
      (OK to be approximate)<em><img src="images/required_star.gif"        
alt="required" /></em> </label>
    <input name="NbrParticipants" type="text" id="NbrParticipants" size="4" maxlength="4" value="" />
    <br />
    <div class="left">The participants' primary work locations are all <em><img src="images/required_star.gif"        
alt="required" /></em></div>
    <br />
    <input class="right" type="radio" name="WorkLocation" id="SameBuilding" value="SameBuilding" />
    <label for="SameBuilding"> in the same building</label>
    <br />
    <input name="WorkLocation" type="radio" class="right" id="SameCity" value="SameCity" />
    <label for="SameCity">in different sites in the same city</label>
    <br />
    <input name="WorkLocation" type="radio" class="right" id="SameCountry" value="SameCountry" />
    <label for="SameCountry">in different cities in the same country</label>
    <br />
    <input name="WorkLocation" type="radio" class="right" id="MultipleCountries" value="MultipleCountries" />
    <label for="MultipleCountries">in multiple countries</label>
    <br />
    <label for="AuthorityName" class="left">What person or group in the project has the authority to allow us to survey the  project's membership? <em><img src="images/required_star.gif"        
alt="required" /></em> </label>
    <input name="AuthorityName" type="text" id="AuthorityName" maxlength="32" value="" />
    <br />
    <label for="AuthorityContact" class="left">Please include contact information for this authority (email or phone) <em><img src="images/required_star.gif"        
alt="required" /></em> </label>
    <input name="AuthorityContact" type="text" id="AuthorityContact" maxlength="32" value="" />
    <br />
    <div class="left">Do you think the participants will be willing to take a <br />
      20-30 minute on-line survey?<em><img src="images/required_star.gif"        
alt="required" /></em></div>
    <input type="radio" name="SurveyWilling" id="Yes" value="Yes" />
    <label for="Yes">Yes</label>
    <input type="radio" name="SurveyWilling" id="No" value="No" />
    <label for="No">No</label>
    <br />
    <label for="ContactDetails" class="left">Will you be our primary point of contact for the project? <br />
      If not, who will be? (provide contact details) <em><img src="images/required_star.gif"        
alt="required" /></em></label>
    <textarea name="ContactDetails" cols="60" rows="5" id="ContactDetails"></textarea>
    <br />
    <label for="Comments" class="left">Comments</label>
    <textarea name="Comments" id="Comments" cols="60" rows="5"></textarea>
    <br />
    <label for="Questions" class="left">Questions for Us</label>
    <textarea name="Questions" id="Questions" cols="60" rows="5"></textarea>
    </p>
    <textarea id="SChk" name="SChk" cols="60" rows="3"></textarea>
    <p align="center">
      <input type="submit" name="Submit" id="Submit" value="Submit" />
    </p>
    <input type="hidden" name="MM_insert" value="form1" />
  </form>
  <div id="footer">Copyright &copy; 2011; The Collaboration Success Wizard team.  All rights reserved.</div>
</div>
<script type="text/javascript">
function CheckOther() {
	var otherval = document.form1.OtherFundedYN.checked; 
	if(otherval == true) {
			document.getElementById('other').style.display = "block";
	} else {
			document.getElementById('other').style.display = "none";
	}
}
function ShowFS () {
	document.getElementById('fundingsource').style.display = "block";
}
function HideFS() {
	document.getElementById('fundingsource').style.display = "none";
	document.getElementById('other').style.display = "none";
}


	
</script>
</body>
</html>
