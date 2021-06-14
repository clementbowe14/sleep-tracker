import logo from './logo.svg';
import './App.css';
import { ChakraProvider } from "@chakra-ui/react"
import SplashPage from './pages/splashPage';
function App() {
  return (
    <ChakraProvider>
      <SplashPage></SplashPage>
    </ChakraProvider>
  );
}

export default App;
