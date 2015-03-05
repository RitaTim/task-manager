$(document).ready(function(){ 	
	
	$('#table_articles').dataTable({
		"paging"   : false,
		"searching": false,
		"bInfo"	   : false,
	})

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

	var show_task = function(id_task, title_task){
		$.ajax({
            url : "/task/show_task", 
            type : "GET",
            data : { 'id_task' : id_task, 'contents' : 'describe'},
            success : function(data) { 
            	$('.modal-body').html(data);
                $('.btn-modal').html('<a><button id="describe_task" class="btn btn-default" title="' + id_task + '">Описание</button></a> <a><button id="edit_task" class="btn btn-default" title="' + id_task + '">Редактирование</button></a>');
                load_contents(id_task, 'describe');
            	load_comments(id_task);               
                $('.modal-title').html(title_task);
            	$('#myModal').modal('show');
            },
            error : function(err) {
                alert("Fail GET /task/show_task");
            }
        })
	};

	$(document).on('click','.task_title', function(){
		show_task( $(this).attr('id'), $(this)[0].textContent );
	});

    $(document).on('click','#edit_task', function(){
        load_contents( $(this)[0].title, 'edit' );
    });

    $(document).on('click','#describe_task', function(){
        load_contents( $(this)[0].title, 'describe' );
    });

	$('.add-task').on('click', function(){
		show_task( 0 );
	});

	$('#myModal').modal('hide');

})