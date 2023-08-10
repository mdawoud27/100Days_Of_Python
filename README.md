# 100Days_Of_Python

Welcome to the **100Days_Of_Python** repository! This is a collection of my journey through 100 days of Python programming, where I will be working on various projects, exercises, and challenges to improve my Python skills.

## Table of Contents

- [About](#about)
- [Projects](#projects)
- [Challenges](#challenges)
- [Progress](#progress)
- [Resources](#resources)
- [Scripting Files I used](#scripting)

## About

This repository documents my commitment to dedicate 100 days to improving my Python programming skills. Each day, I will work on coding exercises, projects, or challenges related to Python. The purpose of this challenge is to learn, practice, and have fun with Python.

## Projects

Throughout this challenge, I will be working on a variety of Python projects. These projects will cover different areas of Python programming, such as web development, automation, and more. Check out each day to see the Day Project.

## Challenges

In addition to projects, I will take on coding challenges and exercises to strengthen my problem-solving abilities and deepen my understanding of Python. These challenges may range from simple coding tasks to more complex algorithmic problems and so on.

## Progress

I will update my progress regularly. Each day's progress will be documented in the day `README.md` file, including the tasks I worked on, challenges I completed, and any new concepts I learned. This section will serve as a log of my journey through the 100 days of Python.

## Resources

Throughout this challenge, I will be using a variety of resources to learn and improve my Python skills. Some of the resources I will be referring to include:

- Online tutorials and courses
- Python documentation
- Coding platforms for challenges and exercises

## Scripting

*To automate some of my work*

- `execute` to give permissions to the file either in the current dir or in a sub.
    ``` bash
      #!/bin/bash
      find . -type f -name "*.py" -exec chmod +x {} \;    
    ```
    
- `push` file to automate uploading files to the remote server.
    ``` bash
      #!/bin/bash
      git add .
      git commit -m "${*:1}"
      git push origin main
    ```
---

Thank you for joining me on this Python journey! If you have any questions, suggestions, or just want to say hi, feel free to reach out.
