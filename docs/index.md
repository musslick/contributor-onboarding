# Basic Tutorial for Open Source Development on GitHub

## Requirements

### General Requirements

Software development is a team effort. Each team member has a role to play in the development process. 
Here, we will simulate a software development team as you may find it both in industry or academia. 
The team consists of a team leader and team members. 
The team leader is responsible for setting up and managing the repository.

**Sections marked with an asterix (*)** are meant to be executed only by the team leader. These sections typically involve 
one-time tasks, such as setting up a branch protection rule. 
If you choose to mirror the practice repo instead of forking it (see below), you can rotate the team leader role every
time an Asterix appears in the documentation. It is recommended that the first team leader is the one who is most 
experienced with git. 

### Technical Requirements

Each student in the group should meet the following requirements:

#### Required
- A [Github account](https://github.com/join).
- [Git](https://git-scm.com/downloads) installed on your computer.
- [Python3](https://www.python.org/downloads/) installed on your computer

#### Recommended:
- [GitHub Desktop](https://desktop.github.com/download/) installed on your computer
- [Pycharm Community Edition](https://www.jetbrains.com/pycharm/download/other.html]) installed on your computer


## * Create a repository

First, we need to create a repository for subsequent exercises in which we 
can practice open-source software development as a team. 

There are two options here:

### Option 1: Mirroring the Practice Repository

Here, we create a simple copy of the practice repo by mirroring it. 
The team leader will have to execute the following steps on their machine:

1. **Create a new repository on GitHub:**
   Go to your GitHub account and create a new repository. Don't add any README or license, just add an empty repository.
   Name the repository `contributor-onboarding`.

2. **Clone the original repository to your local machine:**
   Open your terminal or command prompt and run the following command to clone the repository:

   ```sh
   git clone https://github.com/AutoResearch/contributor-onboarding.git
   ```

3. **Change into the cloned repository directory:**
   ```sh
   cd contributor-onboarding
   ```

4. **Remove the original remote (optional, but recommended to avoid confusion):**
   ```sh
   git remote remove origin
   ```

5. **Add your own repository as the new remote:**
   ```sh
   git remote add origin https://github.com/YOURGITHUBUSERNAME/contributor-onboarding.git
   ```

6. **Push the code to your own repository:**
   ```sh
   git push -u origin main
   ```

   If your repository uses a different branch name, replace `main` with the correct branch name.

### Option 2: Forking the Practice Repository (Preferred)

*Note: If you choose this option, other members of the team will be able to contribute to the working repository 
but do not have the ability to manage the repository settings. There are a number of *

Here, we mimic a practice in 
open-source development where there is some existing project (https://github.com/AutoResearch/contributor-onboarding) and
we want to contribute to a major feature as a team. To do that, we'll have to fork the repo, i.e., create our
own copy of it which is linked to the original project.

1. Go to the repository you want to fork: https://github.com/AutoResearch/contributor-onboarding
2. Click the "Fork" button in the upper right corner of the page.
3. Select your username as the destination for the fork.
4. You may add a description to the fork if you wish.
5. Check the box "Copy the ``main`` branch only".
6. Click the "Create Fork" button.
4. You now have a copy of the repository in your account.

### Add Contributors to the Repository

As a next step we will add all students in the team as contributors. 
You will need the GitHub usernames of all students in your team.

1. Go to the repository on GitHub you want to add contributors to. This is the repository you just created.
2. Click the "Settings" tab.
3. Click the "Manage access" button.
4. Click the "Invite a collaborator" button.
5. Enter the username of the person you want to add as a contributor.
7. Note: For this exercise, you will want to give the person "Maintain" access. However, if you are on a forked repo, you may not have that option.
8. Click the "Add [username] to this repository" button.
9. The person you added will receive an email invitation to contribute to the repository.
10. Once they accept the invitation, they will be able to contribute to the repository.

*Hint: You can also add contributors by adding their GitHub username to the `CONTRIBUTORS.md` file in the repository.*

## Cloning a Repository to Your Local Machine

### Option 1: Cloning with GitHub Desktop

*Note: You may have to log into your GitHub account from GitHub Desktop before you can clone a repository. 
You may also need to give GitHub Desktop permission to access your GitHub account.* 

1. Open GitHub Desktop.
2. Click the "File" menu and select "Clone Repository".
3. Select the "URL" tab.
4. Paste the URL of the repository you want to clone.
5. Choose a local path for the repository.
6. Click the "Clone" button.
7. You now have a copy of the repository on your computer.

### Option 2: Cloning with git
1. Open a terminal.
2. Navigate to the directory where you want to clone the repository.
3. Run the following command:
```bash
git clone repository_url
```
4. You now have a copy of the repository on your computer.

### Option 3: Open the repository in GitHub Codespaces (Preferred)
1. Open the forked repository (the one you created)
2. Click on the green button "Code"
3. Click on "Open in codespaces"

## Create a Virtual Environment

It is a good practice to create a virtual environment for each project you work on.
This ensures that the dependencies for each project are isolated from each other.
Here, we will create a virtual environment for the project in Python.

1. Open a terminal.
2. Navigate to the directory where you cloned the repository.
3. Run the following command to create a virtual environment:
```bash
python3.9 -m venv venv
```
Note: if this doesn't work, try 
```bash
python -m venv venv
```

4. Activate the virtual environment:
```bash
source venv/bin/activate
```
5. You should see `(venv)` in your terminal prompt, indicating that the virtual environment is active.
6. Upgrade pip
```bash
pip install --upgrade pip
```
7. Install the project dependencies:
```bash
pip install --upgrade --editable ".[dev]"
```

Now you can use this environment to run code for your project in PyCharm. 
Note that you will want to configure PyCharm to use this environment for your project.


## Have a look at the repository

Next, all students should have a look at the repository. The main code is in the `src` directory.

## Managing Issues

Issues are a way to track tasks, enhancements, and bugs for your repository. 
You might have noticed that the code in the existing repository has a number of issues.
Let's go ahead and enlist them. But first, you have to enable issues in your repository.

### * Enable Issues

1. Go to the repository on GitHub you just created.
2. Click the "Settings" tab.
3. Scroll down to the "Features" section.
4. Check the box "Issues".

### Create An Issue

Now, let's create some issues for the repository.

1. Go to the repository on GitHub.
2. Click the "Issues" tab.
3. Click the "New issue" button.'
4. Enter a title and description for the issue.
5. You may also enter labels and assignees if you wish.
6. Click the "Submit new issue" button.

Here are some examples but feel free to create your own. 
You may use some of the TODO comments in the code as inspiration:
- the sum function does not work with float variables
- the divide function doesn't check for zero division
- the element-wise multiplication function doesn't check for vector shape compatibility
- ...

## Addressing Issues Through Pull Requests

Now that you have created some issues, it's time to address them.
But we don't want to address them in the main branch directly. 
In fact, we want to protect the main branch from direct pushes so that 
all changes are made through pull requests. This ensures that all changes are reviewed before 
they are merged into the main branch.

### *Adding Branch Protection Rules
1. Go to the repository on GitHub you want to add branch protection rules to. This is the repository you just forked.
2. Click the "Settings" tab.
3. Click the "Branches" tab.
4. Click the "Add classic branch protection rule" link.
5. Enter the name of the branch you want to protect. For this exercise, you will want to protect the ``main`` branch.
6. Check the box "Require pull request reviews before merging".
7. Check the box "Require approvals".
8. Enter the number of approvals required. For this exercise, you will want to require two approvals.

### Create a Branch for Your Issue

Students should now assign themselves to issues (ideally one student per issue). 
Each student should then create a new branch for their issue:

#### Option 1: Via GitHub Desktop

1. Open GitHub Desktop.
2. Click the "Current Repository" menu and select the repository you want to work on.
3. Click the "Current Branch" dropdown.
4. Click the "New Branch" button.
5. Enter a name for your branch (e.g., `fix/sum-function`).
6. Click the "Create Branch" button.

#### Option 2: Via GitHub Repository Page

1. Go to the repository on GitHub.
2. Click the "Code" tab.
3. Click the "main" branch dropdown.
4. Enter a name for your branch (e.g., `fix/sum-function`).
5. Click the "Create branch" button.

#### Option 2: Via GitHub Issues (Preferred)
1. Go to the repository on GitHub.
2. Click the "Issues" tab.
3. Click the issue you want to address.
4. In the right column, under "Development", click "Create a branch".
 
### Fix the Issue

Now, students should fix the issue in their branch.

### Commit Changes to Your Branch

Once the issue is fixed, students should commit their changes to their branch.

#### Option 1: Via GitHub Desktop

1. Open GitHub Desktop.
2. Click the "Current Repository" menu and select the repository you want to work on.
3. Click the "Current Branch" dropdown.
4. Select the branch you want to commit to.
5. Make your changes in the code.
6. Click the "Commit to main" button.
7. Enter a summary and description for the commit.
8. Click the "Commit to main" button.

#### Option 2: Git

1. Open a terminal.
2. Navigate to the repository directory.
3. Run the following command to stage your changes:
```bash
git add name_of_fixed_file
```
4. Run the following command to commit your changes:
```bash
git commit -m "description of fix"
```

### Push Changes to Your Branch

Once the changes are committed, students should push their branch to the repository.

#### Option 1: Via GitHub Desktop

1. Open GitHub Desktop.
2. Click the "Current Repository" menu and select the repository you want to work on.
3. Click the "Current Branch" dropdown.
4. Select the branch you want to push.
5. Click the "Push origin" button.

#### Option 2: Git

1. Open a terminal.
2. Navigate to the repository directory.
3. Run the following command to push your branch:
```bash
git push origin name_of_your_branch
```

### Create a Pull Request (PR)

Once the issue is fixed, students should create a pull request to merge their branch into the main branch.

#### PR Via GitHub Desktop

1. Open GitHub Desktop.
2. Click the "Current Repository" menu and select the repository you want to work on.
3. Click the "Current Branch" dropdown.
4. Select the branch you want to merge into the main branch.
5. Click the "Pull Request" button.

#### PR Via GitHub

1. Go to the repository on GitHub.
2. Click the "Pull requests" tab.
3. Click the "New pull request" button.
4. Select the branch you want to merge into the main branch. IMPORTANT: Do not select the original repository but your own (the fork). 
5. Enter a title and description for the PR.
6. Fill out the PR template.
7. Assign reviewers to the PR.
6. Click the "Create pull request" button.


## Code Reviews

Once a pull request (PR) is created, other students should review the code changes.
Each PR should have at least two reviewers. You can assign reviewers in the PR itself.

### Reviewing a PR

1. Go to the repository on GitHub.
2. Click the "Pull requests" tab.
3. Click the PR you want to review.
4. Review the changes in the PR.
5. Add comments to the PR if you have any feedback.

If you are satisfied with the changes, you can approve the PR.

6. Click the "Approve" button.
7. You may add any additional comments, e.g., congratulate them on the great code they wrote.

If you are concerned about the changes, you can request changes from the author.

6. Click the "Request changes" button.
7. Enter a reason for the requested changes.

Once all reviewers have approved the PR, the author can merge the PR into the main branch.

## Unit Tests

Unit tests are a way to ensure that your code works as expected.

### Writing Unit Tests

First, create an issue for a test you want to add. Then follow the procedure above (create a branch for the issue, then checkout that branch). 

To write a unit test, you need to create a new file in the `tests` directory with the name `test_<module>.py`, 
where `<module>` is the name of the module you want to test. See the example in the repo. 

You may want to create some more issues to propose individual tests. 

Follow the PR process above to then add those tests.

## Automated Testing

Writing tests is great, but running them manually can be time-consuming.
Ideally, we should run all tests automatically whenever a new change is proposed to the codebase.

### *Enable Automated Testing

The first thing we need to do is to enable automated testing in the repository.

1. To enable automated unit tests, go to the repository on GitHub.
2. Click the "Actions" tab.
3. Click the "I understand workflows, go ahead and enable them" button.

### Add the Test Workflow

Now, we need to add a test workflow to the repository. 
To do this, simply rename the ``test-pytest.yml.disabled`` file in the ``.github/workflows`` 
directory to ``test-pytest.yml``.

Of course, this should be done via a PR and code review.

Once the test workflow is enabled, all tests will run automatically whenever a new PR is created.

## Automated Documentation

Documentation is an important part of any software project. You may have noticed a folder in your repository
called `docs`. This folder contains the documentation for the project.

Here, we will enable automated documentation generation using mkdocs. We will automatically generate a documentation
every time a code is pushed to the main branch.

1. First, we want to add the relevant GitHub username to the ``mkdocs.yml`` file:
```
repo_url: 'https://github.com/GITHUBUSERNAME/contributor-onboarding'
```

2. Now we want to enable the publication workflow. 
You can do this by changing the name of the file ``docs-publish.yml.disabled`` in the ``.github/workflows`` 
directory to ``docs-publish.yml``.

3. Now we want to update the documentation links for our project in the ``pyproject.toml`` file. 
To do this, add the corresponding GitHub repository link to the ``documentation`` section of the file.
```
[project.urls]
repository = "https://github.com/GITHUBUSERNAME/contributor-onboarding"
documentation = "https://GITHUBUSERNAME.github.io/contributor-onboarding/"
```

4. Finally, we need to make sure the documentation can be built in the repository. 
To do this, navigate to the Settings -> GitHub Pages. For "Source", select "Deploy from Branch". 
For "Branch", select "gh-pages". Click "Save".


## Publishing your Package on PyPi

Here, we will simulate how to publish your code as an actual PyPi package.
However, we will not actually publish the code to PyPi, but rather to the test PyPi server.

1. The owner of the GitHub repository should first create a PyPi account.
They then need to create a PyPi API token.

2. Next they need to add the token as a secret in the GitHub repository..
   - Navigate to your GitHub repository.
   - Go to `Settings` > `Secrets and variables` > `Actions`.
   - Click `New repository secret`.
   - Add a new secret with the name `TEST_PYPI_API_TOKEN` and the value of your Test PyPI token.

3. Now, we need to enable the publication workflow. 
You can do this by changing the name of the file ``python-publish.yml.disabled`` in the ``.github/workflows``
directory to ``python-publish.yml``.

4. Now, you can create a new release in the repository. 
   - Go to the repository on GitHub.
   - Click the "Releases" tab.
   - Click the "Draft a new release" button.
   - Enter a tag version (e.g., v0.1.0).
   - Enter a title and description for the release.
   - Click the "Publish release" button.

**Congratulations, you published your first pip package!**




