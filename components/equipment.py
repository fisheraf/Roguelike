from equipment_slots import EquipmentSlots


class Equipment:
    def __init__(self, main_hand=None, off_hand=None, left_ring=None, right_ring=None):
        self.main_hand = main_hand
        self.off_hand = off_hand
        self.left_ring = left_ring
        self.right_ring = right_ring

    @property
    def max_hp_bonus(self):
        bonus = 0

        if self.main_hand and self.main_hand.equippable:
            bonus += self.main_hand.equippable.max_hp_bonus

        if self.off_hand and self.off_hand.equippable:
            bonus += self.off_hand.equippable.max_hp_bonus

        if self.left_ring and self.left_ring.equippable:
            bonus += self.left_ring.equippable.max_hp_bonus

        if self.right_ring and self.right_ring.equippable:
            bonus += self.right_ring.equippable.max_hp_bonus

        return bonus

    @property
    def power_bonus(self):
        bonus = 0

        if self.main_hand and self.main_hand.equippable:
            bonus += self.main_hand.equippable.power_bonus

        if self.off_hand and self.off_hand.equippable:
            bonus += self.off_hand.equippable.power_bonus

        if self.left_ring and self.left_ring.equippable:
            bonus += self.left_ring.equippable.power_bonus

        if self.right_ring and self.right_ring.equippable:
            bonus += self.right_ring.equippable.power_bonus

        return bonus

    @property
    def defense_bonus(self):
        bonus = 0

        if self.main_hand and self.main_hand.equippable:
            bonus += self.main_hand.equippable.defense_bonus

        if self.off_hand and self.off_hand.equippable:
            bonus += self.off_hand.equippable.defense_bonus

        if self.left_ring and self.left_ring.equippable:
            bonus += self.left_ring.equippable.defense_bonus

        if self.right_ring and self.right_ring.equippable:
            bonus += self.right_ring.equippable.defense_bonus

        return bonus

    def toggle_equip(self, equippable_entity):
        results = []

        slot = equippable_entity.equippable.slot

        if slot == EquipmentSlots.MAIN_HAND:
            if self.main_hand == equippable_entity:
                self.main_hand = None
                results.append({'dequipped': equippable_entity})
            else:
                if self.main_hand:
                    results.append({'dequipped': self.main_hand})

                self.main_hand = equippable_entity
                results.append({'equipped': equippable_entity})
        elif slot == EquipmentSlots.OFF_HAND:
            if self.off_hand == equippable_entity:
                self.off_hand = None
                results.append({'dequipped': equippable_entity})
            else:
                if self.off_hand:
                    results.append({'dequipped': self.off_hand})

                self.off_hand = equippable_entity
                results.append({'equipped': equippable_entity})
        elif slot == EquipmentSlots.LEFT_RING:
            if self.left_ring == equippable_entity:
                self.left_ring = None
                results.append({'dequipped': equippable_entity})
            else:
                if self.left_ring:
                    results.append({'dequipped': self.left_ring})

                self.left_ring = equippable_entity
                results.append({'equipped': equippable_entity})
        elif slot == EquipmentSlots.RIGHT_RING:
            if self.right_ring == equippable_entity:
                self.right_ring = None
                results.append({'dequipped': equippable_entity})
            else:
                if self.right_ring:
                    results.append({'dequipped': self.right_ring})

                self.right_ring = equippable_entity
                results.append({'equipped': equippable_entity})

        return results