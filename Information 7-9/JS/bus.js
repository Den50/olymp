function enter(){
	var Child   = Number($('.children').val()),
			parents = Number($('.parents').val()),
			bus			= Number($('.k_index').val());
	if(Child < 0 || Child == 0 || Child == '' && parents < 2 || parents == 0 || parents == ''){
		alert('Error');
	}
	else{
	if((Child + parents) % bus != 0){
		console.log(Child + "+" + parents + '=' + Child + parents);
		alert('0');
	}
	else{
		alert((Child + parents) / bus);
	}
	}
}