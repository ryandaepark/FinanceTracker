import styled from 'styled-components';
import * as React from 'react';
import Table from './components/Tables'

const Title = styled.h1`
  font-size: 2em;
  text-align: center;
  color: #BF4F74;
`

function App() {
  return (
    <div className="App">
      <Title> Finance Tracker </Title>
      <Table/>
    </div>
  );
}

export default App;
