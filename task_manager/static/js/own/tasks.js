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
                $('#task-modal #id_text').redactor({
                    minHeight: 200,
                    buttons: [
                        'html', 'formatting', 'bold', 'italic', 'deleted','unorderedlist', 'orderedlist', 'outdent', 'indent',
'image', 'file', 'link', 'alignment', 'horizontalrule'],
                    imageUpload: "/file/photos/upload",
                    imageGetJson: "/file/photos/recent",
                    fileUpload: "/file/files/upload",
                    fileGetJson: "/file/files/recent"
                });
            	$('#text').redactor({
                        minHeight: 200,
                        toolbar: false
                });
                $('#task-modal').modal('show');
            },
            error : function(err) {
                alert("Fail GET /task/task");
            }
        })
	};

    var show_lst_not_dev = function(){
        $.ajax({
            url : "/task/show_lst_not_dev", 
            type : "GET",
            success : function(data) {
                $('.modal-body').html(data);
                $('.btn-modal').empty();
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
                location.reload();
            },
            error : function(err) {
                alert("Fail GET /task/assign_for_user");
            }
        })  
    };

    var load_tasks = function(){
        var iteration_id = $("#load_table_tasks option:selected").attr('id');
        if (iteration_id) {
            $.ajax({
                url : "/task/load_table_tasks", 
                data: {'iteration_id' : iteration_id},
                type : "GET",
                success : function(data) {            
                    $('#content_task_table').html(data);
                },
                error : function(err) {
                    alert("Fail GET /task/load_table_tasks");
                }  
            })  
        }
    };

    $(document).on('click','#assign_for_user', function(){
        assign_for_user('none');
    });

    $(document).on('click','.assign_for_user', function(){
        show_lst_not_dev();
    });

	$(document).on('click','.task_title', function(){
		show_task('all_form', $(this).attr('id'));
	});

    $('.add-task').on('click', function(){
        show_task('edit');
    });

    $(document).on('click','.not_dev_task_title', function(){
        show_task('describe', $(this).prev('input')[0].id);
    });

    $(document).on('click','.toggle_form_task', function(){
        $('#edit').toggle( 'display' );
        $('#describe').toggle( 'display' );
    });

    $(document).on('change','#load_table_tasks', function(){
        console.log('change');
        load_tasks();
    });

	$('#myModal').modal('hide');

    if ( $('#load_table_tasks') ) {
        load_tasks();
    };
})