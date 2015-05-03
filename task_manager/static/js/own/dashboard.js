$(document).ready(function() {
    //menu side
    var show_object = function(object){
        object.removeClass('hidden');
    };

    var hide_object = function(object){
        object.addClass('hidden');
    };

    $('#body-content').removeClass('body-content');
    $('#box-menu').prop('class', 'navbar navbar-fixed-top col-sm-offset-10 dashboard-menu');
    
    hide_object($('#box-menu'));

    $('#active_menu').on('click', function(){
        if ( $('#box-menu').hasClass('hidden') ) {
            show_object($('#box-menu'))
        }
        else {
            hide_object($('#box-menu'))
        }
    });

    //change status task
    $( "#test, #done, #in_progress, #to_do" )
        .sortable({
            connectWith: "ul",
            opacity:0.5,
            dropOnEmpty:true,
            receive: function( event, ui ) {
                var id_task = ui.item.context.id;
                var new_status = ui.item.parent().attr('id'); 
                $.ajax({
                        data: { 'id_task' : id_task, 'new_status' : new_status, 'timestamp' : $.now() },
                        type: 'GET',
                        url: '/task/change_status'
                })
            }
        })
        .disableSelection(); 

    var get_data_filter = function(){
        var id_project    = $("#project").attr('id_project');
        var id_iteration  = $("#which_iteration option:selected").attr('id');
        var which_tasks   = $("#which_tasks option:selected").attr('id') || 0;
        return {id_project: id_project, id_iteration: id_iteration, which_tasks : which_tasks};
    }    

    var lst_tasks_dom = function(tasks){
        lst_res = '';
        $.each( tasks, function( index, task ){
            lst_res += "<li class = '" + task.style + (task.main_task ? " subtask " : " ") + "board_item board_item_color' id=" + task.id + "><a><b><p class='task_title' id='" + task.id + "'>" + task.title + "</p></b></a><div class='board_item_text'><div class='col-sm-8'>" + task.text + "</div><div class='col-sm-2 assigned-ticket text-center'>" + task.assigned__username + "</div></div></li>";
        })
        return lst_res;
    };

    var change_dashboard = function(){
        $('#to_do, #in_progress, #test, #done').empty();
        id_project = $('#project')[0].title;
        $.ajax({
            url : "/task/get_tasks", 
            type : "GET",
            dataType: "json",
            data : get_data_filter(),
            success : function(data) {
                if (!data.empty) {                    
                    $('#to_do')      .append( lst_tasks_dom(data.tasks_to_do)       ); 
                    $('#in_progress').append( lst_tasks_dom(data.tasks_in_progress) );
                    $('#test')       .append( lst_tasks_dom(data.tasks_test)        );
                    $('#done')       .append( lst_tasks_dom(data.tasks_done)        );  
                }         
            },
            error : function(err) {
                alert("fail");
            }
        })
    }

    change_dashboard();
    $('.filter_select' ).on('change', function(){ change_dashboard() });
})