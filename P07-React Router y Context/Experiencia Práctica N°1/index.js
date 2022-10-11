import React from 'react';
import ReactDOM from "react-dom/client";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import Layout from "./pages/Layout";
import Home from "./pages/Home";

import NoPage from "./pages/NoPage";

import { Products } from './pages/Products';
import { FeaturedProducts } from './pages/FeaturedProducts';
import { NewProducts } from './pages/NewProducts';

import { Choco } from './pages/Choco';

import { Users } from './pages/Users';

export default function MiApp() {
 return (
 <BrowserRouter>
 <Routes>
 <Route path="/" element={<Layout />}>
 <Route index element={<Home />} />
 <Route path="products" element={<Products/>} >
 <Route path="featured" element={<FeaturedProducts/>} />
 <Route path="new" element={<NewProducts/>} >
 <Route path="Chocolate" element={<Choco/>} />
 </Route>
 <Route path="Chocolate" element={<Choco/>} />
 </Route>
 <Route path="Usuarios_De_La_Nasa" element={<Users/>}>
 </Route>
 <Route path="*" element={<NoPage />} />
 </Route>
 </Routes>
 </BrowserRouter>
 );
}
const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
 <React.StrictMode>
 <MiApp />
 </React.StrictMode>
 );