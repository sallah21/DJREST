
import { useEffect, useState } from 'react';
import { Button, Container} from '@material-ui/core';
import axios from 'axios';
import BeerInfo from './BeerInfo'
import {Link, BrowserRouter as Router} from 'react-router-dom'

function App() {
  var data;
  const [beerInfo, setBeerInfo] = useState([]); 
  useEffect(()=>{
    axios.get('/myapp/beers/').then(res=>{
      console.log(res.data);
      data =JSON.parse(res.data);
      setBeerInfo(data);
    }).catch(err=>{console.log(err)});  
  },[])
  // console.log(beerInfo);
  return (
    
    
  <div className="App bg-gray-900 h-screen min-h-screen grid place-items-center" >
    <Container maxWidth="md"  className="flex"  >
      <div className="flex gap-5 ">
        {beerInfo.map(elem=>{
          return <BeerInfo key = {elem.id}  id = {elem.id} data={elem}/>
        })}
      </div>
      
        <Button variant="contained">Add Beer</Button>
      
    </Container>

  </div>

  )
 

}


export default App;
