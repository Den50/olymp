function reverse() {
	var word = $('#word').val();
	var KIndex = $('#k_index').val();
	if(KIndex != word.length){
		alert('Error: K != N');
	}
	else{
		if(word.length % 2 == 0){
			if(word.substr(0, word.length - word.length / 2) == word.substr(word.length / 2, word.length).split('').reverse().join('')){
				$('.value').text("\n" + 0);
			}
			else{
			var time = word.substr(0, word.length - 1);
			$('.value').text(time.length + '___' + time.split('').reverse().join(''));
			}
		}
		else{
			if(word.substr(0, word.length - Math.ceil(word.length / 2)) == word.substr(Math.ceil(word.length / 2), word.length).split('').reverse().join('')){
				$('.value').text(0);
			}
			else{
			var time = word.substr(0, word.length - 1);
			$('.value').text(time.length + "____" + time.split('').reverse().join(''));
			}
		}
	}
}