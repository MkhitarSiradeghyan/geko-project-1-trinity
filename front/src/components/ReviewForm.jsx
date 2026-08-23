import { useState } from "react";
import { useDispatch, useSelector } from "react-redux";

import {
    createReview,
} from "../features/reviews/reviewsSlice";


function ReviewForm() {
    const dispatch = useDispatch();

    const creating = useSelector(
        (state) => state.reviews.creating
    );

    const error = useSelector(
        (state) => state.reviews.error
    );


    const [tour, setTour] = useState("");
    const [rating, setRating] = useState("");
    const [comment, setComment] = useState("");


    const handleSubmit = async (event) => {
        event.preventDefault();

        if (!tour || !rating) {
            alert("Tour and rating are required.");
            return;
        }


        const result = await dispatch(
            createReview({
                tour: Number(tour),
                rating: Number(rating),
                comment: comment,
            })
        );


        if (createReview.fulfilled.match(result)) {
            setTour("");
            setRating("");
            setComment("");
        }
    };


    return (
        <section className="review-form">

            <h2>Add Review</h2>

            <form onSubmit={handleSubmit}>

                <label>
                    Tour ID
                </label>

                <input
                    type="number"
                    placeholder="Enter tour ID"
                    value={tour}
                    onChange={(event) =>
                        setTour(event.target.value)
                    }
                />


                <label>
                    Rating
                </label>

                <select
                    value={rating}
                    onChange={(event) =>
                        setRating(event.target.value)
                    }
                >

                    <option value="">
                        Select rating
                    </option>

                    <option value="5">
                        5
                    </option>

                    <option value="4">
                        4
                    </option>

                    <option value="3">
                        3
                    </option>

                    <option value="2">
                        2
                    </option>

                    <option value="1">
                        1
                    </option>

                </select>


                <label>
                    Comment
                </label>

                <textarea
                    placeholder="Write your review"
                    value={comment}
                    onChange={(event) =>
                        setComment(event.target.value)
                    }
                    rows="5"
                />


                {error && (
                    <p className="error">
                        {typeof error === "string"
                            ? error
                            : "Failed to create review"}
                    </p>
                )}


                <button
                    type="submit"
                    disabled={creating}
                >
                    {creating
                        ? "Sending..."
                        : "Add Review"}
                </button>

            </form>

        </section>
    );
}


export default ReviewForm;