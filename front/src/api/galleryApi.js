const API_URL = "/api";

export const getGalleries = async () => {
  const response = await fetch(`${API_URL}/galleries/`);
  if (!response.ok) {
    throw new Error("Failed to fetch galleries");
  }
  return response.json();
};

export const createGallery = async (galleryData) => {
  const response = await fetch(`${API_URL}/galleries/`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(galleryData),
  });
  if (!response.ok) {
    throw new Error("Failed to create gallery");
  }
  return response.json();
};

export const getGalleryById = async (id) => {
  const response = await fetch(`${API_URL}/galleries/${id}/`);
  if (!response.ok) {
    throw new Error("Failed to fetch gallery");
  }
  return response.json();
};

export const uploadPhotos = async (galleryId, formData) => {
  const response = await fetch(
    `${API_URL}/galleries/${galleryId}/upload/`,
    {
      method: "POST",
      body: formData,
    }
  );
  if (!response.ok) {
    throw new Error("Failed to upload photos");
  }
  return response.json();
};

export const deletePhoto = async (photoId) => {
  const response = await fetch(`${API_URL}/photos/${photoId}/`, {
    method: "DELETE",
  });
  if (!response.ok) {
    throw new Error("Failed to delete photo");
  }
  return photoId;
};