<script language="javascript" runat="server" >
  function ucode2str(str){
    str = unescape(str.replace(/\\u/g, "%u"));
    return str;
  }
</script>
<%
'****************************************
' fixCommet 子菜单
'****************************************
Function fixCommet_SubMenu(id)
	Dim aryName,aryPath,aryFloat,aryInNewWindow,i
	aryName=Array("首页","运行")
	aryPath=Array("main.asp","main.asp?act=run")
	aryFloat=Array("m-left","m-left")
	aryInNewWindow=Array(False,False)
	For i=0 To Ubound(aryName)
		fixCommet_SubMenu=fixCommet_SubMenu & MakeSubMenu(aryName(i),aryPath(i),aryFloat(i)&IIf(i=id," m-now",""),aryInNewWindow(i))
	Next
End Function

Function fix_Path(name,p)
  Dim MyPath
  MyPath = IIf(p = "url",BlogHost,BlogPath)
  MyPath = MyPath & "zb_users\PLUGIN\fixCommet\"
  Select Case name
    Case "dJSON"
      MyPath = MyPath & "json\"
    Case Else
      MyPath = MyPath & "ca\" & name & ".txt"
  End Select
  If p = "url" Then
    MyPath = Replace(MyPath,"\","/")
  End If
  fix_Path = MyPath
End Function


Function fix_JSON(file)
  Dim oJSON
  Set oJSON = New aspJSON
  oJSON.loadJSON(LoadFromFile(file,"utf-8"))

  Dim kev,i,oData,cmt
  i = 0
  set oData = oJSON.data("data")
  For Each kev In oData
    Set cmt = oData(kev)
    cmt.item("author_name") = trim(ucode2str(cmt("author_name")))
    cmt.item("message") = trim(ucode2str(cmt("message")))
    If fix_check(cmt) Then
      
    End If
  Next
  Session("batchtime")=Session("batchtime")+RunTime
End Function

Function fix_check(cmt)
    Dim objRS
    Set objRS=Server.CreateObject("ADODB.Recordset")
    objRS.CursorType = adOpenKeyset
    objRS.LockType = adLockReadOnly
    objRS.ActiveConnection=objConn
    objRS.Source=""
    Dim w,noMsg,dMsg
    noMsg = false
    w = " [comm_Author]='" & cmt("author_name") & "'"
    If cmt("parents") = "" Then
      If cmt("post_key") <> cmt("post_id") Then
        noMsg = true
        w = w & " AND [comm_ID]=" & cmt("post_key")
      Else
        w = w & " AND [comm_ParentID]=0"
      End If
    Else
      If PublicObjFSO.FileExists(fix_Path(cmt("parents"),"")) Then
        cmt.item("parents") = LoadFromFile(fix_Path(cmt("parents"),""),"utf-8")
        w = w & " AND [comm_ParentID]=" & cmt("parents")
      Else
        dMsg = cmt("author_name") & vbCrLf & cmt("message") & vbCrLf & cmt("author_url") & vbCrLf & cmt("parents") & vbCrLf & cmt("post_id")
        Call SaveToFile(fix_Path("#" & cmt("author_name"),""),dMsg,"utf-8",False)
        Exit Function
      End If
    End If
    If cmt("thread_key") = "" Then
      If noMsg = false Then w =  w & " AND [comm_ID]=" & cmt("post_key")
      noMsg = true
    Else
      w =  w & " AND [log_ID]=" & cmt("thread_key")
    End If
    If noMsg = false Then 
      w = w & " AND LTrim(RTrim([comm_Content]))='" & cmt("message") & "'"
    End If
    objRS.Open("SELECT * FROM [blog_Comment] WHERE" & w)
    If (Not objRS.bof) And (Not objRS.eof) Then
      fix_check = True
      Call SaveToFile(fix_Path(cmt("post_id"),""),objRS("comm_ID"),"utf-8",False)

      ' Do While Not objRS.eof
        ' If trim(objRS("comm_Content")) <> cmt("message") Then
          ' Response.Write w
          ' Response.Write "<br />"
          ' debug(objRS("comm_ID"))
          ' debug(objRS("comm_Author"))
          ' debug(objRS("comm_Content"))
          ' debug(cmt("message"))
          ' debug("-----")
        ' End If
        ' objRS.MoveNext
      ' Loop
    Else
      Response.Write w
      Response.Write "<br />"
      Response.Write cmt("thread_key")
      Response.Write "<br />"
      Response.Write cmt("post_id")
      Response.Write "<br />"
      Response.Write cmt("parents")
      Response.Write " <br />"
      Response.Write cmt("author_name")
      Response.Write "<br />"
      Response.Write cmt("message")
      Response.Write "<br />"
      Response.Write "----<br />"
      dMsg = cmt("author_name") & vbCrLf & cmt("message") & vbCrLf & cmt("author_url") & vbCrLf & cmt("parents") & vbCrLf & cmt("post_id")
      Call SaveToFile(fix_Path("_" & cmt("author_name"),""),dMsg,"utf-8",False)
      fix_check = fix_creat(cmt)
    End If
End Function

Function fix_creat(cmt)
  Dim objCMT
  Set objCMT = New TComment
  objCMT.IP = cmt("ip")
  objCMT.log_id = cmt("thread_key")
  objCMT.Author = cmt("author_name")
  If objCMT.Author = "沉冰浮水" Then
    objCMT.AuthorID = 1
  End If
  objCMT.EMail = cmt("author_email")
  If objCMT.EMail = "" Or Not CheckRegExp(objCMT.EMail, "[email]") Then
    objCMT.EMail = ""
  End If
  objCMT.HomePage = cmt("author_url")
  If objCMT.HomePage = "" Or Not CheckRegExp(objCMT.HomePage, "[homepage]") Then
    objCMT.HomePage = BlogHost
  End If
  objCMT.PostTime = cmt("created_at")
  objCMT.Content = cmt("message")
  If cmt("parents") <> "" Then
    Response.Write cmt("parents")
    Response.Write "<br />"
    objCMT.ParentID = CLng(cmt("parents"))
  End If
  ' objCMT.Agent = cmt.agent
  If objCMT.Post() Then
    Response.Write objCMT.ID
    Response.Write "<br />"
    Call SaveToFile(fix_Path(cmt("post_id"),""),objCMT.ID,"utf-8",False)
    fix_creat = True
  End If
  Response.Write "fix_creat<br />"
End Function

Function debug(str)
  Response.Write str
  Response.Write "<br />"
End Function
%>