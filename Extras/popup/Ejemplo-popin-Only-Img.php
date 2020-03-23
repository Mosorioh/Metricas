<?php
// Esta pagina muestra como se hace un pop in publicitario,
// el popin consta de un solo elemeto Imagen 
// Imagen
?>

<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">
<head>
<title>jQuery Slide Popup</title>
<link rel="stylesheet" type="text/css" href="style-popup.css" />	
<script type="text/javascript" src="Jquery/jquery.js"></script>
<script type="text/javascript">
function openDialog() {
	$('#overlay').fadeIn('fast', function() {
		$('#popup').css('display','block');
        $('#popup').animate({'left':'30%'},500);
    });
}

function closeDialog(id) {
	$('#'+id).css('position','absolute');
	$('#'+id).animate({'left':'-100%'}, 500, function() {
		$('#'+id).css('position','fixed');
		$('#'+id).css('left','100%');
		$('#overlay').fadeOut('fast');
	});
}
</script>
</head>

<body onload="openDialog();">
<div id="content">
<div id="overlay" class="overlay"></div>
<a onclick="openDialog();">Mostrar publicidad</a>
<div id="popup" class="popup">
	<a onclick="closeDialog('popup');" class="close"></a>
	<div>
    	<h2>Camara Olimpus e330</h2>
        <div style="float:left; width:270px;">
        	<img src="Img-Popup/producto.gif" width="270" />
        </div>
        <div style="float:left; width:285px;">
					Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. 
					Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. 
					Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. Nulla consequat massa quis enim. 
					Donec pede justo, fringilla vel, aliquet nec, vulputate eget, arcu.<br/><br/>
            <div style="margin-top:0px;">
            </div>
    </div>
	</div>
</div>
</div>
</body>
</html>
