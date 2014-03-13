var gVar;

function init() {

	var searchBox = document.getElementById('searchText'),
		$sBoxObj = $(searchBox),
		$asObj = $('#autoSuggestDiv');

	searchBox.addEventListener('input',function(e){
		
		var searchQuery = e.target.value,
			asQueryObj = getWordAtPosition(searchQuery,e.target.selectionStart);

		$asObj.hide();
		resetResults('Press Enter or click Search to find pages from within ICS!');

		if (e.target.value.slice(-1) != ' ' && $.trim(e.target.value) != '' && $.trim($asObj.text()) != asQueryObj.word)
		{	
			if(asQueryObj.partial_word.length >= 3) 
			{
				autoSuggest(e.target,asQueryObj);
			}
		}
	});

	$asObj.css('top',($sBoxObj.offset().top + $sBoxObj.outerHeight()).toString()+'px');

	function acceptAutoSuggest() {
		var currentQuery = $sBoxObj.val(),
			cursorPos = searchBox.selectionStart,
			curwordObj = getWordAtPosition(currentQuery,cursorPos),
			asText = $.trim($asObj.text());

		$sBoxObj.val(currentQuery.replace(curwordObj.word,asText));

		searchBox.selectionStart = curwordObj.end + asText.length - curwordObj.word.length;
		searchBox.selectionEnd = curwordObj.end + asText.length - curwordObj.word.length;	

		setTimeout(function(){
	        $sBoxObj.focus();
	    }, 1);

		$asObj.hide();
	}

	$(document).keydown(function(e) {

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
	    	else if(keynum == 9 || keynum == 39)
	    	{
	    		if($asObj.css('display') != 'none')
				{
	    			acceptAutoSuggest();
	    			if(keynum == 9)
	    				e.preventDefault();
	    		}
	    	}    
        }
	    
	});

	$('#searchButton').click(function(i,obj){
		sendSearchRequest();
	});

	setTimeout(function(){
        $sBoxObj.focus();
    }, 1);

    $asObj.click(function(){
		acceptAutoSuggest();
	});

	function setSelectStyleOpen($selectObj) {
		
		$selectObj.css('border-bottom-left-radius', '0px');
		$selectObj.css('border-bottom-right-radius', '0px');
	}

	function setSelectStyleClosed($selectObj) {
		$selectObj.css('border-bottom-left-radius', $selectObj.css('border-radius'));
		$selectObj.css('border-bottom-right-radius', $selectObj.css('border-radius'));
	}

	var rankTypeSelect = $('#rankTypeSelect'),
		sOpenFlag = false;

	rankTypeSelect.mousedown(function() {
		setSelectStyleOpen($(this));
	});

	rankTypeSelect.blur(function() {
		setSelectStyleClosed($(this));
	});

	$('body').mouseup(function() {
		if(sOpenFlag)
			setSelectStyleClosed(rankTypeSelect);
		sOpenFlag = true;
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
	wordObj['partial_word'] = inputString.slice(i,cPosition);

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

		$asObj.css('left',(asFixedLeft+asOffset+1).toString()+'px');
	$.ajax({
		type: "GET",
		url: URL,
		data: {'q': asWordObj.word, 'as': 'true'},
		success: function(data) {
			
			searchResults = data;
			
			//console.log(data);
			if(data[0] != asWordObj.word)
			{
				cleanPartialWord = asWordObj.partial_word.replace(/\W+/g,'');
				if(data[0].indexOf(cleanPartialWord) != -1)
				{
					$asObj.html('&nbsp;'+cleanPartialWord+'<b>'+data[0].replace(cleanPartialWord,'')+'</b>'+'&nbsp;')
				}
				else
				{
					$asObj.html('&nbsp;'+data[0]+'&nbsp;')
				}
				$asObj.show();
			}
			
		}
	})
}

function resetResults(msg) {
	var resultsContainer = $('.container .row');
	resultsContainer.empty();
	resultsContainer.append($('<h2/>').html(msg));
}

function sendSearchRequest() {
	var queryText = $("#searchText").val(),
		searchResults = [];

	$('#autoSuggestDiv').hide();
	
	if($.trim(queryText) == '')
		return;

	$.ajax({
		type: "GET",
		url: URL,
		data: {'q': queryText, 'rt': $('#rankTypeSelect').val()},
		success: function(data) {
			console.log(data);
			//searchResults = data;
			if (data){
			    try{
			        searchResults=data;	        
			    }
			    catch(e){
			        alert(e); 
			    }
			}
			else
			{
				resetResults('No results found for '+queryText+'.');
				return;
			}

			resultsContainer = $('.container .row');
			resultsContainer.empty();
			var resultRow,
				urlTitle = '',
				url = '',
				resultsHeader = $('<div/>').append(
									$('<h3/>')
										.html("Results for "+queryText+": ")
										.addClass('results-header')
								);
			resultsContainer.append(resultsHeader);

			for(var i = 0; i < searchResults.length; i++) {
				
				url = searchResults[i]['url'];
				urlTitle =  searchResults[i]['title'].length == 0 ? url : searchResults[i]['title'];
				
				var resultRow = $('<div/>').append(
											$('<h5/>').append(
												$('<a/>').html(urlTitle).attr('href',url).addClass('')
											)
								);
				resultsContainer.append(resultRow);
			}
			$('#searchText').blur();
		}
	})
}