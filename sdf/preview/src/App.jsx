import { useState, useEffect } from "react";
import { StlViewer } from "react-stl-viewer";
import "./App.css";

const renderedMeshUrl = new URL("./assets/mesh.stl", import.meta.url).href;
const renderedImageUrl = new URL("./assets/mesh.stl", import.meta.url).href;
const infoUrl = new URL("./assets/info.txt", import.meta.url).href;

function App() {
  const [name, setName] = useState("");
  const [version, setVersion] = useState(0);
  const [loading, isLoading] = useState(true);
  const [showMesh, setShowMesh] = useState(true);
  const [showImage, setShowImage] = useState(false);

  useEffect(() => {
    const id = setInterval(() => {
      fetch(infoUrl)
        .then((r) => r.text())
        .then((info) => {
          const [type, renderId, name] = info.split(" ");
          setName(name);
          setVersion(parseInt(renderId));
          isLoading(false);
          if (type === "stl") {
            setShowMesh(true);
            setShowImage(false);
          } else if (type === "image") {
            setShowMesh(false);
            setShowImage(true);
          } else {
            setShowMesh(true);
            setShowImage(true);
          }
        });
    }, 500);
    return () => clearInterval(id);
  }, []);

  if (loading) {
    return null;
  }

  return (
    <div className="App">
      <h3>{name}</h3>
      <div className="preview">
        {showImage && <img src={renderedImageUrl + "?v=" + version} alt="Rendered stl" />}
        {showMesh && (
          <StlViewer
            style={{
              top: 0,
              left: 0,
              width: "100vw",
              height: "100vh",
            }}
            orbitControls
            shadows
            url={renderedMeshUrl + "?v=" + version}
          />
        )}
      </div>
    </div>
  );
}

export default App;
