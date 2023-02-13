import HomeBody from "./components/HomeBody";
import Navbar from "./components/Navbar";

function App() {
  return (
    <div className="App" style={{boxSizing:'border-box'}}>
      <Navbar />
      <HomeBody />
    </div>
  );
}

export default App;
