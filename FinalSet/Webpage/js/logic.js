var gVar;

function init() {

	var searchBox = document.getElementById('searchText'),
		$sBoxObj = $(searchBox),
		$asObj = $('#autoSuggestDiv');

	searchBox.addEventListener('input',function(e){
		console.log(e);
		gVar = e;
		var searchQuery = e.target.value,
			asQueryObj = getWordAtPosition(searchQuery,e.target.selectionStart);

		if(e.target.value.slice(-1) == ' ' || e.target.value.replace(' ','') == '' || $asObj.text().slice(1,-1) == asQueryObj.word)
		{	
			$asObj.hide();
		}
		else
		{
			if(asQueryObj.word.length >= 3) {
				autoSuggest(e.target,asQueryObj);
			}
		}
	});

	$asObj.css('top',($sBoxObj.offset().top + $sBoxObj.outerHeight()).toString()+'px');

	$(document).keypress(function(e) {
		if($('#searchText').is(':focus'))
		{
			var keynum;

			if(window.event) 
			{ // IE					
            	keynum = e.keyCode;
            }
            else if(e.which)
            { // Netscape/Firefox/Opera					
            	keynum = e.which;
            }
            
	    	if(keynum == 13) 
	    	{ // Enter key is pressed
	        	sendSearchRequest();
	        	return;
	    	}    
        }
	    
	});

	$('#searchButton').click(function(i,obj){
		sendSearchRequest();
	});
}

function getWordAtPosition(inputString, cPosition) {
	var i = cPosition,
		j = cPosition,
		wordObj = {};

	while(i > 0 && inputString[i-1] != ' ') {
		i--;
	}

	while(j < inputString.length && inputString[j] != ' ') {
		j++;
	}

	wordObj['word'] = inputString.slice(i,j);
	wordObj['start'] = i;
	wordObj['end'] = j;

	return wordObj;
}

function autoSuggest(inputObj,asWordObj) {
	var $sBoxObj = $(inputObj),
		$asObj = $('#autoSuggestDiv'),
		asFixedLeft = $sBoxObj.offset().left + parseInt($sBoxObj.css('padding-left').replace('px','')),
		asFixedOffset = parseInt($sBoxObj.css('padding-left').replace('px','')),
		asOffset = $('#asSizeCheck')
						.css('display','none')
						.css('color','#fff')
						.css('position','absolute')
						.css('font-size',$sBoxObj.css('font-size'))
						.css('width','auto')
						.html($sBoxObj.val().slice(0,asWordObj.start))
						.width();

		asOffset = asWordObj.start > 0 ? asOffset : asOffset - 2; 
		console.log(asOffset);

		//$asObj.css('left',(asFixedLeft).toString()+'px');

		$asObj.css('left',(asFixedLeft+asOffset+1).toString()+'px');

	$.ajax({
		type: "GET",
		url: URL,
		data: {'q': asWordObj.word, 'as': 'true'},
		success: function(data) {
			
			searchResults = data;
			
			console.log(data);
			if(data[0] != asWordObj.word)
			{
				$asObj.html('&nbsp;'+asWordObj.word+'<b>'+data[0].replace(asWordObj.word,'')+'</b>'+'&nbsp;')
				$asObj.show();
			}
			
		}
	})
}



function sendSearchRequest() {
	var queryText = $("#searchText").val();
	var searchResults = {};
	
	$.ajax({
		type: "GET",
		url: URL,
		data: {'q': queryText},
		success: function(data) {
			//console.log(data);
			searchResults = data;
			// if (data){
			//     try{
			//         searchResults=JSON.parse(data);	        
			//     }
			//     catch(e){
			//         alert(e); 
			//     }
			// }
			resultsContainer = $('.container .row');
			resultsContainer.empty();
			var resultRow,
				urlTitle = '',
				url = '';
			for(var docId in searchResults) {
				
				url = searchResults[docId]['url'];
				urlTitle =  searchResults[docId]['title'].length == 0 ? url : searchResults[docId]['title'];
				var resultRow = $('<div/>').append(
											$('<h4/>').append(
												$('<a/>').html(urlTitle).attr('href',url).addClass('')
											)
								);
				resultsContainer.append(resultRow);
			}
			$('#searchText').blur();
		}
	})
}