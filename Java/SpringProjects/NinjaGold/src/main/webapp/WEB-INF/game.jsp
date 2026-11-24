
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>

<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Ninja Gold Game</title>
    <!-- Tailwind CSS -->
    <script src="https://cdn.tailwindcss.com"></script>
</head>
<body class="min-h-screen bg-slate-950 text-white">
    <div class="max-w-6xl mx-auto px-6 py-12">
        <!-- Header -->
        <header class="text-center mb-12">
            <h1 class="text-5xl font-extrabold text-yellow-400 mb-3">🥷 Ninja Gold</h1>
            <p class="text-slate-400 text-lg">
                Explore different places and collect gold!
            </p>
        </header>
        <!-- Gold Counter -->
        <div class="bg-slate-900 border border-yellow-500/30 rounded-2xl p-6 mb-10 text-center shadow-lg">
            <h4 class="text-slate-400 text-lg mb-2">
                Your Current Gold
            </h4>
            <p class="text-5xl font-bold text-yellow-400">${Gold} <span class="text-2xl">💰</span></p>
        </div>
        <!-- Locations -->
        <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6 mb-12">
            <!-- Farm -->
            <div class="bg-slate-900 rounded-2xl p-6 border border-slate-800 hover:border-green-500 transition duration-300 text-center">
                <div class="text-5xl mb-4">🌾</div>
                <h2 class="text-2xl font-bold mb-2">
                    Farm
                </h2>
                <p class="text-slate-400 mb-6">
                    Earn 10 - 20 gold
                </p>
                <form action="${pageContext.request.contextPath}/process" method="POST">
                    <input type="hidden" name="place" value="farm">
                    <button type="submit"
                        class="w-full bg-green-600 hover:bg-green-700 text-white font-semibold py-3 rounded-xl transition">
                        Find Gold!
                    </button>
                </form>
            </div>
            <!-- Cave -->
            <div class="bg-slate-900 rounded-2xl p-6 border border-slate-800 hover:border-blue-500 transition duration-300 text-center">
                <div class="text-5xl mb-4">⛰️</div>
                <h2 class="text-2xl font-bold mb-2">
                    Cave
                </h2>
                <p class="text-slate-400 mb-6">
                    Earn 5 - 10 gold
                </p>
                <form action="${pageContext.request.contextPath}/process" method="POST">
                    <input type="hidden" name="place" value="cave">
                    <button type="submit"
                        class="w-full bg-blue-600 hover:bg-blue-700 text-white font-semibold py-3 rounded-xl transition">
                        Find Gold!
                    </button>
                </form>
            </div>
            <!-- House -->
            <div class="bg-slate-900 rounded-2xl p-6 border border-slate-800 hover:border-orange-500 transition duration-300 text-center">
                <div class="text-5xl mb-4">🏠</div>
                <h2 class="text-2xl font-bold mb-2">House</h2>
                <p class="text-slate-400 mb-6">Earn 2 - 5 gold</p>
                <form action="${pageContext.request.contextPath}/process" method="POST">
                    <input type="hidden" name="place" value="house">
                    <button type="submit"
                        class="w-full bg-orange-600 hover:bg-orange-700 text-white font-semibold py-3 rounded-xl transition">
                        Find Gold!
                    </button>
                </form>
            </div>
            <!-- Quest -->
            <div class="bg-slate-900 rounded-2xl p-6 border border-slate-800 hover:border-red-500 transition duration-300 text-center">
                <div class="text-5xl mb-4">⚔️</div>
                <h2 class="text-2xl font-bold mb-2">
                    Quest
                </h2>
                <p class="text-slate-400 mb-6">
                    Earn or lose 0 - 50 gold
                </p>
                <form action="${pageContext.request.contextPath}/process" method="POST">
                    <input type="hidden" name="place" value="quest">
                   <button type="submit"
                        class="w-full bg-red-600 hover:bg-red-700 text-white font-semibold py-3 rounded-xl transition">
                        Go on Quest!
                    </button>
                </form>
            </div>
        </div>
        <!-- Activities -->
        <div class="bg-slate-900 border border-slate-800 rounded-2xl p-6">
            <div class="flex justify-between items-center mb-6">
                <h3 class="text-2xl font-bold">
                    📜 Activities
                </h3>
                <!-- Reset Button -->
                <form action="${pageContext.request.contextPath}/process" method="POST">
                    <input type="hidden" name="place" value="reset">
                    <button type="submit"
                        class="bg-red-600/20 text-red-400 hover:bg-red-600 hover:text-white px-4 py-2 rounded-lg font-semibold transition">
                        Reset Game
                    </button>
                </form>
            </div>
            <ul class="space-y-3">
                <c:choose>
                    <c:when test="${empty activities}">
                        <li class="text-slate-500 text-center py-6">
                            No activities yet. Find some gold!
                        </li>
                    </c:when>
                    <c:otherwise>
                        <c:forEach var="activity" items="${activities}">
                            <li class="bg-slate-800 p-4 rounded-xl text-slate-300 border border-slate-700">
                                ${activity}
                            </li>
                        </c:forEach>
                    </c:otherwise>
                </c:choose>
            </ul>
        </div>
    </div>
</body>
</html>