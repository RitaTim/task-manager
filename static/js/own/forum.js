$(document).ready(function(){ 

      var show_form_forum = function(id_forum){
            $.ajax({
                  url : "/forum/edit_forum", 
                  type : "GET",
                  data : { 'id_forum' : id_forum},
                  success : function(data) { 
                        $('.modal-body').html(data);
                        $('#myModal').modal('show');
                  },
                  error : function(err) {
                      alert("Fail GET /forum/edit_forum" + id_forum);
                  }
            })
            $('.modal-title').text("Форум");
      };

      $(document).on('click', '.add-forum', function(){
            show_form_forum(0);
      });

	
	var load_comments = function(id_forum){
		$.ajax({
                  url : "/comment/get_comments", 
                  type : "GET",
                  data : { 'id_forum' : id_forum },
                  dataType: "html",
                  success : function(data) { 
                  	$('#box_comments').html(data);                        
                        $('#title').addClass('h2');
                  	return false;
                  },
                  error : function(err) {
                  	console.log(err);
                  }
            })
	}

	load_comments( $('.box-form a:first-child').find('label').prop('id') );

	$('.forum').on('click', function(){
		load_comments($(this).attr('id'));
            $('.active_forum').removeClass('active_forum');
            $(this).addClass('active_forum');
	});

})