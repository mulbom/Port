<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8" import="com.javalex.ex.studentDAO" import="java.util.ArrayList"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>
	<%
	studentDAO dao=new studentDAO();
	ArrayList<String> studentList = dao.showAllStudent(); %>
	<table border="1">
	<%try{ %>
		<%for(String sudent:studentList){ %>
			<tr><td><%=sudent%></td><tr>
			<%} %>
		<%} 
		catch
		(Exception error){
			System.out.println(error.toString());
		}%>
	</table>
</body>
</html>
