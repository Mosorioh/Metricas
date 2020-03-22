console.log ("From validar")

function validar(){
    var Pais, Provincia, Ciudad, Sector;
    Pais = document.getElementById("selectPais").value;
    Provincia = document.getElementById("Provincia").value;
    Ciudad = document.getElementById("Ciudad").value;
    Sector = document.getElementById("Sector").value;
    console.log ("Send pais: " + Pais);
    console.log ("Send Provincia: " + Provincia);
    console.log ("Send Ciudad: " + Ciudad);
    console.log ("Send Sector: " + Sector);

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

 

}