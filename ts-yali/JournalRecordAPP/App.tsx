import React from 'react';
import './App.css';
import 'purecss/build/pure.css'
import JournalPanel from './JournalPanel';

/**
 * the App class
 */
class App extends React.Component{
  
  /**
   * Render JSX Content.
   * @returns JSX Element.
   */
  render(): JSX.Element {
    return(
        <div className="APP" style={{margin:20}}>
          <JournalPanel/>
        </div>
    );
  }
}

export default App;
