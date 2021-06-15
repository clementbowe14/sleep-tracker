import logo from "./logo.svg";
import "./App.css";
import { ChakraProvider } from "@chakra-ui/react";
import SplashPage from "./pages/splashPage";
import Dashboard from "./pages/dashboard";
import { BrowserRouter as Router, Switch, Route, Link } from "react-router-dom";
function App() {
  return (
    <ChakraProvider>
    <Router>
      <Switch>
        <Route path="/index">
          <Dashboard></Dashboard>
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
