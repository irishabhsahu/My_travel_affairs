import { useEffect } from 'react';
import './SearchSection.css';

const SearchSection = () => {
  useEffect(() => {
    const stickyHeader = document.getElementById('sticky-search');

    const handleScroll = () => {
      if (stickyHeader) {
        stickyHeader.style.display = window.scrollY > window.innerHeight * 0.6 ? 'block' : 'none';
      }
    };

    window.addEventListener('scroll', handleScroll);
    return () => window.removeEventListener('scroll', handleScroll);
  }, []);

  useEffect(() => {
    const searchBar = document.getElementById('search-bar');
    const searchContainer = document.querySelector('.active-search');
    const recommendations = document.getElementById('recommendations');

    if (searchBar && searchContainer && recommendations) {
      searchBar.addEventListener('focus', () => {
        searchContainer.classList.add('focused');
        recommendations.classList.add('visible');
      });

      document.addEventListener('click', (e) => {
        if (!searchContainer.contains(e.target as Node)) {
          searchContainer.classList.remove('focused');
          recommendations.classList.remove('visible');
        }
      });
    }
  }, []);

  return (
    <>
      <header id="sticky-search">
        <div className="search-bar-container">
          <input type="text" placeholder="Search" />
        </div>
      </header>
      <section className="main">
        <video autoPlay muted loop className="background-video">
          <source src="/vids/home_top.mp4" type="video/mp4" />
        </video>
        <div className="overlay">
          <div className="search-wrapper">
            <div className="search-bar-container active-search">
              <input type="text" id="search-bar" placeholder="Search" />
            </div>
            <div className="recommendations" id="recommendations">
              <p>Popular: Japan, Bali, Paris</p>
            </div>
          </div>
        </div>
      </section>
    </>
  );
};

export default SearchSection;
