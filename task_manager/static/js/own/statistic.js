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
                    $.each( data_user.progress_bar, function( i, task ){
                        lst_progress += "<div id='" + task.id + "' class='progress-bar task_title " + task.css_class + "' role='progressbar' style='width:" + task.width + "%'><a href='#' data-toggle='tooltip' title='Выполнение: " + task.perform_time+ "'>" + task.title + "</a></div>";
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

    var render_chart = function(data, size){
        var start_time  = data.iterate_time.start_line;
        var end_time    = data.iterate_time.dead_line;
        var count_tasks = data.count_tasks;
        
        data_points_ideal = [
            { x: new Date(start_time), y: count_tasks },
            { x: new Date(end_time),   y: 0 }
        ];

        var data_points_real = [];
        var data_tooltipe    = [];
        var num_task = count_tasks - 1;
        data_points_real.push(
            {x: new Date(start_time), y: count_tasks}
        );
        $.each( data.data_tasks, function( i, task ){
            data_points_real.push(
                {x: new Date(task.x_coordinate), y: num_task}
            );
            data_tooltipe.push(
                task.title_task + " <strong>" + task.perform_time
            );
            num_task -= 1;
        });                

        console.log(data_points_real);
        var data_chart = {
            width: size[0],
            height: size[1],
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
                if (data.data_tasks){
                    size = iterate_id ? [ window.innerWidth * 0.70, window.innerHeight * 0.45 ] : [ window.innerWidth * 0.32, window.innerHeight * 0.33 ];
                    render_chart(data, size);
                    $('.time-iterate').html(data.iterate_time.start_line + ' - ' + data.iterate_time.dead_line);
                }
            },
            error : function(err) {
                console.log(err);
            }
        })
    }

    var load_data = function(){
        var iterate_id = $("#which_iteration option:selected").attr('id');
        if (iterate_id) {
            load_statistic(iterate_id);
            load_highcharts(iterate_id);
            $('.info-item').height($('.info-item').innerHeight()/3 + Math.max($('.canvasjs-chart-canvas').innerHeight(), $('#tab1').innerHeight()));
        }
        else {
            load_highcharts();
            $('.canvasjs-chart-canvas').css({ 'width': '300px'});
        }
    };

    $(document).on('change', '#which_iteration', function(){
        load_data();
    });

    load_data();
})