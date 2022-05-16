import { ReactComponent as GithubIcon } from "assets/img/github.svg";
import './style.css';

function Navbar() {
    return (
        <header>
            <nav className="container">
                <div className="deltaavamovie-nav-content">
                    <h1>Delta AVA Movie</h1>
                    <a href="https://github.com/hygorrasec/Engenharia-de-Software/tree/main/Spring%20React/deltaavamovie" target="_blank" rel="noreferrer">
                        <div className="deltaavamovie-contact-container">
                            <GithubIcon />
                            <p className="deltaavamovie-contact-link">/deltaavamovie</p>
                        </div>
                    </a>
                </div>
            </nav>
        </header>
    );
}

export default Navbar;