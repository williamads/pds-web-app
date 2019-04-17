(function(){
    var button = document.getElementById('start-button');
    button.addEventListener('click', foo);
    function foo(){
        var objForm = serializeForm("start");
        console.log(objForm);
        $.ajax({
            method: "POST",
            url: "/pds_web/script",
            data: objForm
        })
    }
    function serializeForm(formName) {
        var fields = document.forms[formName].querySelectorAll("textarea");
        var obj = {};
        for (var i = 0, len = fields.length; i < len; i++) {
            if (fields[i].name) {
                var key = fields[i].name;
                obj[key] = fields[i];
            }
        }
        console.log(obj);
        return obj;
    }
})();



