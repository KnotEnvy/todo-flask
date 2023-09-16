### Flask Todo App

A sleek and responsive Todo list application built using Flask, perfect for jotting down tasks and ensuring productivity.

<video width="630" height="300" src="https://youtube.com/shorts/hiUC6bZa_Ck"></video>

#### Features

- 📝 Easily add new todos.
- ✏️ Update todos as tasks evolve.
- ❌ Remove todos once completed.
- 📱 Fully responsive - works on both desktop and mobile.
- 🎨 Clean and intuitive design.

#### Technologies Used

- [Flask](https://flask.palletsprojects.com/en/2.0.x/) - Lightweight web application framework.
- [SQLAlchemy](https://www.sqlalchemy.org/) - The Python SQL toolkit and Object-Relational Mapping (ORM) library.
- [WTForms](https://wtforms.readthedocs.io/en/2.3.x/) - A flexible forms validation and rendering library.
- [Bootstrap](https://getbootstrap.com/) - Open-source CSS framework directed at responsive, mobile-first front-end web development.

#### Installation & Setup

1. **Clone the repository**:
    ```bash
    git clone https://github.com/KnotEnvy/todo-flask.git
    cd todo-flask
    ```

2. **Set up a virtual environment** (This helps to keep dependencies properly organized):
    ```bash
    python3 -m venv venv_name
    source venv_name/bin/activate  # macOS/Linux
    venv_name\Scripts\activate  # Windows
    ```

3. **Install the required dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Run the app**:
    ```bash
    flask run
    ```

5. **Access the app in your browser**:
   - Once the server is running, open your favorite browser.
   - Navigate to `http://127.0.0.1:5000/` to access the app.

6. **Exiting the app**:
   - To stop the server, in your terminal, simply press `CTRL + C` (or `Cmd + C` on macOS).

7. **Deactivate the virtual environment**:
    ```bash
    deactivate
    ```

#### Contributing

Your contributions are always welcome! If you want to collaborate:

1. Fork the repo: `https://github.com/KnotEnvy/todo-flask/fork`
2. Clone your fork and create a new branch: 
    ```bash
    git clone https://github.com/your_username/todo-flask.git
    cd todo-flask
    git checkout -b name_for_new_branch
    ```
3. Make your contribution and commit your changes: `git commit -m 'Add your feature'`
4. Push to the branch: `git push origin name_for_new_branch`
5. Submit a pull request.

#### License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.
