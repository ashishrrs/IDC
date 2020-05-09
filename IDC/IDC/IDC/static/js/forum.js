function start_discussion()
{
	var html_id = "#new_disc";
	var button_id = "#new_disc_button";
	if($(html_id).css("display")=='block'){
		$(html_id).css("display","none");
		$(button_id).text("Start Discussion");

	}else{
		var a = Array(5).fill('\xa0').join('')+'Cancel'+Array(5).fill('\xa0').join('');
		$(html_id).css("display","block");
		$(button_id).text(a);
	}
}