## Flask Application Design

### HTML Files

**index.html**

- Purpose: The main page of the application, where users can interact with the flashcards.
- Content:
  - A header section with a title and a brief introduction to the application.
  - A form containing an input field for the Australian saying or expression, a submit button, and a result display area.
  - A section to display the translated Dutch expression.

**style.css**

- Purpose: Provides CSS styles for the application, including styling for the form, input field, submit button, and result display areas.
- Content:
  - Custom CSS styles for fonts, colors, layout, and button design.

### Routes

**@app.route('/')**

- Method: GET
- Purpose: Displays the main page with the form for inputting Australian sayings or expressions.

**@app.route('/translate', methods=['POST'])**

- Method: POST
- Purpose: Handles the form submission and translates the Australian saying or expression to Dutch.
- Returns: The translated Dutch expression, displayed on the main page.