import '../Styles/about.css';
import medicine from '../Assets/medicine.svg';

function About() {
  return (
     <div className= 'about'> 
     <img src={medicine} className="medicine" alt="medicine"/>
     <div className='info'>
         <h2>ABOUT US</h2>
         <p>We are a team that aims <br />
            to provide people's <br /> COVID results
            by asking <br />their symptoms <br />
            and then asking <br />0them to upload a CT scan <br /> 
            of their lungs. 
         </p>
     </div>
     </div>
  );
}

export default About;