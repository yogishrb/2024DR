#
# DeepRacer Guru
#
# Version 3.0 onwards
#
# Copyright (c) 2021 dmh23
#

from src.tracks.track import Track
import src.personalize.configuration.personal_track_annotations as config


class DBroSuperRacewayClockwiseTrack(Track):
    def __init__(self):
        super().__init__()

        self._ui_name = "DBro Super Raceway (Clockwise)"
        self._ui_description = "Named after the 2021 AWS DeepRacer finalist Darren \"DBro\" Broderick, the DBro Super Raceway features 2 lightning fast dragstrips and an unforgiving technical section of hairpin turns and cutbacks. Do you have what it takes to advance or will get caught doing DOH-nuts in the green?"
        self._ui_length_in_m = 99.99  # metres     (NOT STATED)
        self._ui_width_in_cm = 107  # centimetres
        self._world_name = "2022_july_pro_cw"
        self._track_sector_dividers = [21, 51, 82, 114, 133, 162]
        self._annotations = config.dbro_super_raceway_cw_annotations
        self._track_width = 1.067

        self._track_waypoints = [(-6.447149331851105, -2.4333889162581492), (-6.573129892349243, -2.401312470436096),
                                 (-6.699078375300187, -2.3691103021495366), (-6.865572929382324, -2.3265414237976074),
                                 (-7.1579430103302, -2.2514835000038147), (-7.450248956680298, -2.176177978515625),
                                 (-7.742079019546509, -2.0991119742393494), (-8.020486116409302, -1.98386549949646),
                                 (-8.261571407318115, -1.8040065169334412), (-8.433274984359741, -1.5575109720230103),
                                 (-8.51435899734497, -1.2680194973945618), (-8.514319658279419, -0.9668484628200531),
                                 (-8.458262920379639, -0.6704287827014923), (-8.390861511230469, -0.37620075047016144),
                                 (-8.32137942314148, -0.08245743811130524), (-8.252684593200684, 0.2114698588848114),
                                 (-8.18458867073059, 0.5055389553308487), (-8.116528749465942, 0.7996161580085754),
                                 (-8.048567771911621, 1.0937164723873138), (-7.980424404144287, 1.3877745270729065),
                                 (-7.912452697753906, 1.6818724870681763), (-7.844434022903442, 1.9759594798088074),
                                 (-7.77717924118042, 2.270221471786499), (-7.681424617767334, 2.5560719966888428),
                                 (-7.535841464996338, 2.8199959993362427), (-7.343933343887329, 3.05245304107666),
                                 (-7.112224340438843, 3.2452110052108765), (-6.848181962966919, 3.390564441680908),
                                 (-6.561760425567627, 3.4845058917999268), (-6.262929439544678, 3.5239850282669067),
                                 (-5.96207857131958, 3.5066274404525757), (-5.673314571380615, 3.421480417251587),
                                 (-5.417525053024292, 3.262850046157837), (-5.210888862609863, 3.043877959251404),
                                 (-5.050729990005493, 2.7882049083709717), (-4.921410322189331, 2.515984535217285),
                                 (-4.869795560836792, 2.2196919918060303), (-4.882845640182495, 1.9183470010757446),
                                 (-4.924807071685791, 1.6195579767227173), (-4.9923505783081055, 1.3253700137138367),
                                 (-5.057512521743774, 1.030641883611679), (-5.112820386886597, 0.733938604593277),
                                 (-5.153539419174194, 0.4348699599504471), (-5.187462568283081, 0.1349322311580181),
                                 (-5.200091123580933, -0.16604389995336533), (-5.119199514389038, -0.4550444409251213),
                                 (-4.93490743637085, -0.6919849365949631), (-4.685449123382568, -0.8605382144451141),
                                 (-4.406970024108887, -0.9762759208679199), (-4.116514444351196, -1.0580480694770813),
                                 (-3.820660948753357, -1.1177117228507996), (-3.522355079650879, -1.1637449860572815),
                                 (-3.223037004470825, -1.2027412056922913), (-2.9234960079193115, -1.240010142326355),
                                 (-2.624486565589905, -1.2812519967556), (-2.323142886161804, -1.2720179855823517),
                                 (-2.0255469679832494, -1.2229165136814124), (-1.7394269704818726, -1.1279720962047577),
                                 (-1.4779254794120789, -0.9783599972724915), (-1.256562739610672, -0.7741460800170898),
                                 (-1.087897926568985, -0.5246888995170593), (-0.977816000580789, -0.2437012605369124),
                                 (-0.8779684156179428, 0.041153401136398315), (-0.7819591164588928, 0.3273315578699112),
                                 (-0.7948786169290566, 0.6264034062624012), (-0.9605954885482788, 0.8742117285728455),
                                 (-1.2338539958000183, 0.9853432774543762), (-1.5277130007743835, 1.054288238286972),
                                 (-1.8200019598007202, 1.1293844878673553), (-2.0884470343589783, 1.2630782723426819),
                                 (-2.3119744658470154, 1.4652690291404724), (-2.4931105375289917, 1.7061864733695984),
                                 (-2.600888967514038, 1.9853089451789856), (-2.58971107006073, 2.285825490951538),
                                 (-2.498346447944641, 2.5727490186691284), (-2.33501797914505, 2.8256255388259888),
                                 (-2.114531993865967, 3.0303280353546143), (-1.8429400324821472, 3.159306049346924),
                                 (-1.545773983001709, 3.207242012023926), (-1.2448800206184387, 3.2099889516830444),
                                 (-0.9432541728019714, 3.198803424835205), (-0.6416989862918854, 3.1854549646377563),
                                 (-0.3401384949684143, 3.172228455543518), (-0.038564921356737614, 3.1593040227890015),
                                 (0.26301050186157227, 3.146422028541565), (0.5645949244499207, 3.133753538131714),
                                 (0.8662009537220001, 3.1216095685958862), (1.1678270101547241, 3.109982967376709),
                                 (1.4695419669151306, 3.1009689569473267), (1.7713019847869873, 3.0936014652252197),
                                 (2.0730855464935303, 3.087244987487793), (2.3748815059661865, 3.0815364122390747),
                                 (2.6766855716705322, 3.0762410163879395), (2.9784939289093018, 3.0711859464645386),
                                 (3.280303955078125, 3.0662394762039185), (3.582116484642029, 3.061476469039917),
                                 (3.8839304447174072, 3.0567744970321655), (4.185742139816284, 3.0519055128097534),
                                 (4.487545490264893, 3.04659903049469), (4.789340496063232, 3.040802001953125),
                                 (5.0911195278167725, 3.034272074699402), (5.392870903015137, 3.026471495628357),
                                 (5.694461345672607, 3.0184175968170166), (5.982843399047852, 2.935001015663147),
                                 (6.210744619369507, 2.7412644624710083), (6.32113242149353, 2.4634064435958862),
                                 (6.3036065101623535, 2.163899064064026), (6.195310831069946, 1.8828175067901611),
                                 (6.0712621212005615, 1.6079645156860352), (6.021308898925781, 1.311813950538637),
                                 (6.092617511749268, 1.0207939445972443), (6.257611036300659, 0.7689677774906158),
                                 (6.452111005783081, 0.5381364971399307), (6.647353410720825, 0.3079321961849928),
                                 (6.842753887176514, 0.07786199450492859), (7.037793874740601, -0.15251414477825165),
                                 (7.232665061950684, -0.3830326981842518), (7.427494525909424, -0.6135869473218918),
                                 (7.622272729873657, -0.844184398651123), (7.816641092300415, -1.0751271843910217),
                                 (8.010629892349243, -1.3063882291316986), (8.203759908676147, -1.5383610129356384),
                                 (8.374521255493164, -1.7868379354476929), (8.489338874816895, -2.065041959285736),
                                 (8.52122688293457, -2.3639509677886963), (8.44628119468689, -2.6543564796447754),
                                 (8.262760639190674, -2.891366958618164), (8.002684831619263, -3.0414669513702393),
                                 (7.70804762840271, -3.102199912071228), (7.406553506851196, -3.1168824434280396),
                                 (7.10502552986145, -3.1308130025863647), (6.803467512130737, -3.144094467163086),
                                 (6.501899003982544, -3.1571240425109863), (6.200363397598267, -3.170833468437195),
                                 (5.899013042449951, -3.1871365308761597), (5.597304105758667, -3.1963425874710083),
                                 (5.295549631118774, -3.2039530277252197), (4.993779420852661, -3.2109129428863525),
                                 (4.692076921463013, -3.204439401626587), (4.392222881317139, -3.170873999595642),
                                 (4.09946346282959, -3.098660469055176), (3.832038998603821, -2.9614189863204956),
                                 (3.6575865745544434, -2.7209094762802124), (3.5961605310440063, -2.4257094860076904),
                                 (3.5717644691467285, -2.1249284744262695), (3.568381428718567, -1.8231300115585327),
                                 (3.5792324542999268, -1.521491527557373), (3.600917935371399, -1.2204325199127197),
                                 (3.6320645809173584, -0.9202044904232025), (3.674775004386902, -0.6214337944984429),
                                 (3.6847530603408813, -0.3206197917461395), (3.6152584552764893, -0.02777249366044998),
                                 (3.4721189737319946, 0.23704568669199944), (3.268003463745117, 0.4584228377789259),
                                 (3.0206304788589478, 0.6307245790958405), (2.73406445980072, 0.717385821044445),
                                 (2.4426335096359253, 0.6534031331539154), (2.204972505569458, 0.46965987607836723),
                                 (2.024064004421234, 0.22871835343539715), (1.8926109671592712, -0.042922504246234894),
                                 (1.7638815641403198, -0.3159472681581974), (1.6326404809951782, -0.5877677947282791),
                                 (1.4950129985809326, -0.8564122915267944), (1.353177934885025, -1.1228616833686829),
                                 (1.208965539932251, -1.3880339860916138), (1.06429922580719, -1.6529589891433716),
                                 (0.9201977998018265, -1.9181914329528809), (0.7780192792415619, -2.1844590306282043),
                                 (0.6387056708335876, -2.4522359371185303), (0.5014405772089958, -2.721052050590515),
                                 (0.34149083122611046, -2.9768195152282715), (0.14640764147043228, -3.206678032875061),
                                 (-0.0916413962841034, -3.390991449356079), (-0.3746206909418106, -3.490318536758423),
                                 (-0.6759431958198547, -3.5040879249572754), (-0.9774762988090515, -3.5177664756774902),
                                 (-1.279246985912323, -3.5245211124420166), (-1.58108651638031, -3.5247809886932373),
                                 (-1.8827984929084778, -3.5160040855407715), (-2.183835029602051, -3.494354009628296),
                                 (-2.483736991882324, -3.460755467414856), (-2.780537486076355, -3.406031012535095),
                                 (-3.073968529701233, -3.3353394269943237), (-3.3648725748062134, -3.254815459251404),
                                 (-3.6540554761886597, -3.168297052383423), (-3.9429640769958496, -3.080859899520874),
                                 (-4.233242988586426, -2.998112916946411), (-4.525368928909302, -2.9221194982528687),
                                 (-4.817789077758789, -2.8472574949264526), (-5.110229969024658, -2.7724785804748535),
                                 (-5.402757883071899, -2.6980406045913696), (-5.6954004764556885, -2.6240519285202026),
                                 (-5.9880383014678955, -2.5500504970550537), (-6.2806127071380615, -2.4757915139198303),
                                 (-6.447149331851105, -2.4333889162581492)]
