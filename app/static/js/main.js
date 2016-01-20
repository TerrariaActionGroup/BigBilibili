$(function(){ 
  $(".nav-main li").hover(function(){
    /*下拉框出现*/
    $("ul",this).slideDown(300)
  },function(){
    /*下拉框消失*/
    $("ul",this).hide();
    });
}); 
