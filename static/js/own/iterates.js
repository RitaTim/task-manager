$(document).ready(function(){ 	
	
	$('#table_iterates').dataTable({
		"paging"   : false,
		"searching": false,
		"bInfo"	   : false,
	})

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

	var show_iterate = function(iterate_id){
        var iterate_id = iterate_id ? iterate_id : '';
		$.ajax({
            url : "/iterates/iterate/" + iterate_id, 
            type : "GET",
            success : function(data) {
                $('#myModal').html(data);           
            	$('#myModal').modal('show');
            },
            error : function(err) {
                alert("Fail GET /iterates/iterate/" + iterate_id);
            }
        })
	};

    // $(document).on('click','#assign_for_user', function(){
    //     assign_for_user( 'none' ); // !!! 
    // });

    // $(document).on('click','.assign_for_user', function(){
    //     show_lst_not_dev( 1 ); // !!current project
    // });

    var target_iterate_days = function(){
        $('#input_iterate_days').toggle();
        $('#value_iterate_days').toggle();
    };

	$(document).on('click','.iterate_title', function(){
		show_iterate( $(this).attr('id') );
	});

    $('#myModal').modal('hide');
    $('.add-iterate').on('click', function(){
        show_iterate();
    });


    $(document).on('click','#value_iterate_days', function(){
        target_iterate_days();
    });

    $(document).on('click','#save_iterate_days', function(){
        new_count_days = $('#iterate_days')[0].value;
        if (new_count_days) {
            $.ajax({
                url : "/iterates/set_iterate_days", 
                type : "GET",
                data: { 'new_count_days' : new_count_days },
                error : function(err) {
                    alert("Fail GET /iterates/iterate/" + iterate_id);
                }
            });
            $('#value_iterate_days').text(new_count_days);
            target_iterate_days();
        };
    });
})