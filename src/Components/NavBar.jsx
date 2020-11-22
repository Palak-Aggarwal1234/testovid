import {Navbar, Nav} from 'react-bootstrap'
import '../Styles/NavBar.css';
import logo from '../Assets/testovid.png';
function NavBar() {
  return (
    <div>
     <Navbar bg="dark" variant="dark" fixed= 'top'>
    <Navbar.Brand href="#home" >
      <img
        alt=""
        src={logo}
        width="30"
        height="30"
        className="d-inline-block align-top"
      />{' '}TESTOVID
    </Navbar.Brand>
  </Navbar>
  <Navbar collapseOnSelect expand="lg" bg="primary" variant="dark" fixed = 'bottom'>
  <Navbar.Brand href="#home">Testing now in your palms</Navbar.Brand>
  <Navbar.Toggle aria-controls="responsive-navbar-nav" />
  <Navbar.Collapse id="responsive-navbar-nav">
    <Nav className="mr-auto">
      <Nav.Link href="#features"></Nav.Link>
      <Nav.Link href="#pricing"></Nav.Link>
    </Nav>
    <Nav>
      <Nav.Link href="#login">Login</Nav.Link>
      <Nav.Link eventKey={2} href="#signup">
        Sign-Up
      </Nav.Link>
    </Nav>
  </Navbar.Collapse>
</Navbar>

    </div>
  );
}

export default NavBar;