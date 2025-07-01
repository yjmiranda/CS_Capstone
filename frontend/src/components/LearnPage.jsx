import React from 'react';
import { Link } from 'react-router-dom';

function LearnPage() {
    return (
        <div className="min-h-screen bg-slate-50 text-gray-800 px-4 py-10 flex flex-col items-center">
            <div className="w-full max-w-4xl">
                <h1 className="text-3xl font-bold text-blue-900 mb-6 text-center">
                    How the Model Works
                </h1>

                {/* Credit Score Insight */}
                <section className="mb-12">
                    <h2 className="text-2xl font-semibold mb-2">Credit Score and Default Risk</h2>
                    <p className="mb-4">
                        The chart below shows the correlation between credit score ranges and default rates.
                        While there is a clear trend indicating that lower credit scores are associated with a higher likelihood of default,
                        credit score alone does not tell the full story. There are many cases where borrowers with lower scores successfully repay their loans — and vice versa.
                    </p>
                    <img src="http://localhost:8000/api/visuals/default_rates_by_credit_score.png" alt="Credit Score vs Default" className="rounded shadow-md w-full" />
                </section>

                {/* Feature Importance */}
                <section className="mb-12">
                    <h2 className="text-2xl font-semibold mb-2">What Features Matter Most?</h2>
                    <p className="mb-4">
                        While credit score often dominates traditional risk models, our machine learning model tells a different story.
                        In fact, <strong>credit score</strong> ranks only <strong>7th</strong> in importance. Instead, the model relies more heavily on a combination of financial and structural factors such as:
                        <strong> Age</strong>, <strong>Interest Rate</strong>, <strong>Loan Term</strong>, <strong>Income</strong>, and <strong>Months Employed</strong>.
                    </p>
                    <p className="mb-4">
                        These features provide a broader and more nuanced view of borrower risk. For example, loan applicants with shorter terms and higher interest rates tend to be more likely to default — regardless of credit score alone.
                    </p>
                    <p className="mb-4">
                        Features with the least influence included <strong>Employment Type</strong>, <strong>Number of Credit Lines</strong>, and <strong>Marital Status</strong>,
                        although these still contribute supporting context to the model's decision-making.
                    </p>
                    <img src="http://localhost:8000/api/visuals/feature_importance_bar_chart.png" alt="Feature Importance Bar Chart" className="rounded shadow-md w-full" />
                </section>

                {/* Model Reliability */}
                <section className="mb-12">
                    <h2 className="text-2xl font-semibold mb-2">How Accurate Is the Model?</h2>

                    <p className="mb-4">
                        To evaluate the reliability of our machine learning model, we use a <strong>confusion matrix</strong> — a breakdown of predicted vs. actual outcomes. It divides results into:
                        <strong> true positives</strong> (correctly predicted defaults),
                        <strong> true negatives</strong> (correctly predicted non-defaults),
                        <strong> false positives</strong> (non-defaults incorrectly labeled as defaults),
                        and <strong> false negatives</strong> (missed defaults).
                    </p>

                    <img src="http://localhost:8000/api/visuals/random_forest_confusion_matrix.png" alt="Confusion Matrix" className="rounded shadow-md w-full" />

                    <p className="mt-4">
                        The confusion matrix shown reflects performance on a model trained with 70% of the available data:
                    </p>
                    <ul className="list-disc list-inside mt-2 space-y-1 text-gray-700">
                        <li><strong>True Negatives:</strong> 50,366</li>
                        <li><strong>True Positives:</strong> 4,672</li>
                        <li><strong>False Positives:</strong> 17,415</li>
                        <li><strong>False Negatives:</strong> 4,152</li>
                    </ul>

                    <p className="mt-4">
                        This corresponds to the following performance metrics:
                    </p>
                    <ul className="list-disc list-inside mt-2 space-y-1 text-gray-700">
                        <li><strong>Accuracy:</strong> 72%</li>
                        <li><strong>Precision:</strong> 0.21</li>
                        <li><strong>Recall:</strong> 0.53</li>
                        <li><strong>F1 Score:</strong> 0.30</li>
                    </ul>

                    <p className="mt-4">
                        These results reflect a strategic balance: while the model does generate more false positives,
                        it successfully identifies over half of all potential defaults — a major improvement over earlier versions.
                        In financial settings like ours, this tradeoff is valuable: catching high-risk borrowers is a higher priority than mistakenly flagging some low-risk applicants.
                    </p>

                    <p className="mt-4">
                        To achieve this balance, we used SMOTE (Synthetic Minority Oversampling) to improve how the model learns from rare default cases,
                        and adjusted the decision threshold to better align with business goals.
                    </p>

                    <p className="mt-4">
                        The version of the model actively used in this application has been retrained using 100% of the available data to maximize learning for live predictions.
                        However, the performance metrics shown here (based on a held-out test set) remain the most reliable indicators of expected behavior.
                    </p>

                    <p className="mt-4">
                        In the future, we aim to further improve performance by exploring more advanced algorithms such as XGBoost or LightGBM, and by incorporating a broader range of real-world lending data.
                    </p>
                </section>

                {/* Navigation */}
                <div className="text-center">
                    <Link to="/" className="text-blue-700 hover:underline font-medium">
                        &larr; Back to Home
                    </Link>
                </div>
            </div>
        </div>
    );
}

export default LearnPage;
