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
    zTranformButton.addEventListener('click', conv_request);
    function conv_request(){
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
                // console.log("data:image/jpg;base64,"+Convert.ToBase64String(response));
                // document.getElementById('z-transform-chart').innerHTML = response;
                // var blob = new Blob(response, {type: "application/zip"});
                // var objectURL = window.URL.createObjectURL(blob);
                // console.log(objectURL)
                // this is the trick - generates url like 
                // blob:http://localhost/adb50c88-9468-40d9-8b0b-1f6ec8bb5a32
                // myImage.src = objectURL;
                //drawConvolutionChart(response.signal);
            }
        }).done(button.className = 'waves-effect waves-light btn')
    }
    zTranformButton.addEventListener('click', conv_request);
// z transform request end

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



