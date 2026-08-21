import { useState } from "react";
import { useDispatch } from "react-redux";
import {
  uploadPhotos,
  fetchGalleryById,
} from "../store/gallerySlice";

const UploadPhotos = ({ galleryId }) => {
  const dispatch = useDispatch();
  const [files, setFiles] = useState([]);
  const handleFileChange = (event) => {
    setFiles(Array.from(event.target.files));
  };

  const handleUpload = async () => {
    if (files.length === 0) {
      return;
    }
    
    const formData = new FormData();

    files.forEach((file) => {
      formData.append("images", file);
    });

    try {
      await dispatch(
        uploadPhotos({
          galleryId,
          formData,
        })
      ).unwrap();

      await dispatch(
        fetchGalleryById(galleryId)
      );

      setFiles([]);
    } catch (error) {
      console.error(error);
    }
  };

  return (
    <div>
      <h3>Upload Photos</h3>

      <input
        type="file"
        multiple
        accept="image/jpeg,image/png,image/webp"
        onChange={handleFileChange}
      />
      <button
        type="button"
        onClick={handleUpload}
      >
        Upload
      </button>
    </div>
  );
};

export default UploadPhotos;