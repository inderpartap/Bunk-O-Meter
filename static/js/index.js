$('#password').focusin(function(){
  $('form').addClass('up')
});
$('#password').focusout(function(){
  $('form').removeClass('up')
});


// Panda Eye movement
$(document).on( "mousemove", function( event ) {
  var dw = $(document).width() / 15;
  var dh = $(document).height() / 15;
  var x = (event.pageX/ dw)-5;
  var y = event.pageY/ dh;
  $('.eye-ball').css({
    width : x,
    height : y
  });
});

// 5.1 and 5.42 are roughly the central values
// validation


// $('.btn').click(function(){
//   $('form').addClass('wrong-entry');
//     setTimeout(function(){ 
//        $('form').removeClass('wrong-entry');
//      },3000 );
// });