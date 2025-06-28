import React from 'react';
import { Link } from 'react-router-dom';

export default function LearnPage() {
    return (
        <div>
            <h1>This is the Learn Page.</h1>
            <Link to="/"><button>Home</button></Link>
        </div>
    )
}