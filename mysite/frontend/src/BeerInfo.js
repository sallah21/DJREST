import React from "react";
import "./App.css"
import { useEffect, useState } from 'react';
import axios from 'axios';
const BeerInfo = ({data})=>{
    const [brewInfo, setBrewInfo] = useState([]); 
  const [loaded, setLoaded] = useState(true);
  console.log(data);
  useEffect(()=>{
    axios.get('/myapp/brewery/'+data.brewery).then(res=>{
     const brewer =JSON.parse(res.data);
      setBrewInfo(brewer);
    }).catch(err=>{console.log(err)});  
  },[])
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
        {brewInfo[0]!==undefined? (<a>Brewery : {brewInfo[0].fields.name} </a>):(<div></div>)}
        </div>
        <p>Description :</p>
        { data.description? (<div><a> {data.description}</a></div>):(<div>None description has been yeeet</div>)}
 
         </div>
   </div>
    
    );
}
export default BeerInfo