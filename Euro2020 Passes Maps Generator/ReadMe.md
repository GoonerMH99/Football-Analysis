## Introduction 
This Project functions as a demo for a website that generates a passes map for each player in each game at the 'Euro 2020'.
This Project was mainly developed using the django tool.
## Home Page
![image](https://user-images.githubusercontent.com/101012808/214400826-9acc24fa-22e6-47bc-a0ca-d19fef122bea.png)
## Match Lineups Page
![image](https://user-images.githubusercontent.com/101012808/214401061-8ef4f9bc-3c8d-454e-a16c-d8ef262cfa42.png)
## Page to show the passes map of the selected player
![image](https://user-images.githubusercontent.com/101012808/214401332-4e37eaff-aee9-4157-bcb7-f684f0688e9d.png)
## Views python file
This file contains all the functions that get called when navigating through the website and more importantly the functions that create and plot the passes map for each selected player.
![image](https://user-images.githubusercontent.com/101012808/214404353-bf2c1317-559c-4aaf-ba2f-6f55c13daf1b.png)
## urls python file
This file is responsible for the url of each HTML page and calling the views functions that renders the desired web page.
![image](https://user-images.githubusercontent.com/101012808/214407278-96fa56f8-ea69-4fb4-a897-9054371177ac.png)

The events data of each game from the 'Euro 2020' used in this project is extracted from the 'open-data' dataset provided by 'StatsBomb' in the form of Json files containing all the events that happened on the ball during the game.
![image](https://user-images.githubusercontent.com/101012808/214411818-caa900cb-4ffa-456e-8e21-aee681835141.png)
