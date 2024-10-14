window.addEventListener("load", () => {
  // Start the game
  if (document.getElementById("game-start")) {
    // If Play! button exists?
    let game_settings;
    localStorage.setItem("userInput", "");
    localStorage.setItem("attempts", 0);

    // start the game..
    const playBtn = document.getElementById("game-start");
    // check if the game is Math Facts..
    // save the game settings to user local storage.
    if (gameType == "math_facts") {
      const operation = document.getElementById("operation");
      const maxNum = document.getElementById("max-number");

      // Get the selected value from the operation dropdown
      localStorage.setItem(
        "operation",
        operation.options[operation.selectedIndex].value
      );
      operation.addEventListener("change", (e) => {
        localStorage.setItem("operation", e.target.value);
      });
      // Get the value from the max-number input
      localStorage.setItem("maxValue", maxNum.value);
      maxNum.addEventListener("change", (e) => {
        localStorage.setItem("maxValue", e.target.value);
      });
    }
    // check if the game is Anagram Hunt..
    // save the game settings to user local storage.
    if (gameType == "anagram_hunt") {
      const wordLength = document.getElementById("word-length");
      // Get the selected value from the word length dropdown
      localStorage.setItem(
        "wordLength",
        wordLength.options[wordLength.selectedIndex].value
      );
      wordLength.addEventListener("change", (e) => {
        localStorage.setItem("wordLength", e.target.value);
      });
    }

    playBtn.addEventListener("click", () => {
      initialGame(gameType);
    });
  }
});

// this function to initial the game.
function initialGame(gameType) {
  let game_settings;

  if (gameType == "math_facts") {
    game_settings = mathSettings();
  }
  if (gameType == "anagram_hunt") {
    game_settings = anagramSettings();
  }
  // a function to startGame to save the basic data to admin..
  startGame(game_settings);
}

// this function to get the csrf token.
function getToken() {
  const csrfInput = document.querySelector("input[name='csrfmiddlewaretoken']");
  const csrfToken = csrfInput.value;
  return csrfToken;
}

function startGame(settings) {
  const csrfToken = getToken();

  const data = {
    game_type: gameType,
    game_settings: settings,
  };

  fetch(ajaxStartURL, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "X-CSRFToken": csrfToken,
    },
    body: JSON.stringify(data),
  })
    .then((response) => response.json())
    .then((data) => {
      const gameId = data.game_id; // Store the game ID
      localStorage.setItem("gameId", gameId);
      updateGame(gameId);
      setTimeout(function () {
        endGame(gameId);
      }, 60000);
    });
}

function updateGame(gameId) {
  if (localStorage.getItem("gameId") == gameId) {
    if (gameType == "math_facts") {
      // listner to check user tries..
      let userInput = "";
      document.querySelectorAll(".btn-game").forEach((btn) => {
        btn.addEventListener("click", function () {
          const answer = localStorage.getItem("question");

          const value = this.getAttribute("data-value");
          userInput += value; // Append the value to the current input

          if (userInput.length >= answer.length) {
            checkAnswer(userInput, answer);
            userInput = "";
            // update the user attempts
            updateAttempts(gameId);
          }
        });
      });

      // Event listener for clearing the input
      document.getElementById("clear").addEventListener("click", function () {
        localStorage.setItem("userInput", "");
      });
    }
    // word-guess the id of ol has correct guesses.
  }
}

function updateAttempts(gameId) {
  const attempts = localStorage.getItem("attempts");
  const csrfToken = getToken();

  if (localStorage.getItem("gameId") == gameId) {
    const data = {
      gameId: gameId,
      tries: attempts,
    };
    fetch(ajaxUpdateURL, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "X-CSRFToken": csrfToken,
      },
      body: JSON.stringify(data),
    })
      .then((response) => response.json())
      .then((data) => {
        const gameId = data.game_id; // Store the game ID
        localStorage.setItem("gameId", gameId);
      });
  }
}

function endGame(gameId) {
  if (document.getElementById("game-score")) {
    const csrfToken = getToken();
    const gameScoreEl = document.getElementById("game-score");
    const score = gameScoreEl.innerText || gameScoreEl.textContent;
    if (localStorage.getItem("gameId") == gameId) {
      const data = {
        gameId: gameId,
        score: score,
      };
      fetch(ajaxEndURL, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          "X-CSRFToken": csrfToken,
        },
        body: JSON.stringify(data),
      })
        .then((response) => response.json())
        .then((data) => {
          const gameId = data.game_id; // Store the game ID
          localStorage.setItem("gameId", gameId);

          if (document.getElementById("play-again")) {
            const playAgainBtn = document.getElementById("play-again");
            playAgainBtn.addEventListener("click", () => {
              resetGame(); // reset the game
              initialGame(gameType); // initial the game
            });
          }
        });
    }
  }
}

// Function to extract the question and calculate the correct answer
function getQuestionAnswer() {
  const questionText = document.getElementById("question").textContent.trim();

  // Extract numbers and operation using regex
  const pattern = questionText.match(/(\d+)\s*([\+\-\*\/])\s*(\d+)/);
  if (pattern) {
    const num1 = parseInt(pattern[1], 10);
    const operator = pattern[2];
    const num2 = parseInt(pattern[3], 10);

    // Calculate the correct answer
    return calculateAnswer(num1, operator, num2);
  }
  return null;
}

// Function to calculate the correct answer
function calculateAnswer(num1, operator, num2) {
  switch (operator) {
    case "+":
      return num1 + num2;
    case "-":
      return num1 - num2;
    case "*":
      return num1 * num2;
    case "/":
      return num1 / num2;
    default:
      return null;
  }
}

// Function to check the user's input and compare it to the correct answer
function checkAnswer(userInput, correctAnswer) {
  const userAnswer = parseInt(userInput, 10);
  // number of attempts
  let attempts = localStorage.getItem("attempts");

  if (userAnswer === parseInt(correctAnswer, 10)) {
    localStorage.setItem("question", getQuestionAnswer());
    localStorage.setItem("userInput", "");
    attempts++;
    localStorage.setItem("attempts", attempts);
  } else {
    attempts++;
    localStorage.setItem("attempts", attempts);
    localStorage.setItem("userInput", "");
  }
}

// Function to reset the game for the next round
function resetGame() {
  localStorage.setItem("attempts", 0);
  localStorage.setItem("userInput", "");
}

// this function to set the math facts settings
function mathSettings() {
  // Create the game settings object
  const settings = {
    operation: localStorage.getItem("operation"),
    max_number: localStorage.getItem("maxValue"),
  };
  // save the new question in local storage..
  localStorage.setItem("question", getQuestionAnswer());

  return settings;
}
// this function to set the anagram game settings
function anagramSettings() {
  // Create the game settings object
  const settings = {
    wordLength: localStorage.getItem("wordLength"),
  };
  return settings;
}
