
import { Link, Outlet } from "react-router-dom";
export const NewProducts = () =>{
    return(
    <>
    <p>List of New Products</p>
    <div>
 <Link to='Chocolate'>CHCOLATE!</Link>
 </div>
 <Outlet/>
    </>
    );
   }