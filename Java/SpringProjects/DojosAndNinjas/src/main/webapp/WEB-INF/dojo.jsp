
<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core"%>
<%@ taglib prefix="form" uri="http://www.springframework.org/tags/form"%>
<%@ page isErrorPage="true" %>

<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>New Dojo</title>
    <script src="https://cdn.tailwindcss.com"></script>
</head>

<body class="bg-gray-100 min-h-screen flex items-center justify-center">

    <div class="bg-white w-full max-w-md p-8 rounded-xl shadow-lg">

        <h1 class="text-3xl font-bold text-gray-800 mb-6 text-center">
            New Dojo
        </h1>

        <form:form action="/add/dojo" method="post" modelAttribute="dojo"
            cssClass="space-y-5">

            <div>
                <form:label path="name"
                    cssClass="block text-sm font-semibold text-gray-700 mb-2">
                    Name:
                </form:label>

                <form:input path="name"
                    cssClass="w-full px-4 py-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:border-indigo-500"/>

                <form:errors path="name"
                    cssClass="text-red-500 text-sm mt-1 block"/>
            </div>

            <input type="submit" value="Create"
                class="w-full bg-indigo-600 hover:bg-indigo-700 text-white font-semibold py-3 rounded-lg cursor-pointer transition duration-200"/>

        </form:form>

        <div class="mt-6 text-center">
            <a href="/ninja"
                class="text-indigo-600 hover:text-indigo-800 font-medium underline">
                Add Ninja
            </a>
        </div>

    </div>

</body>
</html>
