$(document).ready(function(){ 	
	
	var load_comments = function(id_forum){
		$.ajax({
                  url : "/forum/get_comments", 
                  type : "GET",
                  data : { 'id_forum' : id_forum },
                  dataType: "html",
                  success : function(data) { 
                  	$('#box_comments').html(data);
                  	return false;
                  },
                  error : function(err) {
                  	console.log(err);
                  }
            })
	}

	load_comments( $('.box-form a:first-child').find('label').prop('id') );

	$('.forum').on('click', function(){
		load_comments($(this).attr('id'));
            $('.active_forum').removeClass('active_forum');
            $(this).addClass('active_forum');
	});

})