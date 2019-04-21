(function(){
    var button = document.getElementById('start-button');
    var convolutionButton = document.getElementById('convolution-button');
    convolutionButton.addEventListener('click', conv_request);
    function conv_request(){
        button.className = 'waves-effect waves-light btn disabled';
        var objForm = serializeForm("convolution-form");
        console.log(objForm);
        $.ajax({
            method: "POST",
            url: "/convolution",
            data: objForm,
            success: function(response) {
                console.log(response.signal);
                drawConvolutionChart(response.signal);
            }
        }).done(button.className = 'waves-effect waves-light btn')
    }
    button.addEventListener('click', foo);
    function foo(){
        button.className = 'waves-effect waves-light btn disabled';
        var objForm = serializeForm("start");
        console.log(objForm);
        $.ajax({
            method: "POST",
            url: "/script",
            data: objForm,
            success: function(response) {
                console.log(response.signal);
                drawChart1(response.signal);
            }
        }).done(button.className = 'waves-effect waves-light btn')
    }
    function serializeForm(formName) {
        var fields = document.forms[formName].querySelectorAll("input, select, textarea");
        var obj = {};
        for (var i = 0, len = fields.length; i < len; i++) {
            if (fields[i].name) {
                var key = fields[i].name;
                obj[key] = fields[i].type == "checkbox" ? fields[i].checked : fields[i].value;
                ;
            }
        }
        return obj;
    }
})();



