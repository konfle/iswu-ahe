import React from 'react';

class UserInputForm extends React.Component {
  state = {
    result: null,
    error: null,
  };

  submitForm = () => {
    const appType = document.getElementById("appType").value;
    const performance = document.getElementById("performance").value;
    const url = `http://iswu.default.svc.cluster.local:80/user_input?app_type=${appType}&performance=${performance}`;

    fetch(url)
      .then(response => response.json())
      .then(data => {
        // Aktualizuj stan komponentu po otrzymaniu odpowiedzi od serwera
        this.setState({ result: data.decision, error: null });
        // Przekazuj wynik do komponentu nadrzędnego
        this.props.onFormSubmit(data.decision);
      })
      .catch(error => {
        console.error('Error:', error);
        // Aktualizuj stan komponentu w przypadku błędu
        this.setState({ result: null, error: 'Something went wrong.' });
        // Przekazuj informację o błędzie do komponentu nadrzędnego
        this.props.onFormSubmit('Error: Something went wrong.');
      });
  }

  render() {
    return (
      <div>
        <h1>Programming Language Selector</h1>
        <form>
          <label htmlFor="appType">Application Type:</label>
          <input type="text" id="appType" name="appType" required />

          <label htmlFor="performance">Performance (true/false):</label>
          <input type="text" id="performance" name="performance" required />

          <button type="button" onClick={this.submitForm}>Submit</button>
        </form>
        <div id="result">
          {this.state.result && <p>Decision: {this.state.result}</p>}
          {this.state.error && <p>Error: {this.state.error}</p>}
        </div>
      </div>
    );
  }
}

export default UserInputForm;
