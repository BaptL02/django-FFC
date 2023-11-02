
    var qcm = [];

    // Supposons que "qcm" est un tableau en JavaScript contenant les données des questions
    
    for (var i = 0; i < qcm.length; i++) {
        var question = {
            question: qcm[i].question,
            reponse1: qcm[i].reponse1,
            reponse2: qcm[i].reponse2,
            reponse3: qcm[i].reponse3,
            reponse4: qcm[i].reponse4
        };
        qcm.push(question);
    }


var frameDiv = document.querySelector('.frame');

for (var i = 0; i < qcm.length; i++) {
    var question = qcm[i].question;
    var reponse1 = qcm[i].reponse1;
    var reponse2 = qcm[i].reponse2;
    var reponse3 = qcm[i].reponse3;
    var reponse4 = qcm[i].reponse4;

    var div = document.createElement("div");
    div.className = "text_doc formation";
    div.innerHTML = "<p>" + question + "</p>" +
        "<br><input type='radio' name='1' value='a'><p>" + reponse1 + "</p>" +
        "<br><input type='radio' name='1' value='b'><p>" + reponse2 + "</p>" +
        "<br><input type='radio' name='1' value='c'><p>" + reponse3 + "</p>" +
        "<br><input type='radio' name='1' value='d'><p>" + reponse4 + "</p><br>";

    frameDiv.appendChild(div);
}

