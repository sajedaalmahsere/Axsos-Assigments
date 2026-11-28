
<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core"%>
<%@ taglib prefix="form" uri="http://www.springframework.org/tags/form"%>
<%@ page isErrorPage="true" %>

<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>New Ninja</title>
    <script src="https://cdn.tailwindcss.com"></script>
</head>

<body class="bg-gray-100 min-h-screen flex items-center justify-center py-10">

    <div class="bg-white w-full max-w-lg p-8 rounded-xl shadow-lg">

        <h1 class="text-3xl font-bold text-gray-800 mb-8 text-center">
            New Ninja
        </h1>

        <form:form action="/ninja/add" method="post" modelAttribute="ninja"
            cssClass="space-y-5">

            <!-- First Name -->
            <div>
                <form:label path="firstName"
                    cssClass="block text-sm font-semibold text-gray-700 mb-2">
                    First Name:
                </form:label>

                <form:input path="firstName"
                    cssClass="w-full px-4 py-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-indigo-500"/>

                <form:errors path="firstName"
                    cssClass="text-red-500 text-sm mt-1 block"/>
            </div>

            <!-- Last Name -->
            <div>
                <form:label path="lastName"
                    cssClass="block text-sm font-semibold text-gray-700 mb-2">
                    Last Name:
                </form:label>

                <form:input path="lastName"
                    cssClass="w-full px-4 py-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-indigo-500"/>

                <form:errors path="lastName"
                    cssClass="text-red-500 text-sm mt-1 block"/>
            </div>

            <!-- Age -->
            <div>
                <form:label path="age"
                    cssClass="block text-sm font-semibold text-gray-700 mb-2">
                    Age:
                </form:label>

                <form:input path="age"
                    cssClass="w-full px-4 py-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-indigo-500"/>

                <form:errors path="age"
                    cssClass="text-red-500 text-sm mt-1 block"/>
            </div>

            <!-- Dojo Selection -->
            <div>
                <form:label path="dojo"
                    cssClass="block text-sm font-semibold text-gray-700 mb-2">
                    Select Dojo:
                </form:label>

                <form:select path="dojo"
                    cssClass="w-full px-4 py-3 border border-gray-300 rounded-lg bg-white focus:outline-none focus:ring-2 focus:ring-indigo-500">

                    <form:option value="">Select Dojo</form:option>

                    <c:forEach var="dojo" items="${dojos}">
                        <form:option value="${dojo.id}">
                            <c:out value="${dojo.name}"/>
                        </form:option>
                    </c:forEach>

                </form:select>

                <form:errors path="dojo"
                    cssClass="text-red-500 text-sm mt-1 block"/>
            </div>

            <!-- Submit Button -->
            <input type="submit" value="Create Ninja"
                class="w-full bg-indigo-600 hover:bg-indigo-700 text-white font-semibold py-3 rounded-lg cursor-pointer transition duration-200"/>

        </form:form>
        
        <div class="mt-6 pt-5 border-t border-gray-200 text-center">
    		<a href="/ninja/burbank"
       			class="text-indigo-600 hover:text-indigo-800 font-semibold transition duration-200">
        		View Burbank Ninjas →
   			 </a>
		</div>

    </div>

</body>
</html>
