<!--#include file="oauth.asp"-->
<!--#include file="function.asp"-->
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<title>QQ互联SDK For Asp</title>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<meta name="Keywords" content="QQ互联,QQ登陆,腾讯API">
<meta name="description" content="基于ASP的腾讯QQ互联API接入，SDK">
<meta name="author" content="沉冰浮水" />  
<style>
*{ font-size:14px; margin:0; padding:0}
body{ margin:20px;line-height:22px;}
</style>
</head>
<body>
<%
Randomize

If access_token <> "" Then 
	Session("access_token") = access_token
End If
Dim t,have_login
If Session("access_token") = "" Or Request.QueryString("act") = "logout"Then
	Set t = New OAuth
	Dim get_authorize_url
	Session("access_token") = ""
	get_authorize_url = t.getAuthorizeURL()
	Response.Write "<a href=""" & get_authorize_url & """>使用QQ登陆</a>"
	have_login = False
	Set t = Nothing
Else
	have_login = true
	get_authorize_url = "index.asp?act=logout"
	Response.Write "<a href=""" & get_authorize_url & """>注销</a>"
End If
' Response.Write "　<a href=""index.asp"">刷新</a> <a href=""javascript:void(0)"" onclick=""return follow();"">收听沉冰浮水(@wdssmq)</a><span id=""status""></span><br />"
Response.Write "　<a href=""index.asp"">刷新</a> <a href=""https://jq.qq.com/?_wv=1027&k=57UACAn""><img border=""0"" src=""https://pub.idqqimg.com/wpa/images/group.png""></a><span id=""status""></span><br />"

If have_login Then
	Response.Write "access_token : "&Session("access_token")&"<br />"
	Response.Write "openid : "&Session("access_openid")&"<br />"
	Response.Write "有效期 ： "&Session("expires_in")&"<br />"
	Response.Write "refresh_token : "&Session("refresh_token")&"<br />"
	Response.Write "以上值按需写入oauth.asp或者数据库<br />"

%>
<h4>发布微博</h4>
<form action="index.asp?act=post" method="post">
内容：<input name="txt" id="txt" type="text" size="50" maxlength="140" value="微博API测试<%=int(Rnd()*1000)%>" />
<br />
图片：<input name="picurl" id="picurl" type="text" value="http://www.wdssmq.com/logos/qun.jpg" size="70" />
<br />
<!--<input type="file" name="picfile" id="picfile" />-->
<br>
<input name="userip" id="userip" type="hidden" value="" />
<script type="text/javascript" src="http://pv.sohu.com/cityjson?ie=utf-8"></script>
<script type="text/javascript">
<!--
document.getElementById('userip').value = returnCitySN["cip"];
//-->
</script>
<input name="submit" type="submit" value="提交" /> <a href="javascript:void(0)" onclick="return postwb(document.getElementById('txt').value,document.getElementById('picurl').value);">OpenJS发送</a>
</form>
<%
	Select Case Request.QueryString("act")
	Case "post"
		Dim txt,picurl,userip
		txt=request("txt")
		picurl=request("picurl")
		userip=request("userip")
		If txt<>"" Then
			Set t = New OAuth
			Dim PostCode
			Set PostCode = t.Postwb(txt,userip)
			Response.Write "发送状态"&PostCode.msg & "地址：http://t.qq.com/p/t/"& PostCode.data.id
			Set t = Nothing
		End If
	Case Else
		Set t = New OAuth
		Dim UserInfo
		set UserInfo = t.getUserInfo()
		Response.Write "<h4>用户信息</h4>"
    Response.Write "<img src="""&UserInfo.figureurl_1&""" alt=""头像"" />" & "<br/>"
		Response.Write "昵称:"&UserInfo.nickname & "<br/>"
		Response.Write "所在地:"&UserInfo.province & UserInfo.city & "<br/>"
		'想要标签全部输出的话可以做个循环，从0到9，不为空就输出并且继续。。

		'toObject和getItem函数在sha1文件里，有关JSON的内容请自行搜索
	End Select
%>

<% End If %>
<script src="http://mat1.gtimg.com/app/openjs/openjs.js#debug=yes"></script>
<script>
    T.init({
        appkey: 801082401,
        pingback: false
    });

    if (T.loginStatus()) {
        T.task(T.api('friends/check', {
            names: 'wdssmq',
            flag: 1
        }), T.api('user/other_info', {
            name: 'wdssmq'
        })).success(function(ret0, ret1) {
            var stat = T.find("#status")[0];
            var isfollow = ret0[0].data.wdssmq;
            var fansnum = ret1[0].data.fansnum;
            stat.innerHTML = (isfollow ? "已收听": "未收听") + '，听众' + fansnum + '人';
            if (isfollow) stat.className = 'green';
        });
    }
    function postwb(con, pUrl) {
        if (!T.loginStatus()) {
            T.login();
			postwb(con,PicUrl);
            return;
        }
        T.api("t/add_pic_url", {
            content: con,
            pic_url: pUrl
        },
        'json', 'post').success(function() {
            alert('发送成功');
        }).error(function(code, message) {
            alert('发送失败' + message);
        });
        return false;
    }

    function follow() {
        if (!T.loginStatus()) {
			T.login(function (loginStatus) {
				follow();
			},function (loginError) {
				alert(loginError.message);
			});
            return;
        }
        T.api("friends/add", {
            name: 'wdssmq'
        },
        'json', 'post').success(function() {
            alert('收听成功');
        }).error(function(code, message) {
            alert('收听失败' + message);
        });
        return false;
    }
</script>


<p align="center" ><a href="http://www.wdssmq.com/">沉冰浮水</a> | <script type="text/javascript">var _bdhmProtocol = (("https:" == document.location.protocol) ? " https://" : " http://");document.write(unescape("%3Cscript src='" + _bdhmProtocol + "hm.baidu.com/h.js%3Fef14c312dc96b31bf4536edad5be6080' type='text/javascript'%3E%3C/script%3E"));</script></p>

</body>
</html>
