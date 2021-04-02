from src.tracks.track import Track
import src.configuration.personal_track_annotations as config


class LarsLoopTrack(Track):
    def __init__(self):
        super().__init__()

        self._ui_name = "Lars Loop"
        self._ui_description = "Lars Loop is a short track comprised of a modified oval with increasing radius and double apex, a varying double chicane, and a broad hairpin final stretch. It is named in honor of 2020 AWS DeepRacer League silver medalist Lars Ludvigson (Duckworth)."
        self._ui_length_in_m = 99.99  # metres  (99.99 = not stated in AWS DR GUI)
        self._ui_width_in_cm = 107  # centimetres   # TODO
        self._world_name = "thunder_hill_open"
        self._track_sector_dividers = [24, 48, 69]
        self._annotations = config.lars_loop_annotations
        self._track_width = 1.066

        self._track_waypoints = [(1.5632755160331726, -1.4320791363716125), (2.0709489583969116, -1.4242927730083466),
                                 (2.578621983528137, -1.4164928197860718), (3.086295962333679, -1.408689171075821),
                                 (3.593969464302063, -1.4008894562721252), (4.097454071044922, -1.3479962646961212),
                                 (4.563138484954834, -1.1505840718746185), (4.948174476623535, -0.8225848972797394),
                                 (5.260157108306885, -0.42210645973682404), (5.547274827957153, -0.003481656312942505),
                                 (5.792325496673584, 0.4407728388905525), (5.980076551437378, 0.9123452305793762),
                                 (6.138317346572876, 1.3947489857673645), (6.2796430587768555, 1.8824004530906677),
                                 (6.408977508544922, 2.3733750581741333), (6.528566360473633, 2.8668160438537598),
                                 (6.596945524215698, 3.3684329986572266), (6.527557134628296, 3.8692755699157715),
                                 (6.250279903411865, 4.285546541213989), (5.793073892593384, 4.501644611358643),
                                 (5.296926021575928, 4.602712392807007), (4.798203945159912, 4.532587051391602),
                                 (4.410511612892151, 4.2167640924453735), (4.21301007270813, 3.750952959060669),
                                 (4.059242129325867, 3.2670775651931763), (3.9155349731445312, 2.7801125049591064),
                                 (3.779893398284912, 2.2908374071121216), (3.5723224878311157, 1.8361100554466248),
                                 (3.1921374797821045, 1.503767967224121), (2.7076685428619434, 1.3743309378623976),
                                 (2.221081018447876, 1.5036619901657104), (1.8219599723815918, 1.8136704564094543),
                                 (1.5148040056228638, 2.2138710618019104), (1.04414701461792, 2.3895634412765503),
                                 (0.5572960525751114, 2.277476489543915), (0.16184110566974014, 1.9604640603065517),
                                 (-0.29436104744672775, 1.7458440065383911), (-0.7919313609600067, 1.7488374710083008),
                                 (-1.039209634065628, 1.311969518661499), (-1.348665475845337, 0.9352428764104843),
                                 (-1.8498529791832004, 0.9114399254322063), (-2.3272935152053833, 1.0742363631725311),
                                 (-2.728696107864382, 1.3836716413497951), (-3.0530240535736084, 1.7730545401573181),
                                 (-3.308995485305785, 2.2108450531959516), (-3.7223395109176636, 2.4906630516052246),
                                 (-4.225600481033325, 2.5149030089378357), (-4.6698198318481445, 2.2873809337615967),
                                 (-5.048052072525024, 1.9490769505500793), (-5.381816387176514, 1.5671890377998352),
                                 (-5.666332006454468, 1.1468691527843475), (-5.9167890548706055, 0.7053375393152237),
                                 (-6.134303331375122, 0.24667788669466972), (-6.315459966659546, -0.22749889083206654),
                                 (-6.45617938041687, -0.7151507139205933), (-6.545801639556885, -1.2146444916725159),
                                 (-6.578178405761719, -1.7211750149726868), (-6.591742992401123, -2.228720545768738),
                                 (-6.596933603286743, -2.736422538757324), (-6.59478235244751, -3.244147539138794),
                                 (-6.585933446884155, -3.751800537109375), (-6.569818496704102, -4.259271860122681),
                                 (-6.222153902053833, -4.578674554824829), (-5.716580390930176, -4.59562349319458),
                                 (-5.2089478969573975, -4.589447021484375), (-4.701385021209717, -4.60211443901062),
                                 (-4.701385021209717, -4.60211443901062), (-4.233348488807678, -4.43516993522644),
                                 (-3.949254870414734, -4.020798563957214), (-3.7455984354019165, -3.555709481239319),
                                 (-3.5504571199417114, -3.0869795083999634), (-3.3622305393218994, -2.6154290437698364),
                                 (-3.1803709268569946, -2.141385495662689), (-2.967740058898926, -1.6886879801750183),
                                 (-2.497014045715332, -1.5133024752140045), (-1.9904460310935974, -1.4861254394054413),
                                 (-1.4827749729156494, -1.478088229894638), (-0.9750929772853851, -1.4709674715995789),
                                 (-0.4674128443002701, -1.4637114703655243),
                                 (0.040260784327984744, -1.4559287428855896), (0.5479313433170319, -1.4479000866413116),
                                 (1.055602490901947, -1.4399209320545197), (1.5632755160331726, -1.4320791363716125)]
