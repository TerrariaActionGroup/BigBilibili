$(function(){ 
  $(".nav-main li").hover(function(){
    $("ul",this).slideDown(300)
  },function(){
    $("ul",this).hide();
    });
}); 
/*$(function(){ 
  $(".i_user").hover(function(){
    $("img",this).animate({top:'12px',
                            width:'66px',
                            height:'66px',
                            left:'-13px',
                            },'200');
    $(".i_menu",this).slideDown(500);
  },function(){
    $("img",this).animate({top:'0px',
                            width:'40px',
                            height:'40px',
                            left:'0px',
                            },'200');
    $(".i_menu",this).hide();
    });
}); 
*/

// 线程 IDs
var mouseover_tid = [];
var mouseout_tid = [];
 
$(function(){
        $('.i_user').hover(
            // 鼠标进入
            function(){
                var _self = this;
                // 停止卷起事件
                clearTimeout(mouseout_tid[0]);
                // 当鼠标进入超过 0.2 秒, 展开菜单, 并记录到线程 ID 中
                mouseover_tid[0] = setTimeout(function() {
                    $("img",_self).animate({top:'12px',
                            width:'66px',
                            height:'66px',
                            left:'-13px',
                            },'200');
                    $(".i_menu",_self).slideDown(150);
                }, 400);
            },
 
            // 鼠标离开
            function(){
                var _self = this;
                // 停止展开事件
                clearTimeout(mouseover_tid[0]);
                // 当鼠标离开超过 0.2 秒, 卷起菜单, 并记录到线程 ID 中
                mouseout_tid[0] = setTimeout(function() {
                    $("img",_self).animate({top:'0px',
                            width:'40px',
                            height:'40px',
                            left:'0px',
                            border:'2px',
                            },'200');
                    $(".i_menu",_self).slideUp(150);
                }, 400);
            }
        );
});