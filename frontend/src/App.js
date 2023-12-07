import React from 'react';
import UserInputForm from './UserInputForm';

class App extends React.Component {
  handleFormSubmit = (result) => {
    // Przetwarzaj wynik w sposób odpowiedni dla twojej aplikacji
    console.log(result);
  }

  render() {
    return (
      <div>
        {/* Inne elementy aplikacji */}
        <UserInputForm onFormSubmit={this.handleFormSubmit} />
      </div>
    );
  }
}

export default App;
