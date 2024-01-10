//과제  : 학번,이름,나이,학년,전공
//ex   >>  1, lee, 25, 1, 컴공
//형태로 자바빈을 이용해 jsp로 출력하라.
package com.javalex.ex;

import java.sql.Statement;
import java.sql.*;
import java.util.*;

public class studentDAO {
	private String url="jdbc:mysql://localhost:3306/apidb";
	private String id="root";
	private String passwd="1234";
	
	private Connection conn= null;
	private Statement st=null;
	private ResultSet rs = null;
	
	public studentDAO() {
		try {
			Class.forName("com.mysql.jdbc.Driver");
		}
		catch(Exception error){
			System.out.println(error.toString());
		}
	}
	
	public ArrayList<String> showAllStudent() {
		//메소드 반환값으로 할 연결리스트선언
		ArrayList<String> result = new ArrayList<String>();
		//DB랑 접속
		try {
			conn=DriverManager.getConnection(url, id, passwd);
			st = conn.createStatement();
			String query="SELECT * FROM student";
			rs = st.executeQuery(query);
			result.add("학번,이름,나이,학년,전공");
			while(rs.next()) {
				int hakbun=rs.getInt("hakbun");
				String name=rs.getString("name");
				int age =rs.getInt("age");
				int grade=rs.getInt("grade");
				String major=rs.getString("major");
				
				String row = String.format("%d, %s, %d, %d, %s",hakbun, name, age, grade, major);
				
				result.add(row);
			}
		}
		catch(Exception error){
			System.out.println(error.toString());
		}
		//DB 정보들을 result에 하나씩 담아놓기
		
		return result;
	}
}
// https://github.com/mulbom/Port/blob/main/수업자료/JSP/240110_class2.jsp
