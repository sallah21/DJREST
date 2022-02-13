import * as React from 'react';
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
      // console.log(res.data);
      data =JSON.parse(res.data);
      setBeerInfo(data);
    }).catch(err=>{console.log(err)});  
  },[])
  // console.log(beerInfo);
  return (
    
    
  <div className="App bg-gray-900 h-screen min-h-screen grid place-items-center" >
    <Container maxWidth="md"  className="flex"  >
      <div class="flex gap-5 ">
        {beerInfo.map(elem=>{
          console.log(elem);
          return <BeerInfo  id = {elem.pk} data={elem.fields}/>
        })}
      </div>
      <Router>
        <Button variant="contained"><Link >Hello World</Link></Button>
      </Router>
    </Container>

  </div>

  )
 

}


export default App;
