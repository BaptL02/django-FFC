<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.6.0/jquery.min.js"></script>
$(document).ready(function() {
    $('.bouton-filtre').click(function() {
        $.ajax({
            url: "{% url 'livrees_MSFS' %}?filtre=true",
            type: "GET",
            success: function(response) {
              }
          });
      });
  });
