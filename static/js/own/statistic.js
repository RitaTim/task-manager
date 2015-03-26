$(document).ready(function(){
	
    var load_statistic = function(iterate_id){
        lst_users_id =  $('.user_data').map(function(indx, element){return $(element).attr("title")}).get();
        $.ajax({
            url : "/statistic/get_progress_users", 
            type : "GET",
            data : 'iterate_id=' + iterate_id +'&lst_users_id=' + JSON.stringify(lst_users_id),
            dataType: "json",
            success : function(data) {
                $('.time-iterate').html('<label>' + data.iterate_time.start_line + ' - ' + data.iterate_time.dead_line + '</label>');       
                $.each( data.data_users, function( k, data_user ){
                    var lst_progress = "";
                    $.each( data_user.progress_bar, function( i, value ){
                        lst_progress += "<div id='" + value.id + "' class='progress-bar task_title " + value.css_class + "' role='progressbar' style='width:" + value.width + "%'><a href='#' data-toggle='tooltip' title='Выполнение: " + value.perform_time+ "'>" + value.title + "</a></div>";
                    });
                    $('.user_data[title=' + k + '] > .work_process > .progress').html(lst_progress);
                    $('.user_data[title=' + k + '] > .perform_time').html(data_user.all_time);
                });
            },
            error : function(err) {
                console.log(err);
            }
        })
    };

    var render_chart = function(data){
        var start_time  = data.iterate_time.start_line;
        var end_time    = data.iterate_time.dead_line;
        var count_tasks = data.count_tasks;
        
        data_points_ideal = [
            { x: new Date(start_time), y: count_tasks },
            { x: new Date(end_time),   y: 0 }
        ];

        var data_points_real = [];
        var data_tooltipe    = [];
        var num_task = count_tasks;
        $.each( data.data_tasks, function( i, task ){
            data_points_real.push(
                {x: new Date(task.x_coordinate), y: num_task}
            );
            data_tooltipe.push(
                task.title_task + " <strong>" + task.perform_time
            );
            num_task -= 1;
        });                

        var data_chart = {
            width: 1150,
            height: 450,
            title:{
                text: "График",
                fontColor: "green",
                fontSize: 20,
            },
            toolTip: {
                content: function(e){
                    var content;
                    content = data_tooltipe[ count_tasks - e.entries[0].dataPoint.y];
                    return content;
                }
            },
            axisX:{ 
                title: "Время итерации",
                titleFontSize: 20,
            },  
            axisY:{ 
                title:"Задачи",
                titleFontSize: 20,
            },
            data: [
                {
                    type: "line",
                    color: "black",
                    dataPoints: data_points_ideal
                },
                {         
                    type: "stepLine",
                    markerSize: 5,
                    color: "green",
                    dataPoints: data_points_real
                }    
            ]
        };

        var chart = new CanvasJS.Chart("graphic", data_chart);
        chart.render();
    };

    var load_highcharts = function(iterate_id){
        $.ajax({
            url : "/statistic/get_data_graphic", 
            type : "GET",
            data : { 'iterate_id' : iterate_id },
            dataType: "json",
            success : function(data) {
                render_chart(data);
            },
            error : function(err) {
                console.log(err);
            }
        })
    }

    var load_data = function(){
        var iterate_id = $("#which_iteration option:selected").attr('id');
        load_statistic( iterate_id );
        load_highcharts( iterate_id) ;
    };

    $(document).on('change', '#which_iteration', function(){
        load_data();
    });

    load_data();
})