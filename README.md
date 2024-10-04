# django-vue-play2learn-template

A template for starting the final Play2Learn project with Django and Vue.

## How to use this template?

1. If you don't have a [GitHub](https://github.com/) account, create a new account. Otherwise, log in.
2. Go to **Use this template** and select **Create a new repository**.
   ![use template](static/read-me-images/use-template.png)
3. In the **Create a new repository** menu, name your repository, add a short description, make sure your repo is **Public** if you plan to share your work, and select **Create repository**.
   ![create repo](static/read-me-images/create-repo.png)
4. You will now need to clone this repository so that you can work with it in Visual Studio Code:
   ![clone repo](static/read-me-images/clone-repo.png)
5. Open Visual Studio Code, go to **Source Control** and select **Clone Repository**.
   ![vs-code-clone](static/read-me-images/vs-code-clone.png)
6. Paste in the copied URL and select **Clone from URL**
   ![clone from url](static/read-me-images/clone-from-url.png)
7. After you select a folder location for your new repo, open the repo in Visual Studio Code.
   ![open repo](static/read-me-images/open-repo.png)

## How to set up the repo?

1. Create a Python virtual environment and install requirements.txt.
2. Go to vue-games and run `npm install`.

## How to run the project?

1. Run `python manage.py runserver` at the root to start the Django server.
2. Run `npm run serve` at the vue-games folder to start the Vue server.
3. The Vue games will be working at:
   1. Anagram Hunt - [http://127.0.0.1:8000/anagram-hunt/](http://127.0.0.1:8000/anagram-hunt).
   2. Math Facts - [http://127.0.0.1:8000/math-facts/](http://127.0.0.1:8000/math-facts).

## More

If you want to learn more about how we integrated Vue and Django in this template, see [Connecting Django and Vue](https://www.webucator.com/article/connecting-django-and-vue/).
