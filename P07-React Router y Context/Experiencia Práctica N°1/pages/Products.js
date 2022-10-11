import { Link, Outlet } from "react-router-dom";
export const Products = () =>{
 return(
 <>
 <div>
 <input type='search' placeholder='search products' />
 </div>
 <div>
 <Link to='featured'>Features</Link>
 <Link to='new'>New</Link>
 <Link to='Chocolate'>CHCOLATE!</Link>
 </div>
 <Outlet/>
 </>
 );
}