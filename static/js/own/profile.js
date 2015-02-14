$(document).ready(function(){ 	

	$('.dropdown-menu > li').on('click', function(){
		var id_task = $(this).prop("id");

		$.ajax({
            url : "/profile/"+id_task, 
            type : "GET",
            success : function(data) {
            	$('#describe_task').prop("hidden", false);
            	$('#title_task').text(data.title);
            	$('#text_task').text(data.text);
            },
            error : function(err) {
                alert("Fail GET /task/get_task");
            }
        })
	})

})