#!/usr/bin/env python3
from mindmap_leaf import MindMapLeaf
from mindmap_composite import MindMapComposite

def main():
    if __name__ == "__main__":
        # Root of the mindmap
        root = MindMapComposite( "The Battle at Wolf 359", "circle" )

        characters = MindMapComposite( "Characters", "oval" )
        characters.add_child( MindMapLeaf( "Jean-Luc Picard / Locutus", "plain" ) )
        characters.add_child( MindMapLeaf( "William Riker", "plain" ) )
        characters.add_child( MindMapLeaf( "Data", "plain" ) )
        characters.add_child( MindMapLeaf( "Worf", "plain" ) )
        characters.add_child( MindMapLeaf( "Borg Queen (implied presence)", "plain" ) )
        root.add_child( characters )

        plot_points = MindMapComposite( "Plot Points", "square" )
        plot_points.add_child( MindMapLeaf( "Picard is assimilated by the Borg", "plain" ) )
        plot_points.add_child( MindMapLeaf( "Riker takes command of the Enterprise", "plain" ) )
        plot_points.add_child( MindMapLeaf( "The Federation fleet suffers heavy losses", "plain" ) )
        plot_points.add_child( MindMapLeaf( "Enterprise crew devises a plan to stop the Borg", "plain" ) )
        root.add_child( plot_points )

        themes = MindMapComposite( "Themes", "cloud" )
        themes.add_child( MindMapLeaf( "Identity and loss of self", "plain" ) )
        themes.add_child( MindMapLeaf( "Duty and leadership", "plain" ) )
        themes.add_child( MindMapLeaf( "Humanity vs. technology", "plain" ) )
        themes.add_child( MindMapLeaf( "Collectivism vs. individuality", "plain" ) )
        root.add_child( themes )

        setting = MindMapComposite( "Setting", "hexagon" )
        setting.add_child( MindMapLeaf( "USS Enterprise-D", "plain" ) )
        setting.add_child( MindMapLeaf( "Wolf 359 (space battle location)", "plain" ) )
        setting.add_child( MindMapLeaf( "Borg Cube", "plain" ) )
        setting.add_child( MindMapLeaf( "Starfleet Command (background communication)", "plain" ) )
        root.add_child( setting )

        conflicts = MindMapComposite( "Major Conflicts", "bang" )
        conflicts.add_child( MindMapLeaf( "Federation vs. Borg (existential threat)", "plain" ) )
        conflicts.add_child( MindMapLeaf( "Riker’s internal struggle as acting captain", "plain" ) )
        conflicts.add_child( MindMapLeaf( "Enterprise's fight to save Picard from assimilation", "plain" ) )
        root.add_child( conflicts )

        dialogue = MindMapComposite( "Dialogue Highlights", "oval" )
        dialogue.add_child( MindMapLeaf( "“I am Locutus of Borg. Resistance is futile.”", "plain" ) )
        dialogue.add_child( MindMapLeaf( "Riker: \"Mr. Worf, fire.\"", "plain" ) )
        dialogue.add_child( MindMapLeaf( "Guinan advising Riker on letting go of Picard", "plain" ) )
        root.add_child( dialogue )

        stage_directions = MindMapComposite( "Significant Stage Directions", "square" )
        stage_directions.add_child( MindMapLeaf( "Close-up of Picard’s face as Locutus", "plain" ) )
        stage_directions.add_child( MindMapLeaf( "Panoramic view of the devastated fleet at Wolf 359", "plain" ) )
        stage_directions.add_child( MindMapLeaf( "Enterprise maneuvering to evade the Borg", "plain" ) )
        stage_directions.add_child( MindMapLeaf( "Tense bridge scenes as the crew works together", "plain" ) )
        root.add_child( stage_directions )

        root.display()


if __name__ == "__main__":
    main()