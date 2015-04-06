$(document).ready(function(){ 	

	var show_form_project = function(project_id){
		$.ajax({
            url : "/projects/edit_project", 
            type : "GET",
            data : { 'project_id' : project_id},
            success : function(data) { 
            	$('.modal-body').html(data);
            	$('#myModal').modal('show');
            },
            error : function(err) {
                alert("Fail GET /projects/edit_project/" + id_project);
            }
        })
        $('.modal-title').text("Проект");
	};

	$(document).on('click','.edit-project', function(){
		show_form_project( $(this).attr('id') );
	});

	$(document).on('click', '.add-project', function(){
		show_form_project(0);
	});

	$('#myModal').modal('hide');
})