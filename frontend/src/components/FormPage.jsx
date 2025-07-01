import React, { useState } from 'react';
import { Link } from 'react-router-dom';
import {
    EMPLOYMENT_OPTIONS,
    MARITAL_OPTIONS,
    EDUCATION_OPTIONS,
    LOAN_PURPOSE_OPTIONS
} from "./js/dropdownOptions.js"

function FormPage() {
    // stores the object that will be sent to the server
    const [formData, setFormData] = useState({
        age: '',
        income: '',
        loan_amount: '',
        credit_score: '',
        months_employed: '',
        num_credit_lines: '',
        interest_rate: '',
        loan_term: '',
        dti_ratio: '',
        education: '',
        employment_type: '',
        marital_status: '',
        has_mortgage: '',
        has_dependents: '',
        loan_purpose: '',
        has_co_signer: ''
    });

    // stores result sent back from server
    const [result, setResult] = useState(null);

    // updates state object
    const handleChange = e => {
        const {name, value} = e.target;
        setFormData(prev => ({ ...prev, [name]: value}))
    }

    // handles what happens when form is submitted
    const handleSubmit = async e => {
        e.preventDefault();

        // convert values from string to numerical
        const formattedData = {
            ...formData,
            age: Number(formData.age),
            income: Number(formData.income),
            loan_amount: Number(formData.loan_amount),
            credit_score: Number(formData.credit_score),
            months_employed: Number(formData.months_employed),
            num_credit_lines: Number(formData.num_credit_lines),
            interest_rate: Number(formData.interest_rate),
            loan_term: Number(formData.loan_term),
            dti_ratio: Number(formData.dti_ratio),
            education: Number(formData.education),
            employment_type: Number(formData.employment_type),
            marital_status: Number(formData.marital_status),
            has_mortgage: Number(formData.has_mortgage),
            has_dependents: Number(formData.has_dependents),
            loan_purpose: Number(formData.loan_purpose),
            has_co_signer: Number(formData.has_co_signer)
        }

        const response = await fetch("http://localhost:8000/api/predict", {
           method: "POST",
           headers: { "Content-Type": "application/json" },
           body: JSON.stringify(formattedData)
        });

        const data = await response.json();
        setResult(data);
    }

    // renders the select component
    const renderSelect = (label, name, options) => (
        <label className="flex flex-col">
            <span className="font-bold">{label}</span>
            <select name={name} value={formData[name]} onChange={handleChange} className="border border-slate-300 rounded px-2 py-1 mt-1 focus:outline-none focus:ring-2 focus:ring-blue-400">
                <option value="">Select</option>
                {Object.entries(options).map(([label,value]) => (
                    <option key={value} value={value}>{label}</option>
                ))}
            </select>
        </label>
    );

    return (
        <div className="min-h-screen bg-slate-100 flex flex-col items-center py-10 px-4">

            {/*Navigation*/}
            <div className="w-full max-w-2xl mb-4 text-left">
                <Link to="/" className="text-blue-600 hover:underline">&larr; Back to Home</Link>
            </div>
             <h1 className="text-3xl font-bold mb-6 text-center text-blue-900">
                 Loan Default Predictor
             </h1>

            {/*Prediction Form*/}
            <form onSubmit={handleSubmit} className="w-full max-w-2xl bg-white p-6 rounded-xl shadow-md grid grid-cols-1 md:grid-cols-2 gap-4">
                <label className="flex flex-col">
                    <span className="font-bold">Age</span>
                    <input type="number" name="age" value={formData.age} onChange={handleChange} className="border border-slate-300 rounded px-2 py-1 mt-1 focus:outline-none focus:ring-2 focus:ring-blue-400" />
                </label>

                <label className="flex flex-col">
                    <span className="font-bold">Income</span>
                    <input type="number" name="income" value={formData.income} onChange={handleChange} className="border border-slate-300 rounded px-2 py-1 mt-1 focus:outline-none focus:ring-2 focus:ring-blue-400" />
                </label>

                <label className="flex flex-col">
                    <span className="font-bold">Loan Amount</span>
                    <input type="number" name="loan_amount" value={formData.loan_amount} onChange={handleChange} className="border border-slate-300 rounded px-2 py-1 mt-1 focus:outline-none focus:ring-2 focus:ring-blue-400" />
                </label>

                <label className="flex flex-col">
                     <span className="font-bold">Credit Score</span>
                    <input type="number" name="credit_score" value={formData.credit_score} onChange={handleChange} className="border border-slate-300 rounded px-2 py-1 mt-1 focus:outline-none focus:ring-2 focus:ring-blue-400" />
                </label>

                <label className="flex flex-col">
                    <span className="font-bold">Months Employed</span>
                    <input type="number" name="months_employed" value={formData.months_employed} onChange={handleChange} className="border border-slate-300 rounded px-2 py-1 mt-1 focus:outline-none focus:ring-2 focus:ring-blue-400" />
                </label>

                <label className="flex flex-col">
                    <span className="font-bold">Number of Credit Lines</span>
                    <input type="number" name="num_credit_lines" value={formData.num_credit_lines} onChange={handleChange} className="border border-slate-300 rounded px-2 py-1 mt-1 focus:outline-none focus:ring-2 focus:ring-blue-400" />
                </label>

                <label className="flex flex-col">
                    <span className="font-bold">Interest Rate</span>
                    <input type="number" name="interest_rate" value={formData.interest_rate} onChange={handleChange} className="border border-slate-300 rounded px-2 py-1 mt-1 focus:outline-none focus:ring-2 focus:ring-blue-400" />
                </label>

                <label className="flex flex-col">
                    <span className="font-bold">Loan Term (months)</span>
                    <input type="number" name="loan_term" value={formData.loan_term} onChange={handleChange} className="border border-slate-300 rounded px-2 py-1 mt-1 focus:outline-none focus:ring-2 focus:ring-blue-400" />
                </label>

                <label className="flex flex-col">
                    <span className="font-bold">DTI Ratio</span>
                    <input type="number" name="dti_ratio" step="0.01" value={formData.dti_ratio} onChange={handleChange} className="border border-slate-300 rounded px-2 py-1 mt-1 focus:outline-none focus:ring-2 focus:ring-blue-400" />
                </label>

                {renderSelect("Education", "education", EDUCATION_OPTIONS)}
                {renderSelect("Employment Type", "employment_type", EMPLOYMENT_OPTIONS)}
                {renderSelect("Marital Status", "marital_status", MARITAL_OPTIONS)}
                {renderSelect("Loan Purpose", "loan_purpose", LOAN_PURPOSE_OPTIONS)}

                <label className="flex flex-col">
                    <span className="font-bold">Has Mortgage</span>
                    <div className="flex gap-4 mt-1">
                        <label className="flex items-center gap-1">
                            <input
                            type="radio"
                            name="has_mortgage"
                            value="1"
                            checked={formData.has_mortgage === "1"}
                            onChange={handleChange}
                            />
                            Yes
                        </label>
                        <label className="flex items-center gap-1">
                            <input
                            type="radio"
                            name="has_mortgage"
                            value="0"
                            checked={formData.has_mortgage === "0"}
                            onChange={handleChange}
                            />
                            No
                        </label>
                    </div>
                </label>

                <label className="flex flex-col">
                    <span className="font-bold">Has Dependents</span>
                    <div className="flex gap-4 mt-1">
                        <label className="flex items-center gap-1">
                            <input
                            type="radio"
                            name="has_dependents"
                            value="1"
                            checked={formData.has_dependents === "1"}
                            onChange={handleChange}
                            />
                            Yes
                        </label>
                        <label className="flex items-center gap-1">
                            <input
                            type="radio"
                            name="has_dependents"
                            value="0"
                            checked={formData.has_dependents === "0"}
                            onChange={handleChange}
                            />
                            No
                        </label>
                    </div>
                </label>

                <label className="flex flex-col">
                    <span className="font-bold">Has Co-Signer</span>
                    <div className="flex gap-4 mt-1">
                        <label className="flex items-center gap-1">
                            <input
                            type="radio"
                            name="has_co_signer"
                            value="1"
                            checked={formData.has_co_signer === "1"}
                            onChange={handleChange}
                            />
                            Yes
                        </label>
                        <label className="flex items-center gap-1">
                            <input
                            type="radio"
                            name="has_co_signer"
                            value="0"
                            checked={formData.has_co_signer === "0"}
                            onChange={handleChange}
                            />
                            No
                        </label>
                    </div>
                </label>

                <div className="md:col-span-2 flex justify-center mt-4">
                    <button type="submit" className="px-6 py-3 bg-blue-700 text-white rounded-xl hover:bg-blue-800 font-semibold">
                    Predict
                    </button>
                </div>
            </form>

            {/*Prediction Result div*/}
            {result && (
                <div className="mt-8 bg-white p-6 rounded-xl shadow text-center max-w-xl">
                    <h2 className="text-xl font-semibold text-blue-700 mb-2">Prediction Result</h2>
                    <p className="text-lg">
                        This applicant is predicted to be <strong className={result.prediction === 1 ? "text-red-700" : "text-green-700"}>
                            {result.prediction === 1 ? 'High Risk' : 'Low Risk'}
                        </strong>.
                    </p>
                    <p className="text-gray-600 mt-2">
                        Probability of default: {(result.probability * 100).toFixed(2)}%
                    </p>
                </div>
            )}
        </div>
    )
}

export default FormPage