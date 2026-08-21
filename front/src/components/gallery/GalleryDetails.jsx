import { useSelector } from "react-redux";
import UploadPhotos from "./UploadPhotos";
import PhotoList from "./PhotoList";

const GalleryDetails = () => {
  const { currentGallery } = useSelector(
    (state) => state.gallery
  );

  if (!currentGallery) {
    return (
      <p>Select a gallery</p>
    );
  }

  return (
    <div>
      <h2>{currentGallery.title}</h2>
      <p>{currentGallery.description}</p>
      <UploadPhotos
        galleryId={currentGallery.id}
      />
      <PhotoList
        photos={currentGallery.photos || []}
      />
    </div>
  );
};

export default GalleryDetails;