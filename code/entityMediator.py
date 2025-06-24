import pygame
from code.const import HIT_COOLDOWN, WIN_WIDTH
from code.enemy import Enemy
from code.enemyShot import EnemyShot
from code.entity import Entity
from code.player import Player
from code.playerShot import PlayerShot


class EntityMediator: #design pattern factory doesnt need a init
    

    @staticmethod 
    #method to verify if the entity is out of the screen, if so, it will set the health to 0
    def __verify_collision_window(ent: Entity): #private method that just works inside this class
        if isinstance(ent, Enemy):
            if ent.rect.right < 0:
                ent.health = 0
        if isinstance(ent, PlayerShot):
            if ent.rect.left >= WIN_WIDTH:
                ent.health = 0
        if isinstance(ent, EnemyShot):
            if ent.rect.right < 0:
                ent.health = 0
            
    @staticmethod
    def __verify_collision_entity(ent1, ent2):
        hit_cooldown = HIT_COOLDOWN
        # Check if the entities are of types that can interact with each other
        valid_interaction = False #flag to check if the collision is valid
        if isinstance(ent1, Enemy) and isinstance(ent2, PlayerShot):
            valid_interaction = True
        elif isinstance(ent1, PlayerShot) and isinstance(ent2, Enemy):
            valid_interaction = True
        elif isinstance(ent1, EnemyShot) and isinstance(ent2, Player):
            valid_interaction = True
        elif isinstance(ent1, Player) and isinstance(ent2, EnemyShot):
            valid_interaction = True
        elif isinstance(ent1, Player) and isinstance(ent2, Enemy):
            hit_cooldown -= 1
            if hit_cooldown == 0:
                hit_cooldown == HIT_COOLDOWN
                valid_interaction = True
        elif isinstance(ent1, Enemy) and isinstance(ent2, Player):
            hit_cooldown -= 1
            if hit_cooldown == 0:
                hit_cooldown == HIT_COOLDOWN
                valid_interaction = True
        

        
        # Check if the entities are colliding
        if valid_interaction: #== True:
            if (ent1.rect.right >= ent2.rect.left and 
                ent1.rect.left <= ent2.rect.right and 
                ent1.rect.bottom >= ent2.rect.top and 
                ent1.rect.top <= ent2.rect.bottom):
                # If they are colliding, reduce their health by their respective damage
                ent1.health -= ent2.damage
                ent2.health -= ent1.damage
                
                # set the last damage source for both entities
                ent1.last_dmg = ent2.name
                ent2.last_dmg = ent1.name

                


    @staticmethod
    def __give_score(enemy: Enemy, entity_list: list[Entity]):
        if enemy.last_dmg == 'Player1_DLCShot':
            for ent in entity_list:
                if ent.name == 'Player1_DLC':
                    ent.score += enemy.score
        elif enemy.last_dmg == 'Player2_DLCShot':
            for ent in entity_list:
                if ent.name == 'Player2_DLC':
                    ent.score += enemy.score

    @staticmethod
    def verify_collision(entity_list: list[Entity]):
        for i in range(len(entity_list)):
            entity1 = entity_list[i]
            EntityMediator.__verify_collision_window(entity1)
            for j in range(i+1, len(entity_list)): #using i+1 to avoid checking the same pair twice (reduce redundant checks)
                entity2 = entity_list[j]
                EntityMediator.__verify_collision_entity(entity1, entity2)

    @staticmethod
    #method to verify the health of the entities, if the health is 0 or less, it will remove the entity from the list (destroy the entity)
    def verify_health(entity_list: list[Entity]):
        hit_sound = pygame.mixer.Sound('./asset/Sound_hit.wav') # Load the shot sound for the player
        hit_sound.set_volume(0.3)


        for ent in entity_list:
            if isinstance(ent, (Player, Enemy)): #define a tuple of types to check if the entity is a Player or an Enemy to make a sound
                if ent.health <= 0:
                    hit_sound.play()
                    if isinstance(ent, Enemy):
                        EntityMediator.__give_score(ent, entity_list)

                    entity_list.remove(ent)
            elif ent.health <= 0:
                entity_list.remove(ent)
