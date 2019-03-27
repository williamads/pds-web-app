(function(){
    var button = document.getElementById('start-button');
    button.addEventListener('click', foo);
    function foo(){
        console.log('aqui1');
        var objForm = serializeForm("start");
        printText("Iniciando envio de formularios...")
        $.ajax({
            method: "POST",
            url: "/api/start/",
            data: objForm
        }).done(function( msg ) {
            alert("Data Saved: " + msg.success );
        });
    }
    function serializeForm(formName) {
        var fields = document.forms[formName].querySelectorAll("input, select, textarea");
        var obj = {};
        for (var i = 0, len = fields.length; i < len; i++) {
            if (fields[i].name) {
                var key = fields[i].name;
                obj[key] = fields[i].type == "checkbox" ? fields[i].checked : fields[i].value;
            }
        }
        return obj;
    }
    function printText(string){
        var parag = document.getElementById("paragraph");
        var node = document.createTextNode(string);
        parag.appendChild(node);

    }
    console.log('inicio');
})();


