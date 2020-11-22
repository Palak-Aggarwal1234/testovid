import '../Styles/header.css';
import logo from '../Assets/testovid.png';

function Header() {
  return (
     <div className= ' header'> 
     <img
      className="d-block w-100"
      src={logo}
      alt="Testovid"
    />
     </div>
  );
}

export default Header;