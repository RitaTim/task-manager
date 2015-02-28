$(document).ready(function(){ 	
	
	$('#table_articles').dataTable({
		"paging"   : false,
		"searching": false,
		"bInfo"	   : false,
	})

	var show_form_task = function(id_task){
		$.ajax({
            url : "/task/edit_task", 
            type : "GET",
            data : { 'id_task' : id_task},
            success : function(data) { 
            	$('.modal-body').html(data);
            	$('#myModal').modal('show');
            },
            error : function(err) {
                alert("Fail GET /task/edit_task");
            }
        })
	};

	$(document).on('click','.task_title', function(){
		show_form_task( $(this).attr('id') );
	});

	$('.add-task').on('click', function(){
		show_form_task( 0 );
	});

	$('#myModal').modal('hide');
})