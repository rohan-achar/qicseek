<html xmlns="http://www.w3.org/1999/xhtml">
<head>
                <title>useful linux security tools @ the bren school of information and computer sciences</title>
                
                
                <meta content="Tue, 05 Nov 2013 16:35:45 -0320" name="date"/>
                
<link href="../bin/styles/stylesheet_nosidebar.css" rel="stylesheet" type="text/css"/>
<script language="JavaScript">
<!-- 
function clear_textbox()
{
if (document.searchform.q.value == "Search ICS")
document.searchform.q.value = "";
} 
-->
</script>
</head>
<body>

<div id="wrapper">
<script type="text/javascript">

sfHover = function() {
    var sfEls = document.getElementById("navcontainer").getElementsByTagName("LI");
    for (var i=0; i<sfEls.length; i++) 
    {
        sfEls[i].onmouseover=function()
        {
            this.className+=" sfhover";
        }
        
        sfEls[i].onmouseout=function() 
        {
            this.className=this.className.replace(new RegExp(" sfhover\\b"), "");
        }
    }
}

if (window.attachEvent) window.attachEvent("onload", sfHover);

</script>


<div id="header" title="Welcome to the Donald Bren School of Information and Computer Sciences @ UC Irvine">

    <a id="bren_link" href="/"></a>

        <a id="uci_link" href="http://www.uci.edu/"></a>

</div>


    <div CLASS="newbar"><p style="line-height: 0px; display: none; "></p></div>

    
<div id="navcontainer">


<ul>

<li>

    <a href='/computing/account/' title='account'>&raquo; Account</a>

    <ul>
    <li><a href="/computing/account/new.php">&raquo; New User Guide</a></li>
    <li><a href="/computing/account/activate.php">&raquo; Activation</a></li>
    <li><a href="/computing/account/password.php">&raquo; Password Change/Reset</a></li>
    <li><a href="/computing/account/quota.php">&raquo; Quota</a></li>
    <li><a href="/computing/account/renewal.php">&raquo; Renewal</a></li>
    <li><a href='#'>&raquo; Mapping Network Drive</a>
      <ul>
      <li><a href="/computing/account/mapdrive_win.php">&raquo; Windows</a></li>
      <li><a href="/computing/account/mapdrive_mac.php">&raquo; Mac</a></li>
      </ul></li>
    <li><a href="/computing/account/faqs.php">&raquo; FAQs</a></li>     
    </ul>
</li>

<li>

    <a href='/computing/email/' title='e-mail'>&raquo; E-mail</a>

    <ul>
    <li><a href="/computing/email/google_apps.php">&raquo; ICS Google Mail</a></li>
    <li><a href="http://webmail.ics.uci.edu">&raquo; Webmail</a></li>
    <li><a href="/computing/email/thunderbird_setup.php">&raquo; Thunderbird</a></li>
    <li><a href="/computing/email/">&raquo; Mailing Lists</a></li>
    <li><a href="/computing/email/mailboss.php">&raquo; Forwarding/Vacation/Spam Settings</a></li>
    <li><a href="/computing/email/">&raquo; Email Servers Information</a></li>
    <li><a href="/computing/email/group_email.php">&raquo; Checking Group Account Email</a></li>
    </ul>
</li>

<li>

    <a href='/computing/network/' title='network'>&raquo; Network</a>

    <ul>
    <li><a href="http://www.oit.uci.edu/mobile/">&raquo; UCInet Mobile</a></li>
    <li><a href="http://www.oit.uci.edu/security/vpn/">&raquo; VPN</a></li>
    <li><a href="https://netreg.ics.uci.edu/">&raquo; ICS Netreg</a></li>
    <li><a href="http://weather.uci.edu/">&raquo; UCI Weather Report</a></li>
    <li><a href="/computing/network/">&raquo; Open Port Request</a></li>
    </ul>
</li>

<li>

    <a href='#' title='linux'>&raquo; Linux</a>
    
    <ul>
    <li><a href="/computing/linux/hosts.php">&raquo; ICS hosts</a></li>
    <li><a href="/computing/linux/shell.php">&raquo; Changing shell</a></li>
    <li><a href="/computing/linux/modules.php">&raquo; Using modules</a></li>
    <li><a href="/computing/linux/security.php">&raquo; Security</a></li>
    <li><a href="/computing/linux/gsu.php">&raquo; Group account access (gsu)</a></li>
    <li><a href="/computing/linux/sge.php">&raquo; Sun Grid Engine</a></li>
        </ul>
</li>

<li>

    <a href='#' title='services'>&raquo; Other Services</a>

    <ul>
    <li><a href="http://www.ics.uci.edu/~lab">&raquo; Labs</a></li>
    <li><a href="/computing/services/printing.php">&raquo; Printing</a></li>
    <li><a href='#'>&raquo; Sophos</a>
      <ul>
      <li><a href="/computing/services/sophos_win.php">&raquo; Windows</a></li>
      <li><a href="/computing/services/sophos_mac.php">&raquo; Mac</a></li>
      </ul></li>    
    <li><a href="/computing/services/msdnaa_faq.php">&raquo; MSDNAA</a></li>
    <li><a href='#'>&raquo; File Restore</a>
      <ul>
      <li><a href="/computing/services/snapshot.php">&raquo; Self-restore snapshot</a></li>
      <li><a href="/computing/services/restore.php">&raquo; Restore request</a></li>
      </ul></li>
      <li><a href="/computing/quarterlyAnnouncement/index.php">&raquo; Quarterly announcements</a></li>
    </ul>   
</li>

<li> 

    <a href='#' title='web'>&raquo; Web</a>
    
    <ul>
    <li><a href="/computing/web/personalpage.php">&raquo; Personal Webpage</a></li>
    <li><a href="/computing/web/faqs.php">&raquo; General Information</a></li>
    </ul>   
</li>

<li>

    <a href='/computing/policy/' title='contact'>&raquo; Policies</a>
    
    <ul>
    <li><a href="/computing/policy/ethics.php">&raquo; Ethics</a></li>
    <li><a href="/computing/policy/ethics_summary.php">&raquo; Ethics Summary</a></li>
    </ul>
</li>

<li>

    <a href='/computing/contact/' title='contact'>&raquo; Contact</a>
    
    <ul>
    <li><a href="/computing/contact/helpdesk.php">&raquo; Helpdesk</a></li>
    <li><a href="/computing/contact/staff.php">&raquo; Support Staff</a></li>
    <li><a href="/computing/contact/who.php">&raquo; Who To Contact</a></li>
    </ul>
</li>

</ul>

<style type="text/css">@import url("/bin/icssearchstyle/css/icssearch.css");</style>
<script src="/bin/icssearchstyle/js/icssearch.js" type="text/javascript"></script>
<script src="/bin/icssearchstyle/js/icssearchform.js" type="text/javascript"></script>

</div><div id="content"><a id="startcontent" name="startcontent"></a>  
<div id="content_title">Useful Linux Security Tools</div>

<blockquote>
<div id="content_text">

<p>Many programs are available which can help prevent break-ins and minimize the
damage caused.&#160; Since these programs are used to protect the security of your
system, make sure you get any such tools from trusted websites.&#160; Be careful with pre-compiled binaries, especially if you run these 
programs as
root. 
          </p>
<p>&#160;</p>
<ul>
<li> Install <a href="http://www.oit.uci.edu/support/dcs/ssh_info.html"> ssh</a> and <a href="http://www.sslftp.com/"> SSL FTP</a>&#160;and use them instead of <code>telnet</code>,
 <code>rlogin</code>, <code>rsh</code>,
                and <code>ftp</code>&#160;to prevent unencrypted passwords from 
being
                sniffed from off the network. </li>
<p>&#160;</p>
<li> Install <a href="http://www.freebsd.org/doc/en/books/handbook/tcpwrappers.html">
 TCP
                Wrappers</a> to prevent access from untrusted sites or 
to limit
                access only to specific sites. </li>
<p>&#160;</p>
<li> Use <a href="http://metalab.unc.edu/linux/HOWTO/Shadow-Password-HOWTO.html"> 
shadow
                passwords</a> so that the system file containing the 
actual encrypted
                passwords is not accessible to others.&#160; Redhat's default
                configuration does not use shadow passwords, but this 
can be
                easily changed by using the <code>pwconv</code> tool. </li>
<p>&#160;</p>
<li> Use <a href="http://www.tripwire.org/downloads/index.php">Tripwire</a>&#160;to be notified when system files have 
been modified
                or when possible trojan horses have been inserted into 
your system. </li>
</ul>


</div>
</blockquote>
</div>
<div id="sidebar"></div>
<div id="footer"><a href="http://www.uci.edu/copyright.php">Copyright Inquiries</a> |
   <a href="http://www.uci.edu/cgi-bin/phonebook">UCI Directory</a> |
   <a href="http://intranet.ics.uci.edu/">Intranet</a> |
   
   <!-- <a href="http://www.ics.uci.edu/sitemap.php">Site Map</a> | -->
 
  <a href="mailto: i%63%73%77%65%62m%61s%74%65r@%69c%73%2e%75c%69%2eedu">icswebmaster</a> |
Updated: 
November 05 2013</div>
</div>
<script type="text/javascript">
var gaJsHost = (("https:" == document.location.protocol) ? "https://ssl." : "http://www.");
document.write(unescape("%3Cscript src='" + gaJsHost + "google-analytics.com/ga.js' type='text/javascript'%3E%3C/script%3E"));
</script>
<script type="text/javascript">
var pageTracker = _gat._getTracker("UA-605898-1");
pageTracker._trackPageview();
</script>
</body>
</html>
