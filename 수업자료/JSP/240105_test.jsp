<%@ page language="java" contentType="text/html; charset=EUC-KR"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
    <title>multiplicationTables</title>
    <style>
        .table {
            display: flex;
            flex-wrap: wrap;
            max-width: 346px;
            margin: 5px;
            font-weight: bolder;
            border: 1px solid #000;
        }
        .cell {
            width: 30px;
            height: 30px;
            border: 1px solid #000;
            margin: 3px;
            text-align: center;
            line-height: 30px;
        }
    </style>
</head>
<body>
      <!--Q.구구단 표-->
	<!-- 내가 한 풀이 (table 태그 쓰지말라는 줄...) -->
    <div class="table">
        <% for (int i = 1; i <= 9; i++) { %>
            <% for (int j = 1; j <= 9; j++) { %>
            	<% if(i==1&&j==1){ %>
                	<div class="cell">X</div>
                <% }else{%>
                	<div class="cell"><%= i * j %></div>
                <% } %>
            <% } %>
        <% } %>
    </div>
    
    <!-- 아래는 강사님 풀이 -->
    <table border="1">
    	<% String arr[]={"X","2","3","4","5","6","7","8","9"};%>
    	<tr>
    		<%for(int i=0;i<9;i++) {%>
    			<th><%=arr[i] %></th>
    		<%} %>
    	</tr>
    	<% for(int i=1;i<10;i++){ %>
    		<tr>
    		<% for(int j=1;j<10;j++){%>
    			<td><%=i*j %>
    		<%} %>
    		</tr>
    	<%} %>
    </table>
</body>
</html>
