import React, { useState, useRef, useEffect } from "react";
import { BrowserRouter as Router, Routes, Route, Link } from "react-router-dom";

function App() {
  return (
    <Router>
      <div className="min-h-screen bg-gradient-to-br from-pink-50 to-purple-100 font-sans">
        {/* Navigation Bar */}
        <nav className="flex items-center justify-between px-8 py-4 bg-white/80 shadow-md sticky top-0 z-50 backdrop-blur-md">
          <div className="text-2xl font-bold text-pink-600 tracking-tight">VMakeup</div>
          <ul className="flex gap-6 text-lg font-medium text-gray-700">
            <li className="hover:text-pink-500 transition-colors cursor-pointer"><Link to="/">Home</Link></li>
            <li className="hover:text-pink-500 transition-colors cursor-pointer"><Link to="/shop">Shop</Link></li>
            <li className="hover:text-pink-500 transition-colors cursor-pointer"><Link to="/virtual-try-on">Virtual Try-On</Link></li>
            <li className="hover:text-pink-500 transition-colors cursor-pointer"><Link to="/upload-photo">Upload Your Photo</Link></li>
            <li className="hover:text-pink-500 transition-colors cursor-pointer"><Link to="/tutorials">Tutorials</Link></li>
            <li className="hover:text-pink-500 transition-colors cursor-pointer"><Link to="/wishlist">Wishlist</Link></li>
            <li className="hover:text-pink-500 transition-colors cursor-pointer"><Link to="/my-account">My Account</Link></li>
          </ul>
        </nav>

        <Routes>
          <Route path="/" element={
            <>
              {/* Hero Section */}
              <section className="flex flex-col md:flex-row items-center justify-between px-8 py-16 md:py-24 gap-10">
                <div className="flex-1 space-y-6 animate-fade-in-up">
                  <h1 className="text-4xl md:text-6xl font-extrabold text-gray-900 leading-tight">
                    Discover Your <span className="text-pink-500">Perfect Look</span>
                  </h1>
                  <p className="text-lg md:text-2xl text-gray-600 max-w-xl">
                    Try on makeup virtually, get smart product suggestions, and shop the latest trends—all in one luxurious, interactive experience.
                  </p>
                  <div className="flex gap-4 mt-6">
                    <button className="px-6 py-3 bg-pink-500 text-white rounded-lg shadow-lg hover:bg-pink-600 transition-all text-lg font-semibold">Try Virtual Makeup</button>
                    <button className="px-6 py-3 bg-white border border-pink-400 text-pink-500 rounded-lg hover:bg-pink-50 transition-all text-lg font-semibold">Shop Now</button>
                  </div>
                </div>
                <div className="flex-1 flex justify-center animate-fade-in">
                  <img src="https://images.unsplash.com/photo-1517841905240-472988babdf9?auto=format&fit=facearea&w=500&q=80" alt="Makeup Model" className="rounded-3xl shadow-2xl w-80 md:w-96 object-cover" />
                </div>
              </section>

              {/* Trending Collections */}
              <section className="px-8 py-12 bg-white/70 rounded-3xl mx-4 md:mx-16 shadow-xl animate-fade-in-up">
                <h2 className="text-3xl font-bold text-gray-800 mb-6">Trending Collections</h2>
                <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
                  {/* Placeholder cards */}
                  <div className="bg-gradient-to-br from-pink-100 to-pink-200 rounded-xl p-6 shadow-lg hover:scale-105 transition-transform cursor-pointer">
                    <h3 className="text-xl font-semibold mb-2">Spring Blushes</h3>
                    <p className="text-gray-600">Fresh, radiant blushes for a natural glow.</p>
                  </div>
                  <div className="bg-gradient-to-br from-purple-100 to-purple-200 rounded-xl p-6 shadow-lg hover:scale-105 transition-transform cursor-pointer">
                    <h3 className="text-xl font-semibold mb-2">Bestselling Lipsticks</h3>
                    <p className="text-gray-600">Our most-loved shades for every occasion.</p>
                  </div>
                  <div className="bg-gradient-to-br from-yellow-100 to-pink-100 rounded-xl p-6 shadow-lg hover:scale-105 transition-transform cursor-pointer">
                    <h3 className="text-xl font-semibold mb-2">Summer Eyeshadow</h3>
                    <p className="text-gray-600">Vibrant palettes to make your eyes pop.</p>
                  </div>
                </div>
              </section>

              {/* Seasonal Offers */}
              <section className="px-8 py-12 mt-12 animate-fade-in-up">
                <div className="bg-pink-100 rounded-2xl p-8 flex flex-col md:flex-row items-center justify-between shadow-lg">
                  <div className="text-2xl font-bold text-pink-700 mb-4 md:mb-0">🌸 Spring Sale: Up to 30% Off Select Products!</div>
                  <button className="px-6 py-3 bg-pink-500 text-white rounded-lg shadow-lg hover:bg-pink-600 transition-all text-lg font-semibold">Shop Offers</button>
                </div>
              </section>

              {/* Footer */}
              <footer className="mt-16 py-8 text-center text-gray-500 text-sm">
                &copy; {new Date().getFullYear()} VMakeup. All rights reserved.
              </footer>
            </>
          } />
          <Route path="/virtual-try-on" element={
            <div className="flex flex-col items-center justify-center p-8">
              <h1 className="text-3xl font-bold mb-6">Virtual Makeup Try-On</h1>
              <div className="bg-white p-6 rounded-lg shadow-lg w-full max-w-2xl">
                <p className="text-gray-600 mb-4">This feature will allow you to try on makeup products using your camera. Coming soon!</p>
                <button className="px-6 py-3 bg-pink-500 text-white rounded-lg shadow-lg hover:bg-pink-600 transition-all text-lg font-semibold">Start Camera</button>
              </div>
            </div>
          } />
          <Route path="/upload-photo" element={
            <div className="flex flex-col items-center justify-center p-8">
              <h1 className="text-3xl font-bold mb-6">Upload Your Photo</h1>
              <div className="bg-white p-6 rounded-lg shadow-lg w-full max-w-2xl">
                <p className="text-gray-600 mb-4">Upload a photo to try on makeup products. Coming soon!</p>
                <button className="px-6 py-3 bg-pink-500 text-white rounded-lg shadow-lg hover:bg-pink-600 transition-all text-lg font-semibold">Upload Photo</button>
              </div>
            </div>
          } />
        </Routes>

        {/* Simple fade-in animations */}
        <style>{`
          .animate-fade-in-up {
            animation: fadeInUp 1s cubic-bezier(0.23, 1, 0.32, 1);
          }
          .animate-fade-in {
            animation: fadeIn 1.2s cubic-bezier(0.23, 1, 0.32, 1);
          }
          @keyframes fadeInUp {
            0% { opacity: 0; transform: translateY(40px); }
            100% { opacity: 1; transform: translateY(0); }
          }
          @keyframes fadeIn {
            0% { opacity: 0; }
            100% { opacity: 1; }
          }
        `}</style>
      </div>
    </Router>
  );
}

export default App;
