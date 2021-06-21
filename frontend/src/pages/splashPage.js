import styled, { css } from "styled-components";
import { Center, Box, Heading, Flex, Button, Container } from "@chakra-ui/react";
import "./splashpage.css";

export const Background = styled.section`
  margin: 0;
  min-height: 100vh;
  width: 100%;
  height: 100%;
  background: linear-gradient(90deg, #0052d4 0%, #4364f7 50%, #6fb1fc 100%);
`;

const SplashPage = (props) => {
  return (
  
    <Center direction="column" w={"100%"} h={"50%"}>
      <Box className="splash-headings">
        <Heading>Dream Notes</Heading>
        <Container id="splash-subheading">
          
        </Container>
      </Box>
    </Center>
  
  );
};
export default SplashPage;
