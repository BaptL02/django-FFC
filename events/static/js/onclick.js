$(document).ready(function() {
    $('.bouton-filtre').click(function() {
        $.ajax({
            url: "{% url 'livrees_MSFS' %}?filtre=true",
            type: "GET",
            success: 
                console.info("Requete AJAX ok")
          });
      });
  });

