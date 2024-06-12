
import React, { useEffect, useState } from 'react';
import axios from 'axios';

const Deals = () => {
    const [deals, setDeals] = useState([]);

    useEffect(() => {
        axios.get('http://localhost:5000/deals')
            .then(response => {
                setDeals(response.data);
            })
            .catch(error => {
                console.error('There was an error fetching the deals!', error);
            });
    }, []);

    return (
        <div>
            <h1>Grocery Deals</h1>
            <ul>
                {deals.map((deal, index) => (
                    <li key={index}>
                        {deal.name} - {deal.price} - {deal.store}
                    </li>
                ))}
            </ul>
        </div>
    );
};

export default Deals;
                