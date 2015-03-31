$(document).ready(function(){ 
    var lst_assigning_tasks = function(){
        return $('#lst_not_dev_tasks input:checked').map(function(){
            return parseInt($(this).attr("id"));
        }).get();
    };

	var load_comments = function(id_task){
		$.ajax({
            url : "/comment/get_comments", 
            type : "GET",
            data : { 'id_task' : id_task },
            dataType: "html",
            success : function(data) {
            	$('#box-comments').append(data);
            },
            error : function(err) {
            	console.log(err);
            }
        })
	};

    var load_contents = function(id_task, contents){
        $.ajax({
            url : "/task/task", 
            type : "GET",
            data : { 'id_task' : id_task, 'contents' : contents },
            dataType: "html",
            success : function(data) {
                $('.contents').html(data);
                if (contents != 'describe') {
                    $('#edit_task').addClass('active');
                    $('#describe_task').removeClass('active');
                }
                else {
                    $('#describe_task').addClass('active'); 
                    $('#edit_task').removeClass('active');   
                }
            },
            error : function(err) {
                console.log(err);
            }
        })
    };

	var show_task = function(contents, id_task){
        var id_task = id_task ? id_task : '';
		$.ajax({
            url : "/task/task/" + id_task, 
            type : "GET",
            data : { 'contents' : contents },
            success : function(data) {
                $('#task-modal').html(data);
                if ( contents === "all_form" ) {
                    $('.btn-modal').html('<a><button class="btn btn-default toggle_form_task" title="' + id_task + '">Описание</button></a> <a><button class="btn btn-default toggle_form_task" title="' + id_task + '">Редактирование</button></a>');
                }
                if ( contents === "edit" ){
                    $('#describe').hide();
                }
                else {
                    $('#edit').hide();
                }
            	if (id_task) { 
                    load_comments(id_task);
                };               
            	$('#task-modal').modal('show');
            },
            error : function(err) {
                alert("Fail GET /task/task");
            }
        })
	};

    var show_lst_not_dev = function(id_project){
        $.ajax({
            url : "/task/show_lst_not_dev", 
            type : "GET",
            data : { 'id_project' : id_project},
            success : function(data) {
                $('.modal-body').html(data);
                $('.modal-title').html("Склад задач");
                $('#myModal').modal('show');
            },
            error : function(err) {
                alert("Fail GET /task/show_lst_not_dev");
            }
        })
    };

    var assign_for_user = function(id_user){
        tasks_id = 'tasks_id='+JSON.stringify(lst_assigning_tasks());
        $.ajax({
            url : "/task/assign_for_user", 
            data: tasks_id,
            type : "GET",
            success : function(data) {                
                $('#myModal2').modal('hide');
                location.reload();
            },
            error : function(err) {
                alert("Fail GET /task/assign_for_user");
            }
        })  
    };

    $(document).on('click','#assign_for_user', function(){
        assign_for_user( 'none' ); // !!! 
    });

    $(document).on('click','.assign_for_user', function(){
        show_lst_not_dev( 1 ); // !!current project
    });

	$(document).on('click','.task_title', function(){
		show_task( 'all_form', $(this).attr('id') );
	});

    $('.add-task').on('click', function(){
        show_task( 'edit' );
    });

    $(document).on('click','.not_dev_task_title', function(){
        show_task( 'describe', $(this).prev('input')[0].id );
    });

    $(document).on('click','.toggle_form_task', function(){
        $('#edit').toggle( 'display' );
        $('#describe').toggle( 'display' );
    });

	$('#myModal').modal('hide');

})