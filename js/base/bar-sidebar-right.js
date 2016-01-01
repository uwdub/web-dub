// https://stackoverflow.com/questions/20671303/bootstrap_3-changing-div-order-on-small-screens-only/20672040#20672040

$(function() {
  function base_sidebar_right_position_remainder() {
    var w = $(window).width();
    if (w < 992 && $('#base-sidebar-right-remainder-tucked').children().length > 0) {
      $('#base-sidebar-right-remainder-content').prependTo( $('#base-sidebar-right-remainder-bottom') );
    } else if (w > 992 && $('#base-sidebar-right-remainder-bottom').children().length > 0) {
      $('#base-sidebar-right-remainder-content').prependTo( $('#base-sidebar-right-remainder-tucked') );
    }
  }

  $(window).ready(base_sidebar_right_position_remainder);
  $(window).resize(base_sidebar_right_position_remainder);
});
