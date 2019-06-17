(function(){
    
    // signal representation request begin
    var button = document.getElementById('start-button');
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

    // signal representation request end
    
    // convolution request begin
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
    
    // convolution request end
    
//  z transform reqeuest begin
    var zTranformButton = document.getElementById('z-transform-button');
    zTranformButton.addEventListener('click', z_transform_request);
    function z_transform_request(){
        button.className = 'waves-effect waves-light btn disabled';
        var objForm = serializeForm("z-transform-form");
        console.log(objForm);
        $.ajax({
            method: "POST",
            url: "/z-transform",
            data: objForm,
            success: function(response) {
                var image = new Image();
                image.src = "data:image/png;base64,"+response;
                var imageHolder = document.getElementById("z-transform-chart");
                while (imageHolder.firstChild) {
                    imageHolder.removeChild(imageHolder.firstChild);
                }
                imageHolder.append(image);
            }
        }).done(button.className = 'waves-effect waves-light btn')
    }
// z transform request end

//  discretize reqeuest begin
var zTranformButton = document.getElementById('discretize-button');
zTranformButton.addEventListener('click', discretize_request);
function discretize_request(){
    button.className = 'waves-effect waves-light btn disabled';
    var objForm = serializeForm("discretize-form");
    console.log(objForm);
    $.ajax({
        method: "POST",
        url: "/discretize",
        data: objForm,
        success: function(response) {
            console.log(response.signal);
            drawDiscretizeChart(response.signal);
        }
    }).done(button.className = 'waves-effect waves-light btn')
}
// discretize request end

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



