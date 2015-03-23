$(document).ready(function(){ 	

    var show_task = function(id_task) {
        $.ajax({
            url : "/profile/"+id_task, 
            type : "GET",
            success : function(data) {
                $('#describe_task').prop("hidden", false);
                $('#title_task').text(data.title);
                $('#text_task').text(data.text);
                load_comments(id_task);
            },
            error : function(err) {
                alert("Fail GET /task/get_task");
            }
        })
    }

    var load_comments = function(id_task){
        $.ajax({
          url : "/comment/get_comments", 
          type : "GET",
          data : { 'id_task' : id_task },
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

    var lst_item_dom = function(items){
        lst_res = '';
        $.each( items, function( index, value ){
            lst_res += "<li id=" + value.id + ">" + value.title + "</li>";
        });
        return lst_res;
    };

    var fill_in_table = function(id_iterate){
        $.ajax({
            url : "/profile/get_tasks/" + id_iterate, 
            type : "GET",
            DataType: "json",
            success : function(data) {
                jQuery.each(data.tasks, function(index, item) {
                    $('#' + index)[0].children[0].text = item.length;
                    $('#' + index + ' ul').html(lst_item_dom(item));
                });
            },
            error : function(err) {
                alert("Fail GET /profile/get_task");
            }
        })
    };

    var fill_progress_bar = function(iterate_id){
        $.ajax({
            url : "/task/get_progress_bar_user", 
            type : "GET",
            DataType: "json",
            data : { 'iterate_id' : iterate_id },
            success : function(data) {
                var lst_progress = "";
                $.each( data.progress_bar, function( index, value ){
                    lst_progress += "<div id='" + value.id + "' class='progress-bar " + value.css_class + "' role='progressbar' style='width:" + value.width + "%'><a href='#' data-toggle='tooltip' title='Выполнение: " + value.perform_time+ "'>" + value.title + "</a></div>";
                });
                $('#progress-bar').html(lst_progress);
                $('#time-iterate').html('<label>' + data.iterate_time.start_line + ' - ' + data.iterate_time.dead_line + '</label>');
                $('#spend-time').html(data.all_time);
            },
            error : function(err) {
                alert("Fail GET /task/get_progress_bar_user");
            }
        })
    };


    var fill_fields = function(){
        var choice_iter = $('#iterates-menu option:selected')[0].id;
        fill_in_table( choice_iter );
        fill_progress_bar( choice_iter );
    }

    $('#iterates-menu').on('change', function(){
        fill_fields();

    });

	$(document).on('click', '.tasks-menu > li', function(){
		show_task($(this).prop("id"));
	});

    $(document).on('click', '#progress-bar > div', function(){
        show_task($(this).prop("id"));
    });

    fill_fields();
    $("[data-toggle='tooltip']").tooltip(); 

})