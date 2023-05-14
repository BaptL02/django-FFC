<script type="application/javascript" src="https://ajax.googleapis.com/ajax/libs/jquery/3.6.0/jquery.min.js"></script>
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

