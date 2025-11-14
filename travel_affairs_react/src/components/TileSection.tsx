import './TileSection.css';

const tiles = [
  { title: 'Japan', desc: 'Short description for tile one.', img: '/img/Japan.jpeg' },
  { title: 'Malaysia', desc: 'description', img: '/img/Malaysia.jpeg' },
  { title: 'Korea', desc: 'Another short description for tile two.', img: '/img/Korea.jpeg' },
  { title: 'Bali', desc: 'Another short description for tile two.', img: '/img/Bali.jpeg' },
  { title: 'Title Two', desc: 'Another short description for tile two.', img: '/img/image2.jpg' },
  { title: 'Title Two', desc: 'Another short description for tile two.', img: '/img/image2.jpg' },
];

const TileSection = () => {
  return (
    <div className="tile-container">
      {tiles.map((tile, index) => (
        <div className="tile" key={index}>
          <div className="tile-image" style={{ backgroundImage: `url(${tile.img})` }}></div>
          <div className="tile-content">
            <h2 className="tile-title">{tile.title}</h2>
            <p className="tile-description">{tile.desc}</p>
          </div>
        </div>
      ))}
    </div>
  );
};

export default TileSection;
