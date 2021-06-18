import styled, { css } from "styled-components";
import { Box, Heading, Flex} from "@chakra-ui/react";
import "./splashpage.css";

export const Background = styled.section`
  margin: 0;
  min-height: 100vh;
  width: cover;
  height: cover;
  background: linear-gradient(90deg, #0052d4 0%, #4364f7 50%, #6fb1fc 100%);
`;

const SplashPage = (props) => {
  return (
    
      
        <Flex align="center">
            <Box>
                <Heading size="xl">Dream Notes</Heading>
            </Box>
        </Flex>
      
    
  );
};
export default SplashPage;
