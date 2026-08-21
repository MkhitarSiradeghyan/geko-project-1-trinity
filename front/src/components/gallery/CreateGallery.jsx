import { useState } from "react";
import { useDispatch } from "react-redux";
import { createGallery } from "../store/gallerySlice";

const CreateGallery = () => {
  const dispatch = useDispatch();
  const [title, setTitle] = useState("");
  const [description, setDescription] = useState("");
  const [isPublic, setIsPublic] = useState(true);
  const handleSubmit = async (event) => {
    event.preventDefault();

    if (!title.trim()) {
      return;
    }
    try {
      await dispatch(
        createGallery({
          title,
          description,
          is_public: isPublic,
        })
      ).unwrap();
      setTitle("");
      setDescription("");
      setIsPublic(true);
    } catch (error) {
      console.error(error);
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <h2>Create Gallery</h2>
      <div>
        <label>Title</label>
        <input
          type="text"
          value={title}
          onChange={(event) =>
            setTitle(event.target.value)
          }
        />
      </div>
      <div>
        <label>Description</label>
        <textarea
          value={description}
          onChange={(event) =>
            setDescription(event.target.value)
          }
        />
      </div>
      <div>
        <label>
          <input
            type="checkbox"
            checked={isPublic}
            onChange={(event) =>
              setIsPublic(event.target.checked)
            }
          />
          Public
        </label>
      </div>
      <button type="submit">
        Create Gallery
      </button>
    </form>
  );
};

export default CreateGallery;