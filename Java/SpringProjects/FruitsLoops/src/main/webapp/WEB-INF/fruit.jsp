<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
<script src="https://cdn.jsdelivr.net/npm/@tailwindcss/browser@4"></script>
</head>
<body class="bg-gray-100 min-h-screen">

    <div class="max-w-3xl mx-auto px-6 py-12">

        <!-- Header -->
        <div class="text-center mb-10">
            <h1 class="text-4xl font-bold text-green-700 mb-3">
                🍓 Fruit Store
            </h1>
            <p class="text-gray-500 text-lg">
                Fresh fruits and their prices
            </p>
        </div>

        <!-- Fruit Table -->
        <div class="bg-white rounded-xl shadow-lg overflow-hidden">

            <table class="w-full text-left">

                <thead class="bg-green-600 text-white">
                    <tr>
                        <th class="px-6 py-4 font-semibold">Fruit Name</th>
                        <th class="px-6 py-4 font-semibold">Price</th>
                    </tr>
                </thead>

                <tbody class="divide-y divide-gray-200">

                    <c:forEach var="thisItem" items="${fruits}">
                        <tr class="hover:bg-green-50 transition duration-200">

                            <td class="px-6 py-4 font-medium text-gray-800">
                                ${thisItem.name}
                            </td>

                            <td class="px-6 py-4 text-green-700 font-semibold">
                                $${thisItem.price}
                            </td>

                        </tr>
                    </c:forEach>
                     
                     <c:if test="${!thisItem.name.startsWith('G')}">
        					<p>${thisItem.name} - $${thisItem.price} </p>
    				</c:if>

                </tbody>

            </table>

        </div>

        <!-- Footer -->
        <p class="text-center text-gray-400 text-sm mt-8">
            Freshness in every bite! 🍍
        </p>

    </div>

</body>
</html>