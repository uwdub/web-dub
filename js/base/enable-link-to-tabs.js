// https://stackoverflow.com/questions/7862233/twitter-bootstrap-tabs-go-to-specific-tab-on-page-reload-or-hyperlink

$(function() {
  // Javascript to enable link to tab
  var hash = document.location.hash;
  var prefix = "tab_";
  if (hash) {
    $('.nav-tabs a[href='+hash.replace(prefix,"")+']').tab('show');
    $('.nav-pills a[href='+hash.replace(prefix,"")+']').tab('show');
  }

  // If we link to a hash within our page
  $(window).on('hashchange', function(e) {
    $('.nav-tabs a[href='+ window.location.hash.replace(prefix,"")+']').tab('show');
    $('.nav-pills a[href='+ window.location.hash.replace(prefix,"")+']').tab('show');
  });

  // Change hash for page-reload
  $('.nav-tabs a').on('shown.bs.tab', function (e) {
    window.location.hash = e.target.hash.replace("#", "#" + prefix);
  });
  $('.nav-pills a').on('shown.bs.tab', function (e) {
    window.location.hash = e.target.hash.replace("#", "#" + prefix);
  });
});
