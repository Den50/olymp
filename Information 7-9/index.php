<head>
	<meta charset="utf-8">
</head>
<?php
if(isset($_GET['enter'])){
		echo $_GET['data']."<br>";

		for ($i=0; $i < strlen($_GET['data']); $i++) { 

				if($i % 2 == 0){
					echo substr($_GET['data'], $i, 1)." ";
				}
				else{
					echo substr($_GET['data'], -($i+1), 1);
				}
				
				


			
		}
	
	
}
?>
<form action="" method="GET">
	<input type="text" name="data">
	<input type="submit" value="Закодировать" name="enter">
</form>