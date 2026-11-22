<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
    
<%@ taglib prefix="fmt" uri="http://java.sun.com/jsp/jstl/fmt" %>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
<script src="/js/Date.js"></script>
</head>
<body>

	 <p>
        Current Date:
        <fmt:formatDate value="${date}" pattern="EEEE, MMMM dd, yyyy"/>
    </p>
	

</body>
</html>