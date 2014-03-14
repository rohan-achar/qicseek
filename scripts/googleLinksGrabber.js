var jq = document.createElement('script');
jq.src = "https://code.jquery.com/jquery-1.11.0.min.js";
document.getElementsByTagName('head')[0].appendChild(jq);


// ... give time for script to load, then type.
jQuery.noConflict();


linksList = []
$('.srg li h3.r a').each(function(i,obj) {
	var hrefLink = '';
	if(typeof $(obj).data('href') != "undefined")
	{ 
		hrefLink = $(obj).data('href');
	} 
	else
	{
		hrefLink = $(obj).attr('href');	
	}
	if(hrefLink.substr(0,5) == "https")
	{
		linksList.push(hrefLink.replace('https://','http://'));
	}
	else
	{
		linksList.push(hrefLink);
	}

}) 