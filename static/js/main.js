function verdatos(){
    var listapost;
    var identificador=document.getElementById("login_usuario").innerHTML;
    var url="http://localhost:5000/consultarmail"
    var datos={
        "username":identificador,
        "tipo":2  }
    
    fetch(url,
        {
            method:'POST',
            body:JSON.stringify(datos),
            headers:{
                "Content-type":"application/json;charset=UTF-8"
            }

    }
        )
    .then(response=>response.json())
    .then((data)=>{
    listapost=data;    
    var info=""
    
    for(var i=0;i<listapost.length;i++)
    {
        info=info+"<tr'>"
        info=info+"<td>"+listapost[i]['id'] + "</td>"
        info=info+"<td>"+listapost[i]['remitente'] + "</td>"
        info=info+"<td>"+listapost[i]['destinatario'] + "</td>"
        info=info+"<td>"+listapost[i]['fecha'] + "</td>"
        info=info+"<td>"+listapost[i]['asunto'] + "</td>"
        info=info+"<td>"+listapost[i]['mensaje'] + "</td>"
        if(listapost[i]['tipo']=='Mensaje Recibido'){
        info=info+"<td> <span class='badge rounded-pill bg-info'>"+listapost[i]['tipo']+"</span></td>"
        }else{
        info=info+"<td> <span class='badge rounded-pill bg-warning'>"+listapost[i]['tipo']+"</span></td>"    

        }

        info=info+"</tr>"
    
    }
    
 
    document.getElementById("listado").innerHTML=info
    }
    )
    
    }