import { Outlet } from "react-router-dom";
export const Users = () => {
 return(
 <div><h1>Usuario Alfredo</h1>
 <h1>Usuario Tomate</h1>
 <h1>Usuario terceario</h1>
 <Outlet/>
 </div>
 );
}