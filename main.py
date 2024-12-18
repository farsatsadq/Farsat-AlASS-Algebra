import tkinter as tk
from tkinter import messagebox
from owlready2 import get_ontology, Thing

# Load the OWL ontology
ontology_path = "CodeOntology.owl"
ontology = get_ontology(ontology_path).load()


# Create a class for questions, feedback, etc., based on the ontology
class AlgebraApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Algebra Learning App")

        # Set up question, answer, and feedback attributes
        self.question_label = tk.Label(self.root, text="Solve for x: 2x + 4 = 0", font=('Arial', 14))
        self.question_label.pack(pady=20)

        self.answer_entry = tk.Entry(self.root, font=('Arial', 14))
        self.answer_entry.pack(pady=10)

        self.submit_button = tk.Button(self.root, text="Submit", font=('Arial', 14), command=self.check_answer)
        self.submit_button.pack(pady=20)

        # This variable will be used to keep track of the current question
        self.current_question = self.load_question()

    def load_question(self):
        # Example logic to load a simple algebra question based on the ontology
        # In the ontology, you could store equations as instances of `ex:LinearEquation` and give them corresponding coefficients and constants.

        question = ontology.ex.Equation1  # Example: Get a linear equation from the ontology

        coefficient = question.hasCoefficient[0]
        constant = question.hasConstant[0]
        variable = question.hasVariable[0]

        # Construct a question (for simplicity, just a static question here)
        question_text = f"Solve for {variable} in the equation: {coefficient}x + {constant} = 0"

        self.question_label.config(text=question_text)

        # Return the relevant data for checking the answer
        return {
            "coefficient": coefficient,
            "constant": constant,
            "variable": variable
        }

    def check_answer(self):
        # Get the entered answer
        answer = self.answer_entry.get().strip()

        try:
            # Check if the answer is correct (for simplicity, let's assume the answer is numeric and check it)
            coefficient = self.current_question["coefficient"]
            constant = self.current_question["constant"]

            # Solve the equation: coefficient * x + constant = 0
            correct_answer = -constant / coefficient

            # Check the student's answer
            if float(answer) == correct_answer:
                messagebox.showinfo("Correct!", "Well done! That's the correct answer.")
                self.current_question = self.load_question()  # Load the next question
                self.answer_entry.delete(0, tk.END)  # Clear the answer field
            else:
                messagebox.showwarning("Try Again", "Incorrect. Please try again.")
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid number.")


# Main loop to run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = AlgebraApp(root)
    root.mainloop()
