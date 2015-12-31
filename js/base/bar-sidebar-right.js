// https://stackoverflow.com/questions/20671303/bootstrap-3-changing-div-order-on-small-screens-only/20672040#20672040

$(function() {
  $(window).resize(function() {
    var w = $(window).width();
    if (w < 992 && $('#base-sidebar-right-remainder-tucked').children().length > 0) {
      $('#base-sidebar-right-remainder-content').prependTo( $('#base-sidebar-right-remainder-bottom') );
    } else if (w > 992 && $('#base-sidebar-right-remainder-bottom').children().length > 0) {
      $('#base-sidebar-right-remainder-content').prependTo( $('#base-sidebar-right-remainder-tucked') );
    }
  });
});
