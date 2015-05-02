$(document).ready(function(){ 	

	var show_form_project = function(project_id){
        var param = project_id ? "project_id=" + project_id : "";
		$.ajax({
            url : "/projects/edit_project?" + param, 
            type : "GET",
            success : function(data) { 
            	$('.modal-body').html(data);
                $('#myModal #id_text').redactor({
                    minHeight: 200,
                    buttons: [
                        'html', 'formatting', 'bold', 'italic', 'deleted','unorderedlist', 'orderedlist', 'outdent', 'indent',
'image', 'file', 'link', 'alignment', 'horizontalrule'],
                    imageUpload: "/file/photos/upload",
                    imageGetJson: "/file/photos/recent",
                    fileUpload: "/file/files/upload",
                    fileGetJson: "/file/files/recent"
                });
            	$('#myModal').modal('show');
            },
            error : function(err) {
                alert("Fail GET /projects/edit_project/" + id_project);
            }
        })
        $('.modal-title').text("Проект");
	};

	$(document).on('click','.edit-project', function(){
		show_form_project($(this).attr('id'));
	});

	$(document).on('click', '.add-project', function(){
		show_form_project();
	});

	$('#myModal').modal('hide');
    $('.text').redactor({
        minHeight: 200,
        toolbar: false
    });
})