<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<%@ taglib prefix="c" uri="jakarta.tags.core" %>
<!DOCTYPE html>
<html>
<head>
	<meta charset="UTF-8">
	<title>Fit Quest</title>
	<link rel="stylesheet" href="/css/style.css">
</head>
<body>
	<h1>Fit Quest</h1>
	<h2>Your Fitness Points: <c:out value="${points}"/></h2>

	<div class="activities">
		<div class="card">
			<h3>Walk</h3>
			<p>(earns 5 to 10 points)</p>
			<form action="/process" method="post">
				<input type="hidden" name="activity" value="walk">
				<button type="submit">Go for a Walk</button>
			</form>
		</div>

		<div class="card">
			<h3>Yoga</h3>
			<p>(earns 10 to 20 points)</p>
			<form action="/process" method="post">
				<input type="hidden" name="activity" value="yoga">
				<button type="submit">Do Yoga</button>
			</form>
		</div>

		<div class="card">
			<h3>Weights</h3>
			<p>(earns 15 to 30 points)</p>
			<form action="/process" method="post">
				<input type="hidden" name="activity" value="weights">
				<button type="submit">Lift Weights</button>
			</form>
		</div>

		<div class="card">
			<h3>Daily Challenge</h3>
			<p>(earns or loses up to 50 points)</p>
			<form action="/process" method="post">
				<input type="hidden" name="activity" value="challenge">
				<button type="submit">Take the Challenge</button>
			</form>
		</div>
	</div>

	<h3>Activity Log</h3>
	<div class="log">
		<c:forEach var="entry" items="${log}">
			<c:choose>
				<c:when test="${entry.contains('lost')}">
					<p class="lost"><c:out value="${entry}"/></p>
				</c:when>
				<c:otherwise>
					<p class="earned"><c:out value="${entry}"/></p>
				</c:otherwise>
			</c:choose>
		</c:forEach>
	</div>
</body>
</html>
