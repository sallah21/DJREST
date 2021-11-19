import * as React from 'react';
import { useEffect } from 'react';
import { Button, Container } from '@material-ui/core';
import axios from 'axios';

function App() {
  var data;
  useEffect(()=>{
    axios.get('/myapp/beers/').then(res=>{
      //console.log(res.data);
      data =JSON.parse(res.data);
      //console.log(data);
    }).catch(err=>{console.log(err)});  
  },[])

  return (
    
  <div className="App bg-gray-800 h-screen min-h-screen" >
    <Container maxWidth="md"  >
        <Button variant="contained" >Hello World</Button>
    </Container>
  </div>
  )
 

}


export default App;
