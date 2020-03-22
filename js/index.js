$(document).ready(function(){
  $.ajax({
    type: 'GET',
    url: 'http://192.168.100.233:5050/pais',
    datatype: 'json',
    success: function (data) {
      console.log(data);
      //console.log(data[2].Id);
    var pais = data;
    console.log(pais);
  }
  })
  .done(function(listas_rep){
    $('#lista_reproduccion').html(listas_rep)
  })
  .fail(function(){
    alert('Hubo un errror al cargar las listas_rep')
  })




  
  $('#lista_reproduccion').on('change', function(){
    var id = $('#lista_reproduccion').val()
    $.ajax({
      type: 'POST',
      url: 'http://192.168.100.233:5050/provincia/',
      data: {'Id': Id},
      success: function (data) {
        console.log(data);
        //console.log(data[2].Id);
    }
    })
    .done(function(listas_rep){
      $('#videos').html(listas_rep)
    })
    .fail(function(){
      alert('Hubo un errror al cargar los vídeos')
    })
  })

  $('#enviar').on('click', function(){
    var resultado = 'Lista de reproducción: ' + $('#lista_reproduccion option:selected').text() +
    ' Video elegido: ' + $('#videos option:selected').text()

    $('#resultado1').html(resultado)
  })


  
})