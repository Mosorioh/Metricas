console.log ("Conexion js Link")
//<!----- Script 1------>
//<!-- Get all paises -->
//<script>
    fetch('http://181.199.66.129:5050/pais')
    .then(ListPaises=>ListPaises.json())
    .then(ListPaises=>{
      console.log("Lista de Paises")
        console.log(ListPaises)
        
        var resultado = document.getElementById('selectPais');
        var n = 0;
        selectPais.innerHTML = '';
        selectPais.innerHTML = '<option selected="selectPais">Selecciona Tu Pais</option>';
        
        for(let dato of ListPaises){
            n++;
            resultado.innerHTML += `
            <option value="${dato.Id}">${dato.Name_Pais}</option>
            
            `;
           
        }
       
    })
    
//</script>


//<!----- Script 2------>
//<!-- get provincia Segun opcion seleccionada en el drowndoon-->
//<script>	  
	$(document).ready(function(){
    $("#selectPais").on("change",function(){						
      var PaisSelectd=$(this).val()//obtenemos el valor seleccionado en una variable	
      console.log("Pais Seleccionado: " + PaisSelectd) 

  fetch('http://181.199.66.129:5050/provincia/'+PaisSelectd+'')

	.then(Listprovincia=>Listprovincia.json())
	.then(Listprovincia=>{
  console.log("Provincias")   
  console.log( Listprovincia)
  
    var resultado = document.getElementById('Provincia');
        var n = 0;

        
        Provincia.innerHTML = '<option selected="Provincia" >Selecciona Tu Region</option>';
        
        for(let dato of Listprovincia){
            n++;
            resultado.innerHTML += `
            <option value="${dato.Id}">${dato.Name_provincia}</option>
            
            `;
			}
			
			})
		})
	})
//</script>

//<!----- Script 3------>
//<!-- get provincia Segun opcion seleccionada en el drowndoon-->
//<script>	  
	$(document).ready(function(){
    $("#Provincia").on("change",function(){						
      var ProvinciaSelectd=$(this).val()//obtenemos el valor seleccionado en una variable	
      console.log("Provincia Seleccionado: " + ProvinciaSelectd) 

  fetch('http://181.199.66.129:5050/City/'+ProvinciaSelectd+'')

	.then(Listcity=>Listcity.json())
	.then(Listcity=>{
  console.log("City")   
  console.log( Listcity)
  
    var resultado = document.getElementById('Ciudad');
        var n = 0;
        Ciudad.innerHTML = '';
        Ciudad.innerHTML = '<option selected="Ciudad" >Selecciona Tu Ciudad</option>';
        
        for(let dato of Listcity){
            n++;
            resultado.innerHTML += `
            <option value="${dato.Id}">${dato.City_name}</option>
            
            `;
			}
			
			})
		})
	})
// </script>


//<!----- Script 3------>
//<!-- get provincia Segun opcion seleccionada en el drowndoon-->
//<script>	  
$(document).ready(function(){
  $("#Ciudad").on("change",function(){						
    var CitySelectd=$(this).val()//obtenemos el valor seleccionado en una variable	
    console.log("Ciudad Seleccionado: " + CitySelectd)  

fetch('http://181.199.66.129:5050/Sector/'+CitySelectd+'')

.then(ListSector=>ListSector.json())
.then(ListSector=>{
console.log("Sector")   
console.log( ListSector)

  var resultado = document.getElementById('Sector');
      var n = 0;
      Sector.innerHTML = '';
      Sector.innerHTML = '<option selected="Sector" >Selecciona Tu Sector</option>';
      
      for(let dato of Listcity){
          n++;
          resultado.innerHTML += `
          <option value="${dato.Id}">${dato.Sector}</option>
          
          `;
    }
    
    })
  })
})