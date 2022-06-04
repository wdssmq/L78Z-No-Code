<%@LANGUAGE="VBSCRIPT" CODEPAGE="65001"%>
<% Option Explicit %>
<% Response.CodePage=65001%>
<% Response.Charset="UTF-8" %>
<% On Error Resume Next %>
<%
'******************************************************
''作者：沉冰浮水
''微博：http://t.qq.com/wdssmq
'******************************************************
Const apiKey="" '填入你的 Key 和密钥
Const secretKey="" 'App Secret
Dim callBack
callBack="http://"&request.ServerVariables("HTTP_HOST")&Replace(request.ServerVariables("SCRIPT_NAME"),"index.asp","callback.asp") '返回地址

' http://test.wdssmq.com/qqsns/callback.asp

Const OpenID=""
Const access_token=""
Const expires_in=""
Const refresh_token=""


Class OAuth
Private oDic,aKeys,access_token,TimeLine,boundary
'初始化通用参数
Private Sub Class_Initialize
	TimeLine= DateDiff("s","01/01/1970 08:00:00",Now()) 'oauth_timestamp
	boundary="------------------"&TimeLine
	Set oDic = Server.CreateObject("Scripting.Dictionary")
End Sub
'销毁对象
Private Sub Class_Terminate()
	Set oDic = Nothing
End Sub

Function getAuthorizeURL()
	Dim url,method
	url="https://graph.qq.com/oauth2.0/authorize"
	method="GET"
	oDic.Add "client_id",apiKey
	oDic.Add "response_type","code"
	oDic.Add "redirect_uri",callback
	oDic.Add "scope","add_t"
	getAuthorizeURL= url&"?"&Sorts
End Function

Sub getAccessToken (code)
	Dim url,method
	url="https://graph.qq.com/oauth2.0/token"
	method="GET"
	oDic.Add "client_id",apiKey
	oDic.Add "client_secret",secretKey
	oDic.Add "grant_type","authorization_code"
	oDic.Add "code",code
	oDic.Add "access_token",access_token
	oDic.Add "redirect_uri",callback
	Call setSession(doRequest(method,url,Sorts, null, false))
End Sub

Public Property Get haslog
  If Session("access_token")<>"" And Session("access_openid")<>"" Then
    haslog= True
  End If
End Property

Sub setSession(str)
	Dim ary1
	ary1 = Split(Replace(str,"=","&"),"&")
	If ubound(ary1) > 1 Then
		Session("access_token") = ary1(1)
		Session("expires_in") = ary1(3)
		Session("refresh_token") = ary1(5)
	End If
End Sub

'获取OpenID
Function getOpenID()
  Dim url,method,strRequest
  oDic.Add "access_token",Session("access_token")
  oDic.Add "format","json"
  url="https://graph.qq.com/oauth2.0/me"
  method="GET"
  strRequest=Replace(doRequest(method, url, Sorts, null, false)," );","")
  strRequest=Replace(strRequest,"callback( ","")
  Response.Write strRequest
  set getOpenID=toObject(strRequest)
End Function

Sub setToken()
	oDic.Add "oauth_consumer_key",apiKey
	oDic.Add "access_token",Session("access_token")
	'oDic.Add "clientip",Request.ServerVariables("remote_addr")
	oDic.Add "oauth_version","2.a"
  oDic.Add "openid",Session("access_openid")
End Sub

'获取用户信息
Function getUserInfo()
Dim url,method
Call setToken
url="https://graph.qq.com/user/get_user_info"
method="GET"
set getUserInfo=toObject(doRequest(method, url, Sorts, null, false))
End Function

'发送微博
Function Postwb(con,ip)
Dim url,method
Call setToken
method="POST"
oDic.Add "content",con
oDic.Add "format","json"
oDic.Add "clientip",ip
url="https://graph.qq.com/t/add_t"
set Postwb=toObject(doRequest(method, url, "", Sorts, false))
End Function

'发送数据
Function doRequest(verb, resLoc, getData, objData, multi)
	Dim aUrl,xmlhttp
	If(getData <>"") then getData = "?"&getData
	aUrl = resLoc & getData
	Response.write aUrl & "<br>"
	Set xmlhttp=Server.CreateObject("MSXML2.ServerXMLHTTP")
	xmlhttp.Open verb,aUrl,false
	If(verb = "POST") Then
		If(multi) Then '如果是图片
			xmlhttp.setRequestHeader "Content-Type","multipart/form-data; boundary="&boundary
			'图片上传处理
		Else
			xmlhttp.setRequestHeader "Content-Type", "application/x-www-form-urlencoded; charset=utf-8"
		End  If
	End  If
	xmlhttp.send(objData)
	doRequest=xmlhttp.responseText
	Response.Write("测试信息，可注释: " & Replace(Replace(doRequest,"<","&lt;"),">","&gt;") & "<br><br>一个在线格式化JSON数据的工具：http://jsonformatter.curiousconcept.com/<br><br>")
	Set xmlhttp=Nothing
End Function

Sub refreshToken ()
	Dim url,method
	oDic.Add "client_id",apiKey
	oDic.Add "grant_type","refresh_token"
	oDic.Add "refresh_token",Session("refresh_token")
  oDic.Add "format","json"
	url="https://open.t.qq.com/cgi-bin/oauth2/access_token"
	method="GET"
	Call setSession(doRequest(method,url,Sorts, null, false))
End Sub

Function Sorts()
	Dim i,arr(),aKeys,aItems
	ReDim arr(oDic.Count-1)
	aKeys = oDic.Keys
	aItems = oDic.Items
	For i=0 To oDic.Count-1
	arr(i)=aKeys(i)&"="&strUrlEnCode(oDic.Item(aKeys(i)))
	Next
	Sorts=join(arr,"&")
End Function

'URL Encode，并将不需要转换的再替换回来
Function strUrlEnCode(byVal strUrl)
	strUrlEnCode = Server.URLEncode(strUrl)
	strUrlEnCode = Replace(strUrlEnCode,"%5F","_")
	strUrlEnCode = Replace(strUrlEnCode,"%2E",".")
	strUrlEnCode = Replace(strUrlEnCode,"%2D","-")
	strUrlEnCode = Replace(strUrlEnCode,"+","%20")
End Function

End Class
%>
