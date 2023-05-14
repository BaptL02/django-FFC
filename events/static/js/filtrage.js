  document.addEventListener('DOMContentLoaded', function() {
    const listItems = document.querySelectorAll('#filtre li');

    listItems.forEach((listItem) => {
      const checkbox = listItem.querySelector('input[type="checkbox"]');

      checkbox.style.visibility = 'hidden';

      listItem.addEventListener('click', function() {
        checkbox.click();
      });

      checkbox.addEventListener('change', function() {
        if (this.checked) {
          listItem.style.backgroundColor = 'lightskyblue';
          listItem.style.borderRadius = '10px'
        } else {
          listItem.style.backgroundColor = '';
        }
      });
    });
  });