function init() {
	$('#searchButton').click(function(i,obj){
		sendSearchRequest();
	});
	$(document).keypress(function(e) {
		if($('#searchText').is(':focus'))
		{
	    	if(e.which == 13) {
	        	sendSearchRequest();
	    	}
	    }
	});
}


function inputValidation() {

}

function autoSuggest() {

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