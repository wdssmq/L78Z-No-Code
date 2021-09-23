<%@ LANGUAGE="VBSCRIPT" CODEPAGE="65001"%>
<% Option Explicit %>
<% 'On Error Resume Next %>
<% Response.Charset="UTF-8" %>
<!-- #include file="..\..\c_option.asp" -->
<!-- #include file="..\..\..\zb_system\function\c_function.asp" -->
<!-- #include file="..\..\..\zb_system\function\c_system_lib.asp" -->
<!-- #include file="..\..\..\zb_system\function\c_system_base.asp" -->
<!-- #include file="..\..\..\zb_system\function\c_system_event.asp" -->
<!-- #include file="..\..\..\zb_system\function\c_system_manage.asp" -->
<!-- #include file="..\..\..\zb_system\function\c_system_plugin.asp" -->
<!-- #include file="..\p_config.asp" -->
<%
Server.ScriptTimeout=999
%>
<%
Call System_Initialize()
'检查非法链接
Call CheckReference("")
'检查权限
If BlogUser.Level>1 Then Call ShowError(6)
If CheckPluginState("fixCommet")=False Then Call ShowError(48)
BlogTitle="多说评论导入"
Dim act:act = Request.QueryString("act")
Dim ves
If act="run" Then
  For ves = 1 to 17
    Call AddBatch("评论导入","Call fix_JSON(""" & BlogPath & "zb_users\PLUGIN\fixCommet\json\"&ves&".json" & """)")
  Next
  Call SetBlogHint(True,Empty,Empty)
  Response.Redirect "main.asp"
End If




%>
<!--#include file="..\..\..\zb_system\admin\admin_header.asp"-->
<!--#include file="..\..\..\zb_system\admin\admin_top.asp"-->
<div id="divMain">
  <div id="ShowBlogHint">
    <%Call GetBlogHint()%>
  </div>
  <div class="divHeader"><%=BlogTitle%></div>
  <div class="SubMenu"><%=fixCommet_SubMenu(0)%></div>
  <div id="divMain2"> 
    <%'fix_JSON(BlogPath & "zb_users\PLUGIN\fixCommet\json\3.json")%>
  </div>
</div>
<!--#include file="..\..\..\zb_system\admin\admin_footer.asp"-->

<%Call System_Terminate()%>
