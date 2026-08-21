import { useDispatch } from "react-redux";
import {
  deletePhoto,
} from "../store/gallerySlice";

const PhotoList = ({ photos }) => {
  const dispatch = useDispatch();
  const handleDelete = async (photoId) => {
    try {
      await dispatch(deletePhoto(photoId)).unwrap();
    } catch (error) {
      console.error(error);
    }
  };

  if (photos.length === 0) {
    return <p>No photos</p>;
  }

  return (
    <div>
      <h3>Photos</h3>
      {photos.map((photo) => (
        <div key={photo.id}>
          <img
            src={photo.image}
            alt={photo.caption || "Gallery image"}
            width="200"
          />

          {photo.caption && (
            <p>{photo.caption}</p>
          )}

          {photo.file_size && (
            <p>
              Size: {photo.file_size} bytes
            </p>
          )}
          <button
            onClick={() =>
              handleDelete(photo.id)
            }
          >
            Delete
          </button>
        </div>
      ))}
    </div>
  );
};

export default PhotoList;