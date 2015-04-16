$(document).ready(function(){
    var notification = function(action){
        $.ajax({
            url : "/notification/get_notification", 
            type : "GET",
            data : {'action' : action},
            success : function(data) {
                $('.modal-body').html(data);
                $('.btn-modal').hide();
                $('#myModal').modal('show');
            },
            error : function(err) {
                alert("Fail GET /notification/get_notification");
            }
        })
    };

    $(document).on('click', '.active_notification', function(){
        notification($(this)[0].id);
    })
})