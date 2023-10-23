from libqtile.config import Group
from icons import group_icons, group_screen
from libqtile.config import Click, Drag, Key, ScratchPad, DropDown

class CreateGroups:
    group_names = group_icons

    def init_groups(self):
        """
        Return the groups of Qtile
        """
        #### First and last
        # groups = [Group(name, layout="monadtall") if name == self.group_names[0]
        #           else Group(name, layout="floating")
        #           if name == self.group_names[-1] else Group(name, layout="monadtall")
        #           for name in self.group_names]
        # print(group_icons)
        # print(group_screen)
        # groups = [Group(info[0], layout="monadtall", screen_affinity=info[1]) for info in zip(group_icons, group_screen)]
        groups = []
        for info in zip(group_icons, group_screen):
            # print(info[0], ':', info[1])
            group = Group(info[0], layout="monadtall", screen_affinity=info[1])
            # print(group)
            groups.append(group)
        # print(groups)
        groups.append(
                ScratchPad("scratchpad", [
                    DropDown('term', 'alacritty', opacity=0.8, height=0.5, width=0.8)
                    ])
                )
        return groups


if __name__ == "__main__":
    v = CreateGroups()
    v.init_groups()

