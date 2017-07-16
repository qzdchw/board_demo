<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>留言板</title>
    <link rel="stylesheet" type="text/css" href="http://localhost:9999/message/base.css">

</head>
<body>

<form action="/message" method="post">
        <div class="center">
            <input type="text" name="id_name" placeholder="标题" id="key"><br>
            <textarea rows="10" cols="30" name="text"></textarea><br>
            <button id="sure" type="submit">确定</button>
        </div>
</form>


 <p>共有<span id="long">{{lenlen}}</span>条留言</p>
%for i in nid:             
        {{ i[0] }} 
        {{ i[1] }} 
        <br>
    
%end 


<script type="text/javascript">
</script>
</body> 
</html>