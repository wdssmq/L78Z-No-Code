<!--#include file="oauth.asp"-->
<!--#include file="function.asp"-->
<%
Dim t : Set t = New OAuth
If Request("act")="getOpenID" Then
  Session("access_openid") = t.getOpenID().openid
Else
  Call t.getAccessToken (Request("code"))
End If
Set t = Nothing
if Session("access_token")<>"" and Request("act")="" Then
  Response.Redirect("callback.asp?act=getOpenID")
Else
  Response.Redirect("index.asp")
End If

%>
<a href="index.asp">index.asp</a>