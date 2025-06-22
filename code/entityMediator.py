from code.enemy import Enemy
from code.entity import Entity


class EntityMediator: #design pattern factory doesnt need a init
    

    @staticmethod 
    #method to verify if the entity is out of the screen, if so, it will set the health to 0
    def __verify_collision_window(ent: Entity): #private method that just works inside this class
        if isinstance(ent, Enemy):
            if ent.rect.right < 0:
                ent.health = 0
        

    @staticmethod
    def verify_collision(entity_list: list[Entity]):
        for i in range(len(entity_list)):
            test_entity = entity_list[i]
            EntityMediator.__verify_collision_window(test_entity)

    @staticmethod
    #method to verify the health of the entities, if the health is 0 or less, it will remove the entity from the list (destroy the entity)
    def verify_health(entity_list: list[Entity]):
        for ent in entity_list:
            if ent.health <= 0:
                entity_list.remove(ent)
