 $(document).ready(function(){
    $(".article__subtitle").click(function(){
   if ($(this).parent().find(".article__text").hasClass('active')){
     $(this).css("background-color","grey");
   }
   $(this).parent().find(".article__text").toggleClass("active");
   $(this).parent().find(".article__link").toggleClass("active");
  })
  })