function enter(){
	var lenles = 50;
	var data= $('.data').val();
	if(data > 15){
		alert("Error");
	}
	else{
		var minutes = (8 * 60 + lenles*data);
		console.log(Math.floor(minutes / 60) + ' - ' + (minutes % 60));
		//console.log(summ);
		//var minutes = 
		//alert(100 % 60);
		alert(Math.floor(minutes / 60) + ':' + (minutes % 60));
	}
}