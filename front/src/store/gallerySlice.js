import { createAsyncThunk, createSlice } from "@reduxjs/toolkit";
import {
  getGalleries,
  createGallery as createGalleryApi,
  getGalleryById,
  uploadPhotos as uploadPhotosApi,
  deletePhoto as deletePhotoApi,
} from "../api/galleryApi";


export const fetchGalleries = createAsyncThunk(
  "gallery/fetchGalleries",
  async () => {
    return await getGalleries();
  }
);

export const createGallery = createAsyncThunk(
  "gallery/createGallery",
  async (galleryData) => {
    return await createGalleryApi(galleryData);
  }
);

export const fetchGalleryById = createAsyncThunk(
  "gallery/fetchGalleryById",
  async (id) => {
    return await getGalleryById(id);
  }
);

export const uploadPhotos = createAsyncThunk(
  "gallery/uploadPhotos",
  async ({ galleryId, formData }) => {
    return await uploadPhotosApi(galleryId, formData);
  }
);

export const deletePhoto = createAsyncThunk(
  "gallery/deletePhoto",
  async (photoId) => {
    await deletePhotoApi(photoId);

    return photoId;
  }
);

const initialState = {
  galleries: [],
  currentGallery: null,
  loading: false,
  error: null,
};

const gallerySlice = createSlice({
  name: "gallery",
  initialState,

  reducers: {
    clearCurrentGallery: (state) => {
      state.currentGallery = null;
    },
  },

  extraReducers: (builder) => {
    builder

      .addCase(fetchGalleries.pending, (state) => {
        state.loading = true;
        state.error = null;
      })
      .addCase(fetchGalleries.fulfilled, (state, action) => {
        state.loading = false;
        state.galleries = action.payload;
      })
      .addCase(fetchGalleries.rejected, (state, action) => {
        state.loading = false;
        state.error = action.error.message;
      })

      .addCase(createGallery.fulfilled, (state, action) => {
        state.galleries.push(action.payload);
      })

      .addCase(fetchGalleryById.pending, (state) => {
        state.loading = true;
        state.error = null;
      })
      .addCase(fetchGalleryById.fulfilled, (state, action) => {
        state.loading = false;
        state.currentGallery = action.payload;
      })
      .addCase(fetchGalleryById.rejected, (state, action) => {
        state.loading = false;
        state.error = action.error.message;
      })

      .addCase(uploadPhotos.fulfilled, (state) => {

      })

      .addCase(deletePhoto.fulfilled, (state, action) => {
        if (state.currentGallery) {
          state.currentGallery.photos =
            state.currentGallery.photos.filter(
              (photo) => photo.id !== action.payload
            );
        }
      });
  },
});

export const { clearCurrentGallery } = gallerySlice.actions;

export default gallerySlice.reducer;