"use strict";var _typeof="function"==typeof Symbol&&"symbol"==typeof Symbol.iterator?function(e){return typeof e}:function(e){return e&&"function"==typeof Symbol&&e.constructor===Symbol&&e!==Symbol.prototype?"symbol":typeof e};!function n(l,s,d){function r(o,e){if(!s[o]){if(!l[o]){var i="function"==typeof require&&require;if(!e&&i)return i(o,!0);if(c)return c(o,!0);var t=new Error("Cannot find module '"+o+"'");throw t.code="MODULE_NOT_FOUND",t}var a=s[o]={exports:{}};l[o][0].call(a.exports,function(e){return r(l[o][1][e]||e)},a,a.exports,n,l,s,d)}return s[o].exports}for(var c="function"==typeof require&&require,e=0;e<d.length;e++)r(d[e]);return r}({1:[function(e,o,i){o.exports='<div class="jq-global__dialog js-jq-global__dialog"><div class="jq__main"><div class="login_logo"></div><ul class="tab-nav"><li class="active">注册</li><li>登录</li></ul><ul class="jq-global__tab-content"><li><div class="register-apply"><form> <input type="text" placeholder="手机号" class="phone register-phone"/><div class="phone-tip register-valid-tip">输入的手机号码无效，请输入正确的手机号码</div><div class="registered-tip phone-tip"></div><div class="input-wrap"> <input type="text" class="registerValidCode" placeholder="请输入验证码"/> <span class="getRegisterCode">获取短信验证码</span></div><div class="phone-tip register-pass-tip">请输入正确的短信验证码</div> <button type="submit" class="btn-register btn-style">注&nbsp;&nbsp;册</button> <span class="register-tip">注册即同意聚宽<a>服务协议</a>和<a>隐私条款</a></span></form></div><div class="register-message"><form> <input type="text" placeholder="8~20位密码，包含大小写英文字母和数字" class="set-pwd"/> <span class="phone-tip set-pwd-tip">请输入8-20位密码，包含大小写英文字母和数字</span> <input type="text" placeholder="设置昵称" class="set-nickname"/><div class="phone-tip set-nickname-tip"></div> <button type="submit" class="btn-finish btn-style">完&nbsp;&nbsp;成</button><p class="register-tip top20">注册即同意聚宽<a>服务协议</a>和<a>隐私条款</a></p></form></div><div class="jq-third-login"><div class="jq-third-login-wechat-text"><div class="jq-third-login-line"></div><p> <span>微信注册</span></p></div><div class="jq-third-login-wechat"><div class="jq-third-login-wechat-btn js-jq-login-wechat" data-type="wx"></div></div></div></li><li><div class=\'password-login clear\'><form name="formPwdLogin" class="formPwdLogin"> <input type="text" placeholder="手机号" class="phone pwd-phone" name="CyLoginForm[username]"/><div class="phone-tip login-pwd-tip">输入的手机号码无效，请输入正确的手机号码</div> <input type="password" class="jq-login__password" placeholder="请输入密码" name="CyLoginForm[pwd]"/><div class="phone-tip login-tip1"></div> <button class="login-submit btnPwdSubmit">登&nbsp;&nbsp;录</button> <a class="change-login-type to-validate">使用手机验证码登录 &gt;</> <a class="forget-password" href="/user/account/forgetpwd">忘记密码？</a></form></div><div class=\'valid-login clear\'><form> <input type="text" placeholder="手机号" class="phone valid-phone"/> <span class="phone-tip login-valid-tip">输入的手机号码无效，请输入正确的手机号码</span><span class="phone-tip login-img-tip"></span><div class="input-wrap"> <input type="text" placeholder="请输入8位验证码" class="loginValidCode"/> <span class="getloginCode">获取短信验证码</span></div><div class="phone-tip login-tip1"></div> <span class="phone-tip toManyApply">发送太频繁了，歇一歇再发吧</span> <button class="login-submit btnValidSubmit">登&nbsp;&nbsp;录</button> <a class="change-login-type to-password">使用账号密码登陆 &gt;</> <a class="forget-password" href="/user/account/forgetpwd">忘记密码？</a></form></div><div class="jq-third-login"><div class="jq-third-login-wechat-text"><div class="jq-third-login-line"></div><p> <span>微信登录</span></p></div><div class="jq-third-login-wechat"><div class="jq-third-login-wechat-btn js-jq-login-wechat" data-type="wx"></div></div></div></li></ul></div></div>'},{}],2:[function(require,module,exports){var indexComponent=function indexComponent(exports,node){var $,$node,$scope={registerFlag1:!0,registerFlag2:!0},$dialog1,$appDialog,domHtml=require("./index.component.html"),tabItem=!0,$dialog,applyFlag=!0,reg=/^[1](3|4|5|6|7|8|9)\d{9}$/,virtualNumReg=/^[1](3|4|5|6|7|8|9)\d{9}$|^111\d{8}$/,pwdReg=/^(?=.*[0-9])(?=.*[a-z])(?=.*[A-Z]).{8,20}$/,dialogFlag=!1,isMobile=function(){for(var e=new Array("Android","iPhone","SymbianOS","Windows Phone","iPad","iPod"),o=!0,i=navigator.userAgent,t=0;t<e.length;t++)if(0<i.indexOf(e[t])){o=!1;break}return!o},api={followList:"/user/account/followingList",followerList:"/user/account/followerList",followUser:"/community/follow/submitFollow",unFollowUser:"/community/follow/cancelFollow",buildUrl:"/algorithm/factor/build",redirectUrl:{factorDetailList:"/algorithm/factorAnaly/analyList?factorId=",factorDetail:"/algorithm/factorAnaly/detail?factorAnalyId="}},createDialog=function(o){function e(){$dialog.close()}return $dialog=BootstrapDialog.show({title:o.title,message:o.domHtml,cssClass:o.dialogCss||"",buttons:[{label:o.cancelBtnText||"取消",cssClass:o.cancelBtnCss||"btn-error",action:o.cancel&&o.cancel(e)||e},{label:o.submitBtnText||"确认提交",cssClass:o.submitBtnCss||"btn-link",action:o.submit&&o.submit(e)||e}],onshown:function(e){e.open(),o.onshown&&o.onshown()}}),o.btnWidth&&$dialog.$modalFooter.find(".btn").width(o.btnWidth),o.width&&($dialog.$modalContent.width(o.width),$dialog.$modalDialog.width(o.width)),o.marginTop&&$dialog.$modalDialog.css({marginTop:o.marginTop}),o.height&&($dialog.$modalContent.height(o.height),$dialog.$modalDialog.height(o.height),$dialog.$modalBody.css({"max-height":o.height-50})),o.clearPadding&&$dialog.$modalBody.css({padding:"0px"}),o.isAuto&&$dialog.$modalDialog.css({"margin-left":"auto","margin-right":"auto"}),o.isHideHeader&&$dialog.$modalHeader.hide(),o.isHideFooter&&$dialog.$modalFooter.hide(),$dialog};$scope.curDialog=null,$scope.loginCallback=null,$scope.waitTime=60,$scope.needImageValid=0,$scope.countTime=function(e,o){var i=$(e);i.addClass("msgCount"),i.attr("isCounting","true"),i.text("重新发送("+o+")");var t=setInterval(function(){"true"===$(e).attr("isCounting")&&(o-=1,$(e).text("重新发送("+o+")"),-1==o&&($(e).removeAttr("isCounting"),clearInterval($(e).attr("timeId")),$(e).removeAttr("timeId"),$(e).text("获取短信验证码"),i.removeClass("msgCount")))},1e3);$(e).attr("timeId",t)};var getNewImgCode=function(){$dialog1.find(".valideCode-img").attr("src","/common/verifyCode/valideCode?width=110")},tabLoginContent=function(){var e=$(this).index();$(this).addClass("active").siblings().removeClass("active"),$dialog1.find(".jq-global__tab-content li").eq(e).show().siblings().hide()},toValidLogin=function(){$(".password-login").hide(),$(".valid-login").show()},toPwdLogin=function(){$(".password-login").show(),$(".valid-login").hide()},gotoLoginNow=function(){$(".jq-global__tab-content li").eq(1).show().siblings().hide(),$(".tab-nav li").eq(1).addClass("active").siblings().removeClass("active")},phoneBlur=function(){var e=$(this),o=e.val(),i="CyLoginForm[username]"===e.attr("name")?virtualNumReg:reg;e.parents(".register-apply").find(".registered-tip").hide(),i.test(o)?(e.removeClass("jq-login__input_error"),e.next().hide()):(e.next().css("dispaly","inlineBlock"),e.addClass("jq-login__input_error"),e.next().show())},followCallback=function(e,o,i){var t,a=o.data,n=$node.find(".jq-c-follow-group .count").eq(0),l=parseInt(n.text());switch(a){case 1:t="关注",e.addClass("add"),i&&n.text(l-1);break;case 2:t="已关注",e.removeClass("add"),i&&n.text(l+1);break;case 3:t="关注",e.addClass("add"),i&&n.text(l-1);break;case 4:t="互相关注",e.removeClass("add"),i&&n.text(l+1)}e.text(t),e.attr("data-state",a),$scope.toggleFollowUserFlag=!1},passwordBlur=function(){$(this).next().hide()},getLoginValidCode=function(){if("true"!==$(this).attr("isCounting")&&""!=$(this).timeId){var e=$dialog1.find(".valid-phone").val();reg.test(e)?($dialog1.find(".login-valid-tip").hide(),$dialog1.find(".login-img-tip").hide(),$dialog1.find(".toManyApply").hide(),$scope.phoneData={mob:e},$scope.sendType="login",$scope.validCode($node,window.captcharData).getCaptchar()):$dialog1.find(".login-valid-tip").show()}},btnPwdLogin=function(){var e=$dialog1.find(".pwd-phone").val();return("CyLoginForm[username]"===$dialog1.find(".pwd-phone").attr("name")?virtualNumReg:reg).test(e)?$.ajax({type:"POST",dataType:"json",url:"/user/login/doLogin",data:$dialog1.find(".formPwdLogin").serialize(),success:function(e){if("00000"===e.code)exports.setCS&&exports.setCS(e.data.user.user,e.data.user.mobile,e.data.user.nickName),"/"===location.pathname?window.location.href="/view/user/floor":$scope.loginCallback(),window.loginStatus=!0,$scope.curDialog.close();else{if("10000"===e.code)for(var o in e.error)$dialog1.find(".password-login .login-tip1").html(e.error[o]);else"20000"===e.code?$dialog1.find(".password-login .login-tip1").html(e.msg):$dialog1.find(".password-login .login-tip1").text("输入手机号和密码不匹配");$dialog1.find(".password-login .login-tip1").show()}return!1},error:function(){$dialog1.find(".password-login .login-tip1").text("登录异常")}}):$dialog1.find(".login-pwd-tip").show(),!1},btnVlidLogin=function(){var e=$dialog1.find(".valid-phone").val();if(!reg.test(e))return $dialog1.find(".login-valid-tip").show(),!1;var o={mob:e,verifyCode:$dialog1.find(".loginValidCode").val()};return $.ajax({type:"POST",dataType:"json",url:"/user/login/doLogin5",data:o,success:function(e){"00000"===e.code?(exports.setCS&&exports.setCS(e.data.user.user,e.data.user.mobile,e.data.user.nickName),"/"===location.pathname?window.location.href="/view/user/floor":$scope.loginCallback(),window.loginStatus=!0,$scope.curDialog.close()):(e.error&&e.error.verifyCode&&$dialog1.find(".valid-login .login-tip1").text(e.error.verifyCode),e.msg&&$dialog1.find(".valid-login .login-tip1").html(e.msg),$dialog1.find(".valid-login .login-tip1").show())},error:function(){}}),!1},getRegisterValidCode=function(){if("true"!==$(this).attr("isCounting")&&""!=$(this).timeId){var e=$dialog1.find(".register-phone").val();if(!reg.test(e))return $dialog1.find(".register-valid-tip").show(),void $dialog1.find(".register-phone").addClass("jq-login__input_error");$dialog1.find(".register-valid-tip").hide(),$dialog1.find(".register-pass-tip").hide(),$dialog1.find(".register-img-tip").hide(),$(this).removeClass("jq-login__input_error"),$scope.phoneData={mob:e},$scope.sendType="register",$scope.validCode($node,window.captcharData).getCaptchar()}},submitValidCode=function(e){var n=$scope.sendType;if("forgetPwd"===$scope.sendType)$scope.$http.promise("/common/verifyCode/send?type=forgetpwd&captcha=slide",{"UserModel[mob]":$('input[name="UserModel[mob]"]').val(),valideCode:e},"post").done(function(e){$scope.countTime("#btnVerifyCode",$scope.waitTime),$("#btnSubmit").removeAttr("disabled")},function(e){var o=e.error;for(var i in o){var t="UserModel["+i+"]",a='<label class="error_tip error" id="'+t+'">'+o[i]+"</label>";if("valideCode"===i)return BootstrapDialog.show({title:"提示",message:o[i]}),!1;0<$("#"+i).length?$("#"+i).after(a):$('input[name="'+t+'"]',$('form[name="UserModel"]').eq(0)).after(a)}});else{if(!$scope.phoneData)return!1;$scope.phoneData.valideCode=e,$.ajax({type:"POST",dataType:"json",url:"/common/verifyCode/send2?type="+n+"&captcha=slide",data:$scope.phoneData,success:function(e){var o="register"===n?".getRegisterCode":".getloginCode",i=$("register"===n?".register-valid-tip":".login-valid-tip"),t="register"===n?".register-pass-tip":".toManyApply";if("00000"===e.code)$scope.countTime(o,$scope.waitTime),"register"===n&&$(".registered-tip").hide();else if("10000"===e.code){var a=e.error;a.mob&&(i.hide(),"register"===n?$(".registered-tip").html(a.mob).show():$(".login-img-tip").text(a.mob).show()),a.valideCode&&BootstrapDialog.show({title:"提示",message:a.valideCode}),a.verifyCode&&$dialog1.find(t).text(a.verifyCode).show()}},error:function(){}})}},btnRegister1=function(){if(!$scope.registerFlag1)return!1;var e=$dialog1.find(".register-phone").val();if(!reg.test(e))return $dialog1.find(".register-valid-tip").show(),!1;var o=$dialog1.find(".registerValidCode").val();if(0==o.length)return!1;$scope.registerFlag1=!1;var i={mob:e,verifyCode:o};return $.ajax({type:"POST",dataType:"json",url:"/user/register/doRegister2",data:i,success:function(e){if("00000"===e.code)$dialog1.find(".register-apply").hide(),$dialog1.find(".register-message").show(),$dialog1.find(".register-pass-tip").hide();else if("10000"===e.code)for(var o in e.error)$dialog1.find(".register-pass-tip").text(e.error[o]).show();$scope.registerFlag1=!0},error:function(){$scope.registerFlag1=!0}}),!1},showNicknameTip=function(){var e=$dialog1.find(".set-nickname").val(),o="";if(0==e.length||16<e.length)return o=0==e.length?"请填写昵称":"昵称长度不能超过16个字",$dialog1.find(".set-nickname-tip").html(o).show(),!1;$dialog1.find(".set-nickname-tip").hide()},showSetPwdTip=function(){var e=$dialog1.find(".set-pwd").val(),o=$dialog1.find(".set-pwd-tip");if(!pwdReg.test(e))return o.show(),!1;o.hide()},btnRegister2=function(){if(!$scope.registerFlag2)return!1;var e=$dialog1.find(".set-pwd").val(),o=$dialog1.find(".set-nickname").val(),i={pwd:e,alias:o},t="";return $dialog1.find(".set-nickname-tip").hide(),$dialog1.find(".set-pwd-tip").hide(),pwdReg.test(e)?0==o.length||16<o.length?(t=0==o.length?"请填写昵称":"昵称长度不能超过16个字",$dialog1.find(".set-nickname-tip").html(t).show()):($scope.registerFlag2=!1,$.ajax({type:"POST",dataType:"json",url:"/user/register/doRegister3",data:i,success:function(e){if("00000"===e.code)return window.jqLog&&window.jqLog.setRegister(i.alias),$.get("/user/register/checkCount",{alias:i.alias}),"/"===location.pathname?window.location.href="/view/user/floor":$scope.loginCallback($scope.$this),$scope.curDialog.close(),!1;e.error&&$dialog1.find(".set-nickname-tip").text(e.error.alias).show(),$scope.registerFlag2=!0},error:function(){$scope.registerFlag2=!0}})):$dialog1.find(".set-pwd-tip").show(),!1},Cy={alert:(fb=function(e){BootstrapDialog&&BootstrapDialog.show({title:"提示",btnOKLabel:"确认",message:e})},gb.toString=function(){return fb.toString()},gb),ajax:function(e,i){i.type||(i.type="post"),i.dataType||(i.dataType="json"),"object"==_typeof(i.data)?i.data.ajax=1:i.data+="&ajax=1",0<e.indexOf("?")?e+="&ajax=1":e+="?ajax=1",i.loading&&$(".shadow").css("display","block"),void 0===i.async&&(i.async=!0),void 0===i.timeout&&(i.timeout=6e4),$.ajax({url:e,type:i.type,timeout:i.timeout,dataType:i.dataType,async:i.async,data:i.data,error:function(e){i.fail&&i.fail(e)},success:function(e){i.loading&&$(".shadow").css("display","none"),2==e.status?i.fail?i.fail(e):Cy.alert&&Cy.alert(e.msg):e.redirect?location.href=e.redirect:i.success(e)},complete:function(e,o){i.fail&&"success"!=o&&"error"!=o&&i.fail(o)}})}},fb;function gb(e){return fb.apply(this,arguments)}var onGetUserInfo=function(){$.get("/user/index/isLogin",function(e){if("00000"===(e=JSON.parse(e)).code){e.data.isLogin&&(window.loginStatus=!0);var o=window.captcharData||{};o.method=submitValidCode,$scope.validCode($node,o).init()}})},onShowDialogHome=function(e){$scope.$this=$(this),$scope.loginCallback=e.data.callback,window.loginStatus?callback_refreshWindow_home():isMobile()?location.href="/user/login/index":showDialog()},onShowDialog=function(e){var o=$(this).attr("data-register");if(isMobile())$(this).hasClass("show-dialog-register")&&(o=!0),window.loginStatus?($scope.$this=$(this),e.data.callback()):location.href=o?"/user/login/index?applyFlag="+o:"/user/login/index";else{$scope.$this=$(this),$scope.loginCallback=e.data.callback;var i=e.data.type;$(this).hasClass("show-dialog-register")&&(tabItem=!1),!$(this).hasClass("show-dialog-login")&&"login"!==i||(tabItem=!0),window.loginStatus?$scope.loginCallback($scope.$this):showDialog()}},moreIndex=1,moreData=[],callback_LoadMore=function(){moreIndex+=1,$(".celue_item").each(function(e,o){var i=$(o).attr("postId_backtestId");moreData.push(i)});var e=moreData.join(","),o="/default/index/getBacktestList?page="+moreIndex+"&isAjax=1";$.ajax({type:"POST",dataType:"json",url:o,data:{ids:e},success:function(e){$(".celue_box").append(e.data.html),isMobile()&&e.data.count<6?$("#more_item").addClass("hidden"):!isMobile()&&e.data.count<6&&$("#more_item").addClass("hidden")},error:function(){}})},wechatDialog=null,checkBindStatusEnable=!0;function checkBindStatus(timestamp){checkBindStatusEnable&&$.get("/user/wechat/bindStatus?wechatId=1",function(res,status){if(res=eval("("+res+")"),"ok"==res.data.bindState){if(void 0!==timestamp&&res.data.subTime<timestamp)return void setTimeout("checkBindStatus("+timestamp+")",1e3);setTimeout("wechatDialog.close()",2e3),setTimeout(function(){addWechatSub()},2001)}else setTimeout("checkBindStatus()",2e3)})}function bindWechat(e,o){var i;i=o?'<p class="message-check tcenter"><img style="width:25px;height:25px" src="'+g_staticHost+'/algorithm/img/chenggong.png" alt=""></p><p class="tcenter mt_20">'+o+"</p>":"",BootstrapDialog.show({title:"策略订阅-微信绑定",onshown:function(e){wechatDialog=e},onhidden:function(e){checkBindStatusEnable=!1},message:'<div id="wechat-body">'+i+'<p class="tcenter mb_20"><img src="'+e+'" alt="" style="width:150px;height:150px;"></p><p class="tcenter">微信扫一扫，通过微信接收该策略的下单信号</p></div>'}),checkBindStatus(Date.parse(new Date)/1e3)}function addWechatSub(o,i){o=o||"",Cy.ajax("/algorithm/live/SetWechatSub?action=add&backtestId="+i,{success:function(e){"nobind"==e.data.result&&bindWechat(e.data.qrCode,o),$('.freeOrder[_backtestId="'+i+'"]').html("已订阅")},fail:function(e){BootstrapDialog.alert("")}})}var subLive=function(o,i,e){Cy.ajax("/algorithm/live/SubLive?backtestId="+o,{success:function(e){1==e.data.isNew&&($(".subscribeCount").html(i+1),addWechatSub("恭喜您，订阅成功。",o))},fail:function(e){Cy.alert("订阅失败:"+e.msg)}})},callback_freeOrder=function(){var e=$scope.$this.attr("_backtestId"),o=$scope.$this.attr("_postId"),i=parseInt($scope.$this.prev("span").find(".subscribeCount").html());subLive(e,i,o)},callback_getCode=function(){var e="/algorithm/index/clone?backtestId="+$scope.$this.attr("_backtestId")+"&postId="+$scope.$this.attr("_postId");window.open(e)},callback_checkDetail=function(){var e=$scope.$this.attr("urlhref");window.open(e)},callback_cloneStrategy=function(){var e="/algorithm/index/clone?backtestId=",o=$(".clone_backtestId").val(),i=$(".clone_postId").val();e+=o,i&&(e+="&postId=",e+=i),window.location.href=e},callback_strategyLogin=function(){window.location.href="/algorithm/live/shoplist"},callback_shareFunction=function(){window.location.href="/algorithm/apishare/editCode"},callback_refreshWindow=function(){0<window.location.href.indexOf("user/login/index")?(window.location.origin||(window.location.origin=window.location.protocol+"//"+window.location.hostname+(window.location.port?":"+window.location.port:"")),window.location.href=window.location.origin):window.location.reload()},callback_refreshWindow_home=function(){window.loginStatus?callback_LoadMore():callback_refreshWindow()},callback_factorAnalize=function(){exports.factorAnaly()},callback_huice=function(){window.newHuice()},showDialog=function(){dialogFlag=!0,setTimeout(function(){dialogFlag=!1},500),$scope.curDialog=$scope.dialog.createDialog({type:"type-default",width:"460px",height:"500px",marginTop:"50px",isHideHeader:!0,isHideFooter:!0,size:"size-large",closable:!0,clearPadding:!0,domHtml:domHtml}),$scope.curDialog.$modal.on("hide.bs.modal",function(){if(dialogFlag)return!1}),($dialog1=$scope.curDialog.$modal).find(".tab-nav").find("li").removeClass("active"),($appDialog=$dialog1).delegate(".tab-nav li","click",tabLoginContent),$appDialog.delegate(".to-validate","click",toValidLogin),$appDialog.delegate(".to-password","click",toPwdLogin),$appDialog.delegate(".goto-login","click",gotoLoginNow),$appDialog.delegate(".phone","blur",phoneBlur),$appDialog.delegate(".valideCode-img","click",getNewImgCode),$appDialog.delegate(".getloginCode","click",getLoginValidCode),$appDialog.delegate(".btnPwdSubmit","click",btnPwdLogin),$appDialog.delegate(".btnValidSubmit","click",btnVlidLogin),$appDialog.delegate(".getRegisterCode","click",getRegisterValidCode),$appDialog.delegate(".btn-register","click",btnRegister1),$appDialog.delegate(".set-nickname","blur",showNicknameTip),$appDialog.delegate(".set-pwd","blur",showSetPwdTip),$appDialog.delegate(".btn-finish","click",btnRegister2),$appDialog.delegate(".jq-login__password","focus",passwordBlur),$appDialog.delegate(".pwd-phone","keyup",cleanTips),$appDialog.delegate(".jq-login__password","keyup",cleanTips),tabItem?$dialog1.find(".tab-nav").find("li").eq(1).addClass("active").click():$dialog1.find(".tab-nav").find("li").eq(0).addClass("active").click(),tabItem=!0};function cleanTips(){$dialog1.find(".password-login .login-tip1").text("")}var followUser=function(e,o){$.get(api.followUser,{bId:e}).then(function(e){"00000"===(e=JSON.parse(e)).code?o&&o(e):"10001"===e.code&&($scope.loginCallback=function(){var e=parent.location.href;parent.location.href="/user/login/index?redirect="+encodeURIComponent(e)},onShowDialog())})},unFollowUser=function(e,o){$.get(api.unFollowUser,{bId:e}).then(function(e){"00000"===(e=JSON.parse(e)).code?o&&o(e):"10001"===e.code&&($scope.loginCallback=function(){var e=parent.location.href;parent.location.href="/user/login/index?redirect="+encodeURIComponent(e)},onShowDialog())})},toggleFollowUser=function(o){if($scope.toggleFollowUserFlag)return!1;$scope.toggleFollowUserFlag=!0;var i=$scope.$this;o="boolean"!=typeof o||o;var e=i.attr("data-state"),t=i.attr("data-follow-id");switch(e){case"1":followUser(t,function(e){followCallback(i,e,o)});break;case"2":unFollowUser(t,function(e){followCallback(i,e,o)});break;case"3":followUser(t,function(e){followCallback(i,e,o)});break;case"4":unFollowUser(t,function(e){followCallback(i,e,o)})}},loadComponents=function(){$=require("jquery"),$scope.$render=require("@util/render.component")(),$scope.$http=require("@util/http.component")(),$scope.validCode=require("@component/validCode/validCode.component"),$scope.dialog={createDialog:createDialog};require("./index.component.html");$scope.indexTpl=require("./index.component.html")},parseDOM=function(){$node=$(node)},wechatLogin=function(){var e=$(this).attr("data-type");$scope.$http.promise("/user/login/wxlogin",{type:e}).done(function(e){window.location.href=e.redirect})},callback_follow_detail=function(){if(window.loginStatus){toggleFollowUser(!1)}else window.location.href=window.location.pathname+"?tab=btn-follow"},callback_follow=function(){window.loginStatus?toggleFollowUser():callback_refreshWindow()},bindListener=function(){$node.delegate("#more_item","click",{callback:callback_refreshWindow},onShowDialogHome),$node.delegate(".freeOrder","click",{callback:callback_freeOrder},onShowDialog),$node.delegate(".getCode","click",{callback:callback_getCode,type:"login"},onShowDialog),$node.delegate(".linkToChicang","click",{callback:callback_checkDetail},onShowDialog),$node.delegate(".login_click","click",{callback:callback_refreshWindow},onShowDialog),$node.delegate(".toShareFunction","click",{callback:callback_shareFunction},onShowDialog),$node.delegate(".js-jq-other-user-follow-btn","click",{callback:callback_follow},onShowDialog),$node.delegate(".js-jq-follow-btn","click",{callback:callback_follow_detail},onShowDialog),$node.delegate(".free_register_now","click",{callback:callback_refreshWindow},onShowDialog),$node.delegate(".show-dialog-login","click",{callback:callback_refreshWindow},onShowDialog),$node.delegate(".show-dialog-register","click",{callback:callback_refreshWindow},onShowDialog),$node.delegate("#factorAnaly-button","click",{callback:callback_factorAnalize},onShowDialog),$node.delegate(".bigBtnText","click",{callback:callback_refreshWindow},onShowDialog),$node.delegate(".white_on_white","click",{callback:callback_refreshWindow},onShowDialog),$node.delegate("#daily-new-backtest-button","click",{callback:callback_huice},onShowDialog),$node.delegate(".js-jq-login-wechat","click",wechatLogin),$("#btnVerifyCode").click(function(){"true"!==$(this).attr("isCounting")&&($scope.sendType="forgetPwd",$scope.validCode($node,window.captcharData).getCaptchar())})},initPlugins=function(){onGetUserInfo()},init=function(){loadComponents(),parseDOM(),bindListener(),initPlugins()};return{init:init}};module.exports=indexComponent},{"./index.component.html":1,"@component/validCode/validCode.component":void 0,"@util/http.component":void 0,"@util/render.component":void 0,jquery:"jquery"}],3:[function(e,o,i){e("./index.component")(window,document.body).init()},{"./index.component":2}]},{},[3]);