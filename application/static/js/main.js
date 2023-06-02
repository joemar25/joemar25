$(function() {
  var $nav = $(".nav");

  $(document).on("click", ".nav-toggle", function () {
    $nav.toggleClass("open");
  });
});