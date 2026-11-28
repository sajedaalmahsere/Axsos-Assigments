
<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core"%>
<%@ taglib prefix="form" uri="http://www.springframework.org/tags/form"%>
<%@ page isErrorPage="true" %>

<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Burbank Location Ninjas</title>
    <script src="https://cdn.tailwindcss.com"></script>
</head>

<body class="bg-gray-100 min-h-screen py-12 px-4">

    <div class="max-w-4xl mx-auto bg-white p-8 rounded-xl shadow-lg">

        <h1 class="text-3xl font-bold text-gray-800 mb-8 text-center">
            Burbank Location Ninjas
        </h1>

        <div class="overflow-x-auto">
            <table class="w-full text-left border-collapse">

                <thead>
                    <tr class="bg-indigo-600 text-white">
                        <th class="px-6 py-4 rounded-tl-lg">First Name</th>
                        <th class="px-6 py-4">Last Name</th>
                        <th class="px-6 py-4 rounded-tr-lg">Age</th>
                    </tr>
                </thead>

                <tbody>
                    <c:forEach var="ninja" items="${ninja}">
                        <tr class="border-b border-gray-200 hover:bg-indigo-50 transition duration-200">

                            <td class="px-6 py-4 text-gray-700">
                                <c:out value="${ninja.firstName}"/>
                            </td>

                            <td class="px-6 py-4 text-gray-700">
                                <c:out value="${ninja.lastName}"/>
                            </td>

                            <td class="px-6 py-4 text-gray-700">
                                <c:out value="${ninja.age}"/>
                            </td>

                        </tr>
                    </c:forEach>
                </tbody>

            </table>
        </div>

        <div class="mt-6 text-center">
            <a href="/ninja"
               class="inline-block bg-indigo-600 hover:bg-indigo-700 text-white font-semibold px-6 py-3 rounded-lg transition duration-200">
                Add New Ninja
            </a>
        </div>

    </div>

</body>
</html>
