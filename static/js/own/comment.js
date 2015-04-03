$(document).ready(function(){ 	

      var load_comment = function(args){
            $.ajax({
            url : "/comment/create", 
            type : "GET",
            data : args,
            dataType: "html",
            success : function(data) { 
                  $('#lst-comments').append(data);
            },
            error : function(err) {
                  console.log(err);
            }
        })
      }

      $('#add_comment').on('click', function(){
            var text =  $('#text_comment').val();
            if ( $(this).attr('data-forum') ) {
                  load_comment( { 'id_forum' : $(this).attr('data-forum'), 'text' : text } )
            }
            else {
                  load_comment( { 'id_task' : $(this).attr('data-task'),  'text' : text } )
            }
      });

})