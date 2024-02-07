// script that adds the class red
const $ = window.$;
$('#red_header').bind('click', function () {
  $('header').addClass('red');
});
