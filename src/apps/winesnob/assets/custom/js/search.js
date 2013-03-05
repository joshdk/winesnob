;(function($){

	$(function(){
		$("#search").submit(function(){
			base = "/results/";
			query = $("#query").val();

			if(query.length > 0){
				window.location.href = base + query;
			// }else{
				// window.location.href = base + "wine";
			}
			return false;
		});
	});

})(jQuery);
