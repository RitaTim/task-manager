$(document).ready(function(){
	$('#myModal').modal('hide');

	$('.data-table').dataTable({
		"paging"   : false,
		"searching": false,
		"bInfo"	   : false,
	});
})