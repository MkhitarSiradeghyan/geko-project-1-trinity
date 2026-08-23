import { useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";

import {
    fetchReviews,
} from "../features/reviews/reviewsSlice";

import ReviewCard from "./ReviewCard";


function ReviewList() {
    const dispatch = useDispatch();

    const {
        reviews,
        loading,
        error,
    } = useSelector(
        (state) => state.reviews
    );


    useEffect(() => {
        dispatch(fetchReviews());
    }, [dispatch]);


    if (loading) {
        return <p>Loading reviews...</p>;
    }


    if (error) {
        return (
            <p>
                Error loading reviews
            </p>
        );
    }


    return (
        <section>
            <h2>Reviews</h2>

            {reviews.length === 0 ? (
                <p>No reviews yet.</p>
            ) : (
                reviews.map((review) => (
                    <ReviewCard
                        key={review.id}
                        review={review}
                    />
                ))
            )}
        </section>
    );
}


export default ReviewList;