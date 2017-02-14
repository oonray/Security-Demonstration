
<html>

  <head>
	<h1> The results:</h1>
	<hr/>
  </head>

<body>

<?php

if(!$argv[3]){
$argv[3] = '';
}
$result = system($argv[2]." ".$argv[3].'');
echo($result);

?>

<p>
<!--<b>NOTE:</b> If you are a student and can read this, you gained 10 extra points!!-->
</p>
<p>You are on the right track! try a Command!</p>
</body>
</html>

