import { useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import {
  fetchGalleries,
  fetchGalleryById,
} from "../store/gallerySlice";

const GalleryList = () => {
  const dispatch = useDispatch();

  const {
    galleries,
    loading,
    error,
  } = useSelector((state) => state.gallery);

  useEffect(() => {
    dispatch(fetchGalleries());
  }, [dispatch]);

  if (loading) {
    return <p>Loading...</p>;
  }
  
  if (error) {
    return <p>{error}</p>;
  }

  return (
    <div>
      <h2>Galleries</h2>
      {galleries.length === 0 && (
        <p>No galleries found</p>
      )}
      {galleries.map((gallery) => (
        <div key={gallery.id}>
          <h3>{gallery.title}</h3>
          <p>{gallery.description}</p>
          <p>{gallery.is_public ? "Public" : "Private"}</p>
          <button onClick={() =>dispatch(fetchGalleryById(gallery.id))}>
            Open
          </button>
        </div>
      ))}
    </div>
  );
};

export default GalleryList;