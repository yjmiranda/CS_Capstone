import React from 'react';
import { Link } from 'react-router-dom';

export default function FormPage() {
    return (
        <div>
            <h1>This is the Form Page.</h1>
            <Link to="/"><button>Home</button></Link>
        </div>
    )
}