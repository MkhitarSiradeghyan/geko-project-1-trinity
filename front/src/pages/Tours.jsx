import { useGetToursQuery } from "../../store/api/toursApi";


const Tours = () => {
    const {
        data: tours,
        isLoading,
        isError,
        error,
    } = useGetToursQuery();

    console.log("TOURS:", tours);
    console.log("ERROR:", error);

    if (isLoading) {
        return <p>Loading...</p>;
    }

    if (isError) {
        return <p>Something went wrong.</p>;
    }

    return (
        <div>
            <h1>Tours</h1>

            {tours?.map((tour) => (
                <div key={tour.id}>
                    <h2>{tour.title}</h2>
                    <p>
                        {tour.price} {tour.currency}
                    </p>
                </div>
            ))}
        </div>
    );
};

export default Tours;