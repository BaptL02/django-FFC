$(document).ready(function() {
    $('.bouton-filtre').click(function() {
        $.ajax({
            url: "{% url 'en_livrees_MSFS' %}?filtre=true",
            type: "GET",
            success: function(response) {
              }
          });
      });
  });

