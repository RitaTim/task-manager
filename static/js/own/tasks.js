$(document).ready(function(){ 	
	
	$('#table_articles').dataTable({
		"paging"   : false,
		"searching": false,
		"bInfo"	   : false,
	})


	$('.task_title').click(function(){
		$.ajax({
            url : "/task/get_task", 
            type : "GET",
            data : { 'id_task' : $(this).attr('id'), 'id_project' : $("#project").attr('id_project')},
            success : function(data) { },
            error : function(err) {
                alert("Fail GET /task/get_task");
            }
        })
	})

})