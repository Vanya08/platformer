import os

game_folder = os.path.dirname(__file__)
resource_folder = os.path.join(game_folder, "resources")
image_folder = os.path.join(resource_folder, 'image') 
player_image = os.path.join(image_folder, 'player.png')
enemy_image = os.path.join(image_folder, 'enemy.png')
bullet_image = os.path.join(image_folder, 'Bullet.png')
level1_image = os.path.join(image_folder, 'level1.gif')