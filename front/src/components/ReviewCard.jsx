import { useDispatch } from "react-redux";
import { deleteReview } from "../features/reviews/reviewsSlice";

function ReviewCard({ review }) {
    const dispatch = useDispatch();

    const handleDelete = () => {
        dispatch(deleteReview(review.id));
    };

    return (
        <div className="review-card">
            <h3>{review.user}</h3>

            <p>
                Tour: {review.tour}
            </p>

            <p className="rating">
                {"⭐".repeat(review.rating)}
            </p>

            <p>
                {review.comment || "No comment"}
            </p>

            <small>
                {new Date(review.created_at).toLocaleDateString()}
            </small>

            <br />

            <button onClick={handleDelete}>
                Delete
            </button>
        </div>
    );
}

export default ReviewCard;