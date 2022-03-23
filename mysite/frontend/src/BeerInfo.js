import React from "react";
import "./App.css"
const BeerInfo = ({data})=>{
    return (
<div  className="py-3 overflow-hidden text-white shadow-2xl bg-gray-800 mb-2 grid place-items-center w-full rounded-2xl content-center " id={data.id}>
        <div  className="BeerInfo">
         {/* <button class={`${loaded?"bg-red-500":"bg-green-500"}`} onClick={()=>{setLoaded(!loaded)}}>test</button>*/} 
        <div>
        <a className='font-black'><strong>Name : {data.name} </strong> </a>
        </div>
        <div>
        <a>Alcohol : {data.alc}% </a>
        </div>
        <div>
        <a>Ibu : {data.ibu}% </a>
        </div>
        <div>
            <p>Type : {data.type}  </p>
        </div>
        <div>
        {data.brewery!==undefined? (<a>Brewery : {data.brewery} </a>):(<div></div>)}
        </div>
        <p>Description :</p>
        { data.description? (<div><a> {data.description}</a></div>):(<div>None description has been yeeet</div>)}
 
         </div>
   </div>
    
    );
}
export default BeerInfo