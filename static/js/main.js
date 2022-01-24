let formName=document.getElementById("form_name")
let formComment=document.getElementById("form_comment")
document.getElementById("button_send").onclick=function(){
    data={
        name:formName.value,
        comment:formComment.value,
        date:Date.now()
    }
    
    const xhr = new XMLHttpRequest();
    let jsonText = JSON.stringify(data);
    xhr.open("POST","/chat",false)
    xhr.setRequestHeader("Content-Type","application/json")
    xhr.send(jsonText)
    
    if(xhr.status!==200){
        console.log(xhr.statusText)
    }
}

document.getElementById("button_update").onclick=function(){
    data={
        name:formName.value,
        comment:formComment.value,
        date:Date.now()
    }
    
    const xhr = new XMLHttpRequest();
    let jsonText = JSON.stringify(data);
    xhr.open("GET","/chat",false)
    xhr.send()
    
    if(xhr.status!==200){
        console.log(xhr.statusText)
    }else{
        chats=JSON.parse(xhr.responseText)
        for(const c of chats){
            console.log(c)
        }
    }
}