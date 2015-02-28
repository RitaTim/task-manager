$(document).ready(function() {
    $(function() {

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
            $.each( tasks, function( index, value ){
                        lst_res += "<li class = 'board_item board_item_color' id=" + value.id + "><p> <b>" + value.title + "</b> </p><p>" + value.text + "</p></li>";
            })
            return lst_res;
        };

        var change_dashboard = function(){
            $('#to_do, #in_progress, #test, #done').empty();
            $.ajax({
                url : "/task/get_tasks", 
                type : "GET",
                dataType: "json",
                data : get_data_filter(),
                success : function(data) {                    
                    $('#to_do')      .append( lst_tasks_dom(data.tasks_to_do)       ); 
                    $('#in_progress').append( lst_tasks_dom(data.tasks_in_progress) );
                    $('#test')       .append( lst_tasks_dom(data.tasks_test)        );
                    $('#done')       .append( lst_tasks_dom(data.tasks_done)        );           
                },
                error : function(err) {
                    alert("fail");
                }
            })
        }

        change_dashboard();
        $('#which_iteration' ).on('change', function(){ change_dashboard() });
        $('#which_tasks').on('change', function(){ change_dashboard() });
    })
})