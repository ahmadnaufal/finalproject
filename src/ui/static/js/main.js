$('#test_set').removeAttr('disabled');
$('#cv_size').attr('disabled', 'disabled');

$('#eval_test').on('checked', function() {
	$('#test_set').removeAttr('disabled');
	$('#cv_size').attr('disabled', 'disabled');
});

$('#eval_cv').on('checked', function() {
	$('#test_set').attr('disabled', 'disabled');
	$('#cv_size').removeAttr('disabled');
});