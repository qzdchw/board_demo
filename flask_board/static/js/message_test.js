$.ajax({      
        url: 'http://localhost:5000/message_json',      
        datatype: "json",      
        type: 'get',      
        success: function (data) {      
        //成功后回调      
            var len=data.lenlen;
            var id=data.nid;
            var text=data.ntext;
            total(len);
            for (var i = 0; i < id.length; i++) 
            {
                createDiv(id[i],text[i])
            }
    },      
        error: function(){      
        //失败后回调      
            alert("服务器请求失败");      
        },             
})
function total(n)
{
    var span=document.getElementById("total");
    span.innerHTML=n;
}
function createDiv(idname,content)
{
    var oparent=document.getElementsByTagName('main');
    var sonbox=document.createElement('section')
    sonbox.className="messages";
    oparent[0].appendChild(sonbox);
    var user=document.createElement('p');
    user.className="ids";
    var text=document.createElement('p');
    text.className="texts";
    sonbox.appendChild(user);
    sonbox.appendChild(text);
    user.innerHTML=idname;
    text.innerHTML=content;
}