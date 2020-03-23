console.log ("From validar")

function validar(){
    var Pais, Provincia, Ciudad, Sector, TotalPersonasCasa, TotalPersonasSalidas, IntervaloSalida, Ultimas48;
    Pais = document.getElementById("selectPais").value;
    Provincia = document.getElementById("Provincia").value;
    Ciudad = document.getElementById("Ciudad").value;
    Sector = document.getElementById("Sector").value;
    TotalPersonasCasa = document.getElementById("TotalPersonas").value;
    TotalPersonasSalidas = document.getElementById("TotalSalidas").value;
    IntervaloSalida = document.getElementById("IntervaloSalida").value;
    Ultimas48 = document.getElementById("Ultimas48").value;
    


    console.log ("Send pais: " + Pais);
    console.log ("Send Provincia: " + Provincia);
    console.log ("Send Ciudad: " + Ciudad);
    console.log ("Send Sector: " + Sector);
    console.log ("Send TotalPersonasCasa: " + TotalPersonasCasa);
    console.log ("Send TotalPersonasSalidas: " + TotalPersonasSalidas);
    console.log ("Send intervalo: " + IntervaloSalida);
    console.log ("Send Ultimas 48 Hora: " + Ultimas48);

    if(Pais === "Selecciona Tu Pais"){
        alert("Debe Selecionar un Pais");
        return false;
    }
    if(Provincia === "Selecciona Tu Region"){
        alert("Debe Selecionar una Region");
        return false;
    }
    if(Ciudad === "Selecciona Tu Ciudad"){
        alert("Debe Selecionar una Ciudad");
        return false;
    }
    if(Sector === "Selecciona Tu Sector"){
        alert("Debe Selecionar un Sector");
        return false;
    }
    if(TotalPersonasCasa === ""){
        alert("Debe Indicar cuantas Personas viven en su casa");
        return false;
    }
    if(TotalPersonasCasa < 1){
        alert("Solo se permiten valores mayor a 0");
        return false;
    }
    if(TotalPersonasSalidas === ""){
        alert("Debe Indicar cuantas Personas Salieron de su casa");
        return false;
    }
    if(TotalPersonasSalidas < 1){
        alert("Solo se permiten valores mayor a 0");
        return false;
    }
    if(TotalPersonasSalidas < TotalPersonasCasa){
        alert("El total de personas que salieron de la casa, No puede ser mayor al numero de personas que vivien en la casa");
        return false;
    }
    if(IntervaloSalida === ""){
        alert("Debe Indicar el tiempo aproximado de exposicion");
        return false;
    }
    if(IntervaloSalida < 0.5){
        alert("Debe Indicar el tiempo aproximado de exposicion");
        return false;
    }
    if(Ultimas48 === "select"){
        alert("Debe indicar si en las ultimas 48 horas salio alguien de su casa");
        return false;
    }
 

}