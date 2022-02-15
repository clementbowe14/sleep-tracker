
import "./App.css";
import SplashPage from "./pages/splashPage";
import Dashboard from "./pages/dashboard";
import Background from "./pages/splashPage"
import { BrowserRouter as Router, Switch, Route, Link } from "react-router-dom";
import { ChakraProvider } from "@chakra-ui/react";
function App() {
  return (
    <ChakraProvider>
   
    <Router>
      <Switch>
        <Route path="/index">
          <Dashboard/>
        </Route>
        <Route path="/">
          <SplashPage />
        </Route>
      </Switch>
      </Router>
      </ChakraProvider>
  );
}

export default App;
