$(document).ready(function(){ 	

      var load_comment = function(id_forum){
            $.ajax({
            url : "/comment/create", 
            type : "GET",
            data : { 'id_forum' : id_forum, 'text' :  $('#text_comment').val()},
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
            load_comment($(this).attr('data-forum'));
      });

})