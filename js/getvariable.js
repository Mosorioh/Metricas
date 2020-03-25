//<!----- Get variable url------>
//<!----- Script 5------>
//<!--El siguiente bloque optine de la url la varible Get-->
//console.log("Get.js")
    /**
     * @param String name
     * @return String
     */
    function getParameterByName(name) {
        name = name.replace(/[\[]/, "\\[").replace(/[\]]/, "\\]");
        var regex = new RegExp("[\\?&]" + name + "=([^&#]*)"),
        results = regex.exec(location.search);
        return results === null ? "" : decodeURIComponent(results[1].replace(/\+/g, " "));
    }
    var Pais = getParameterByName('Pais');
    //console.log("GET Pais ID:" + Pais )

//<!----- Get variable url------>
//<!----- Script 5------>
//<!--El siguiente bloque optine de la url la varible Get-->
//console.log("Get.js")
    /**
     * @param String name
     * @return String
     */
    function getParameterByName(name) {
        name = name.replace(/[\[]/, "\\[").replace(/[\]]/, "\\]");
        var regex = new RegExp("[\\?&]" + name + "=([^&#]*)"),
        results = regex.exec(location.search);
        return results === null ? "" : decodeURIComponent(results[1].replace(/\+/g, " "));
    }
    var Provincia = getParameterByName('Provincia');
   // console.log("GET Provincia ID:" + Provincia )

//<!----- Get variable url------>
//<!----- Script 5------>
//<!--El siguiente bloque optine de la url la varible Get-->
//console.log("Get.js")
    /**
     * @param String name
     * @return String
     */
    function getParameterByName(name) {
        name = name.replace(/[\[]/, "\\[").replace(/[\]]/, "\\]");
        var regex = new RegExp("[\\?&]" + name + "=([^&#]*)"),
        results = regex.exec(location.search);
        return results === null ? "" : decodeURIComponent(results[1].replace(/\+/g, " "));
    }
    var Ciudad = getParameterByName('Ciudad');
    //console.log("GET Ciudad ID:" + Ciudad )

    //<!----- Get variable url------>
//<!----- Script 5------>
//<!--El siguiente bloque optine de la url la varible Get-->
//console.log("Get.js")
    /**
     * @param String name
     * @return String
     */
    function getParameterByName(name) {
        name = name.replace(/[\[]/, "\\[").replace(/[\]]/, "\\]");
        var regex = new RegExp("[\\?&]" + name + "=([^&#]*)"),
        results = regex.exec(location.search);
        return results === null ? "" : decodeURIComponent(results[1].replace(/\+/g, " "));
    }
    var Sector = getParameterByName('Sector');
    //console.log("GET Sector ID:" + Sector )

    //<!----- Get variable url------>
//<!----- Script 5------>
//<!--El siguiente bloque optine de la url la varible Get-->
//console.log("Get.js")
    /**
     * @param String name
     * @return String
     */
    function getParameterByName(name) {
        name = name.replace(/[\[]/, "\\[").replace(/[\]]/, "\\]");
        var regex = new RegExp("[\\?&]" + name + "=([^&#]*)"),
        results = regex.exec(location.search);
        return results === null ? "" : decodeURIComponent(results[1].replace(/\+/g, " "));
    }
    var Ubicacion = getParameterByName('Ubicacion');
   // console.log("GET Ubicacion ID:" + Ubicacion )



///////////////////////////////////////////////////////////////////
// Lista de variablas obtenidas
///////////////////////////////////////////////////////////////////
console.log("GET- Pais ID:" + Pais)
console.log("GET- Provincia ID:" + Provincia)
console.log("GET- Ciudad ID:" + Ciudad)
console.log("GET- Sector ID:" + Sector)
console.log("GET- Ubicacion ID:" + Ubicacion)

///////////////////////////////////////////////////////////////////
// Condicionales segun valores de varianles
///////////////////////////////////////////////////////////////////
if(Ubicacion > 0){
    console.log ("Working with Ubicacion");
    // Urls
    var Urlpie1 = 'http://181.199.66.129:5060/PieChart/' +Pais+ '/' +Provincia+ '/' +Ciudad+ '/' +Sector+ '/' +Ubicacion
    var UrlMotivo = 'http://181.199.66.129:5060/motivo/' +Pais+ '/' +Provincia+ '/' +Ciudad+ '/' +Sector+ '/' +Ubicacion
    var UrlMain = 'http://181.199.66.129:5060/Grafico/' +Pais+ '/' +Provincia+ '/' +Ciudad+ '/' +Sector + '/' +Ubicacion
    var UrlExpuestos = 'http://181.199.66.129:5060/Expuestos/'+Pais+ '/' +Provincia+ '/' +Ciudad+ '/' +Sector + '/' +Ubicacion
    var UrlRiesgo = 'http://181.199.66.129:5060/Expuestos/'+Pais+ '/' +Provincia+ '/' +Ciudad+ '/' +Sector + '/' +Ubicacion
    // Print pantalla
    console.log ("URL Pie 1 Total: " + Urlpie1)
    console.log ("URL Pie 2 Motivo: " + UrlMotivo)
    console.log ("URL Main Graphic: " + UrlMain)
    console.log ("URL Expuestos Total: " + UrlExpuestos)
    console.log ("URL Riesgos Motivo: " + UrlRiesgo)

    } else if (Sector > 0){

    console.log ("Working with Sector");
    // Urls
    var Urlpie1 = 'http://181.199.66.129:5060/PieChart/' +Pais+ '/' +Provincia+ '/' +Ciudad+ '/' +Sector
    var UrlMotivo = 'http://181.199.66.129:5060/motivo/' +Pais+ '/' +Provincia+ '/' +Ciudad+ '/' +Sector
    var UrlMain = 'http://181.199.66.129:5060/Grafico/' +Pais+ '/' +Provincia+ '/' +Ciudad+ '/' +Sector 
    var UrlExpuestos = 'http://181.199.66.129:5060/Expuestos/'+Pais+ '/' +Provincia+ '/' +Ciudad+ '/' +Sector 
    var UrlRiesgo = 'http://181.199.66.129:5060/Expuestos/'+Pais+ '/' +Provincia+ '/' +Ciudad+ '/' +Sector 
    // Print pantalla
    console.log ("URL Pie 1 Total: " + Urlpie1)
    console.log ("URL Pie 2 Motivo: " + UrlMotivo)
    console.log ("URL Main Graphic: " + UrlMain)
    console.log ("URL Expuestos Total: " + UrlExpuestos)
    console.log ("URL Riesgos Motivo: " + UrlRiesgo)

    } else if (Ciudad > 0){

    console.log ("Working with Ciudad");
    // Urls
    var Urlpie1 = 'http://181.199.66.129:5060/PieChart/' +Pais+ '/' +Provincia+ '/' +Ciudad
    var UrlMotivo = 'http://181.199.66.129:5060/motivo/' +Pais+ '/' +Provincia+ '/' +Ciudad
    var UrlMain = 'http://181.199.66.129:5060/Grafico/' +Pais+ '/' +Provincia+ '/' +Ciudad
    var UrlExpuestos = 'http://181.199.66.129:5060/Expuestos/'+Pais+ '/' +Provincia+ '/' +Ciudad
    var UrlRiesgo = 'http://181.199.66.129:5060/Expuestos/'+Pais+ '/' +Provincia+ '/' +Ciudad
    // Print pantalla
    console.log ("URL Pie 1 Total: " + Urlpie1)
    console.log ("URL Pie 2 Motivo: " + UrlMotivo)
    console.log ("URL Main Graphic: " + UrlMain)
    console.log ("URL Expuestos Total: " + UrlExpuestos)
    console.log ("URL Riesgos Motivo: " + UrlRiesgo)

    }else if(Provincia > 0){
    
        console.log ("Working with Provincia");
        // Urls
        var Urlpie1 = 'http://181.199.66.129:5060/PieChart/' +Pais+ '/' +Provincia
        var UrlMotivo = 'http://181.199.66.129:5060/motivo/' +Pais+ '/' +Provincia
        var UrlMain = 'http://181.199.66.129:5060/Grafico/' +Pais+ '/' +Provincia
        var UrlExpuestos = 'http://181.199.66.129:5060/Expuestos/'+Pais+ '/' +Provincia
        var UrlRiesgo = 'http://181.199.66.129:5060/Expuestos/'+Pais+ '/' +Provincia
        // Print pantalla
        console.log ("URL Pie 1 Total: " + Urlpie1)
        console.log ("URL Pie 2 Motivo: " + UrlMotivo)
        console.log ("URL Main Graphic: " + UrlMain)
        console.log ("URL Expuestos Total: " + UrlExpuestos)
        console.log ("URL Riesgos Motivo: " + UrlRiesgo)
    
    } else if(Pais > 0){
    
        console.log ("Working with Pais");
        // Urls
        var Urlpie1 = 'http://181.199.66.129:5060/PieChart/' +Pais
        var UrlMotivo = 'http://181.199.66.129:5060/motivo/' +Pais
        var UrlMain = 'http://181.199.66.129:5060/Grafico/' +Pais
        var UrlExpuestos = 'http://181.199.66.129:5060/Expuestos/'+Pais
        var UrlRiesgo = 'http://181.199.66.129:5060/Expuestos/'+Pais
        // Print pantalla
        console.log ("URL Pie 1 Total: " + Urlpie1)
        console.log ("URL Pie 2 Motivo: " + UrlMotivo)
        console.log ("URL Main Graphic: " + UrlMain)
        console.log ("URL Expuestos Total: " + UrlExpuestos)
        console.log ("URL Riesgos Motivo: " + UrlRiesgo)
    
    } else {
        console.log ("pais es 0");
    }
            
                